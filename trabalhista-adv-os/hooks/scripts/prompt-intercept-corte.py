#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Trabalhista-Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-corte`, `--quick`, `--no-suprema`, `/corte off`.
3. Detecta GATILHO TRABALHISTA via keywords (3 niveis):
   - Gatilho 1: prompt contem palavra "trabalhista" (case insensitive)
   - Gatilho 2: keywords fortes do dominio (CLT, vinculo, horas extras, FGTS,
     justa causa, vara do trabalho, TRT, TST, etc.)
   - Gatilho 3: comandos `/start-trabalhista`, `/trabalhista-master`, etc.
4. Se gatilho dispara:
   - Verifica se `trabalhista/cowork-state.json` existe no path atual
   - SIM: injeta protocolo R1-R4 + aponta para skill `trabalhista-master`
   - NAO: sugere `/start-trabalhista` ao usuario (mas nao bloqueia)
5. Se ha bypass: reafirma em stdout que o bypass foi aceito (transparencia).
6. Se nao eh tarefa trabalhista nem juridica geral: silencio (exit 0 sem output).

Tambem respeita state.json: se `suprema_corte.enabled = false`, nunca injeta R1-R4.

Stdlib only.
"""

from __future__ import annotations

import io
import json
import os
import re
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).resolve().parent
PLUGIN_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))

import importlib.util
spec = importlib.util.spec_from_file_location("hook_utils", PLUGIN_ROOT / "scripts" / "hook-utils.py")
hook_utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook_utils)


# Gatilho 1: palavra "trabalhista" (com/sem acento, variantes, case insensitive)
TRIGGER_TRABALHISTA = [
    r"\btrabalhista\b",
    r"\btrabalhistas\b",
    r"\btrabalhistico\b",
    r"\bjustica\s+do\s+trabalho\b",
    r"\bjustiça\s+do\s+trabalho\b",
    r"\bdireito\s+do\s+trabalho\b",
]

# Gatilho 2: keywords fortes do dominio trabalhista brasileiro
DOMAIN_KEYWORDS = [
    # Diplomas e orgaos
    r"\bCLT\b", r"\bTST\b", r"\bTRT\b", r"\bSDI\b", r"\bSDC\b",
    r"\bvara\s+do\s+trabalho\b", r"\bMPT\b", r"\bMTE\b",
    # Reclamacao trabalhista
    r"\breclamacao\s+trabalhista\b", r"\breclamação\s+trabalhista\b",
    r"\breclamatoria\b", r"\breclamatória\b",
    r"\breclamante\b", r"\breclamada\b", r"\breclamado\b",
    # Vinculo e contrato
    r"\bvinculo\s+empregaticio\b", r"\bvínculo\s+empregatício\b",
    r"\bvinculo\s+de\s+emprego\b", r"\bvínculo\s+de\s+emprego\b",
    r"\bCTPS\b", r"\bcarteira\s+de\s+trabalho\b",
    r"\bcontrato\s+de\s+trabalho\b",
    # Verbas e direitos
    r"\bhoras\s+extras?\b", r"\bFGTS\b", r"\bverbas\s+rescisorias\b",
    r"\bverbas\s+rescisórias\b", r"\bTRCT\b",
    r"\badicional\s+de\s+insalubridade\b", r"\badicional\s+de\s+periculosidade\b",
    r"\binsalubridade\b", r"\bpericulosidade\b",
    r"\baviso\s+previo\b", r"\baviso\s+prévio\b",
    r"\bdecimo\s+terceiro\b", r"\bdécimo\s+terceiro\b",
    r"\bferias\b", r"\bférias\b", r"\bequiparacao\s+salarial\b",
    r"\bequiparação\s+salarial\b", r"\bjornada\b", r"\bintrajornada\b",
    r"\binterjornada\b", r"\bbanco\s+de\s+horas\b",
    # Rescisao
    r"\bjusta\s+causa\b", r"\brescisao\s+indireta\b", r"\brescisão\s+indireta\b",
    r"\bdispensa\s+sem\s+justa\s+causa\b", r"\bdemissao\b", r"\bdemissão\b",
    # Estabilidades
    r"\bestabilidade\s+gestante\b", r"\bestabilidade\s+acidentaria\b",
    r"\bestabilidade\s+acidentária\b", r"\bgarantia\s+de\s+emprego\b",
    r"\bcipeiro\b",
    # Pecas e fases
    r"\bcontestacao\s+trabalhista\b", r"\bcontestação\s+trabalhista\b",
    r"\baudiencia\s+una\b", r"\baudiência\s+una\b",
    r"\baudiencia\s+de\s+instrucao\b", r"\baudiência\s+de\s+instrução\b",
    r"\brazoes\s+finais\b", r"\brazões\s+finais\b",
    # Recursos trabalhistas
    r"\brecurso\s+ordinario\b", r"\brecurso\s+ordinário\b",
    r"\brecurso\s+de\s+revista\b", r"\bAIRR\b", r"\bagravo\s+de\s+peticao\b",
    r"\bagravo\s+de\s+petição\b", r"\btranscendencia\b", r"\btranscendência\b",
    # Normas coletivas
    r"\bCCT\b", r"\bACT\b", r"\bconvencao\s+coletiva\b", r"\bconvenção\s+coletiva\b",
    r"\bacordo\s+coletivo\b", r"\bnorma\s+coletiva\b", r"\bdissidio\s+coletivo\b",
    r"\bdissídio\s+coletivo\b",
    # Conceitos
    r"\bReforma\s+Trabalhista\b", r"\bLei\s+13\.?467\b",
    r"\bonus\s+da\s+prova\b", r"\bônus\s+da\s+prova\b",
    r"\bgrupo\s+economico\b", r"\bgrupo\s+econômico\b",
    r"\bterceirizacao\b", r"\bterceirização\b",
    r"\bsucessao\s+trabalhista\b", r"\bsucessão\s+trabalhista\b",
    r"\bdano\s+moral\s+trabalhista\b", r"\bacidente\s+de\s+trabalho\b",
    r"\bcartao\s+de\s+ponto\b", r"\bcartão\s+de\s+ponto\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-trabalhista",
    "/trabalhista-master",
    "/caso-trabalhista",
    "/peticao-trabalhista",
    "/contestacao-trabalhista",
    "/recurso-trabalhista",
    "/parecer-trabalhista",
    "/calculo-trabalhista",
    "/jurisprudencia-trabalhista",
    "/revisao-trabalhista-final",
    "/status-trabalhista",
]

# Keywords juridicas gerais (fallback — se prompt e juridico mas nao trabalhista,
# ainda assim aplica protocolo cauteloso de Suprema Corte)
LEGAL_KEYWORDS_GENERAL = [
    r"\bpeticao\b", r"\bpetição\b", r"\bcontestacao\b", r"\bcontestação\b",
    r"\brecurso\b", r"\bapelacao\b", r"\bapelação\b",
    r"\bembargos\b", r"\breplica\b", r"\bréplica\b",
    r"\bparecer\b", r"\bjurisprudencia\b", r"\bjurisprudência\b",
    r"\bsentenca\b", r"\bsentença\b", r"\bdecisao\b", r"\bdecisão\b",
    r"\baudiencia\b", r"\baudiência\b", r"\bprocesso\b",
]

BYPASS_TOKENS = [
    "--no-corte",
    "--no-suprema",
    "--quick",
    "/corte off",
    "/corte-off",
]


def _load_input() -> dict:
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except Exception:
        return {}


def _matches_any(text: str, patterns: list[str]) -> bool:
    for pat in patterns:
        if re.search(pat, text, re.IGNORECASE):
            return True
    return False


def _is_trabalhista(prompt: str) -> bool:
    """Detecta se o prompt e do dominio trabalhista (gatilhos 1, 2 ou 3)."""
    if _matches_any(prompt, TRIGGER_TRABALHISTA):
        return True
    if _matches_any(prompt, DOMAIN_KEYWORDS):
        return True
    low = prompt.lower()
    for cmd in PLUGIN_COMMANDS:
        if cmd.lower() in low:
            return True
    return False


def _is_legal_general(prompt: str) -> bool:
    """Detecta se e tarefa juridica em geral (mesmo nao sendo trabalhista)."""
    return _matches_any(prompt, LEGAL_KEYWORDS_GENERAL)


def _has_bypass(prompt: str) -> str | None:
    low = prompt.lower()
    for token in BYPASS_TOKENS:
        if token in low:
            return token
    return None


def _has_trabalhista_state(cowork: Path | None) -> bool:
    """Verifica se existe `trabalhista/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "trabalhista" / "cowork-state.json").exists()


def _suprema_corte_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica suprema_corte.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "trabalhista" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("suprema_corte", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env TRABALHISTA_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("TRABALHISTA_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "trabalhista" / "cowork-state.json").exists():
            return p
    return hook_utils.find_cowork(Path.cwd())


def main() -> int:
    payload = _load_input()
    prompt = payload.get("prompt") or payload.get("user_prompt") or ""
    if not isinstance(prompt, str) or not prompt.strip():
        return 0

    cowork = _resolve_cowork()
    bypass = _has_bypass(prompt)

    is_trab = _is_trabalhista(prompt)
    is_legal_other = _is_legal_general(prompt) and not is_trab

    # Caso 1: bypass explicito
    if bypass and (is_trab or is_legal_other):
        sys.stdout.write(
            f"[trabalhista-adv-os] Bypass detectado ({bypass}). "
            "Pecas, recursos, pareceres e calculos serao entregues SEM validacao "
            "da Suprema Corte (R1-R4). Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa trabalhista + plugin configurado
    if is_trab and _has_trabalhista_state(cowork):
        if not _suprema_corte_enabled(cowork):
            sys.stdout.write(
                "[trabalhista-adv-os] Demanda trabalhista detectada. "
                "Suprema Corte DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: trabalhista-master.\n"
            )
        else:
            sys.stdout.write(
                "[trabalhista-adv-os] Demanda trabalhista detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `trabalhista-master` (Tier 0 — sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as 24 Proibicoes Absolutas (PA-01 a PA-24), com atencao especial:\n"
                "   - PA-05: coerencia de polo (peca alinhada ao lado do cliente no CASO.md)\n"
                "   - PA-07: nao aplicar a Reforma 13.467/2017 a fato anterior a 11/11/2017\n"
                "   - PA-08: prazo recursal correto (RO/RR/AIRR 8 dias; ED 5 dias; RE/ARE 15 dias)\n"
                "   - PA-09: prescricao bienal e quinquenal\n"
                "   - PA-15: nao analisar pedido sem documento essencial\n"
                "   - PA-23: nao aplicar CDC a relacao de emprego\n"
                "4. Acionar os 7 Protocolos da Camada 2 conforme demanda\n"
                "5. Antes de entregar: Suprema Corte R1->R2->R3->R4 (PA-24)\n"
                "\n"
                "Bypass disponivel: `--no-corte`, `--quick`, `/corte off`.\n"
            )
        return 0

    # Caso 3: tarefa trabalhista mas plugin NAO configurado
    if is_trab and not _has_trabalhista_state(cowork):
        sys.stdout.write(
            "[trabalhista-adv-os] Detectei demanda trabalhista, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-trabalhista para configurar (~5 min).\n"
            "Vou criar uma pasta `trabalhista/` aqui com sua identidade, polos de "
            "atuacao, tom de voz e configuracao das skills trabalhistas.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa juridica geral (nao trabalhista) — protocolo cauteloso
    if is_legal_other:
        sys.stdout.write(
            "[trabalhista-adv-os] Tarefa juridica detectada (nao especificamente trabalhista). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas).\n"
            "2. Apresentar estrutura + premissas antes de redigir.\n"
            "3. Aguardar confirmacao do usuario.\n"
            "4. Antes de entregar: executar Suprema Corte R1-R4 se aplicavel.\n"
            "Bypass: `--no-corte`, `--quick`, `/corte off`.\n"
        )
        return 0

    # Caso default: nao e tarefa juridica, nem trabalhista — silencio
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
