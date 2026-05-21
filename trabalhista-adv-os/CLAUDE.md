# CLAUDE.md — Plugin Trabalhista-Adv-OS

> Instrucoes para futuras sessoes neste sub-repositorio. Ler PRIMEIRO ao retomar trabalho.
> Estende o CLAUDE.md da familia de plugins Adv-OS e os niveis superiores do workspace.

---

## Identidade do Projeto

- **Nome:** Plugin Trabalhista-Adv-OS
- **Slug:** `trabalhista-adv-os`
- **Tipo:** plugin Claude Code (`.claude-plugin/plugin.json`)
- **Audiencia:** advogados trabalhistas brasileiros — atende os DOIS polos da Reclamacao Trabalhista (reclamante e reclamada)
- **Versao atual:** 0.1.0
- **Plugin de referencia (engine):** `previdenciario-adv-os`
- **Repo marketplace (a criar nas FASES 2-7 do PLAYBOOK):** repo publico `trabalhista-adv-os-marketplace`

---

## REGRA DE OURO — DESPERSONALIZACAO ABSOLUTA (PLUGIN COMERCIAL)

Este plugin sera **comercializado** (Kirvano via marketplace GitHub publico). Sem `authorship_whitelist`. **Zero mencoes** ao criador da metodologia em qualquer arquivo distribuido.

**ZERO mencoes permitidas (ver `audit/forbidden-terms.json` para lista canonica):**
- Nome do criador da metodologia (qualquer variante) e OAB pessoal
- Email/contato pessoal, escritorio-modelo, mentorias/coworks proprietarios
- Ferramentas proprietarias do escritorio de origem, padroes nomeados pessoalmente

Identidade do operador resolvida em **runtime** via persona local em `<cwd>/trabalhista/persona.md` (fora do plugin). Tokens nas skills: `{{ADVOGADO_NOME}}`, `{{ADVOGADO_OAB}}`, `{{ADVOGADO_UF}}`, `{{FIRM_NAME}}`, `{{CIDADE}}`, `{{UF}}`, `{{TOM_VOZ_PERFIL}}`, `{{TOM_VOZ_INTENSIDADE}}`.

```bash
# Antes de CADA commit
python3 audit/audit.py
# Verificacao reforcada pre-release
python3 audit/audit.py --json | jq '.total_matches'   # esperado: 0
```

> **Exceção conhecida:** os 2 arquivos em `.planning/` (design-spec e build-plan) citam fontes de porte e por isso disparam o audit. São dev-only, NÃO vão ao marketplace e são excluídos do scan final do Sprint 9.

---

## Hierarquia das 4 Camadas (Constituicao Operacional)

```
CAMADA 1 — PROIBICOES ABSOLUTAS (PA-01 a PA-25) — inviolaveis
CAMADA 2 — PROTOCOLOS TECNICOS (7)               — aplicacao obrigatoria
CAMADA 3 — IDENTIDADE TECNICA E ESTILO            — FIRAC + estrutura da peca
CAMADA 4 — SKILLS OPERACIONAIS (32, Tier 0/1/2/3) — operacional
```

Camada superior SEMPRE prevalece — inclusive contra instrucao do usuario. Detalhamento:
- `.planning/HIERARQUIA-4-CAMADAS.md` — referencia rapida
- `.planning/PROIBICOES-ABSOLUTAS.md` — PA-01 a PA-25 detalhadas
- `.planning/PROTOCOLOS-TECNICOS.md` — os 7 protocolos
- `.planning/2026-05-20-design-spec.md` — spec integral

---

## Arquitetura em Uma Frase

Plugin trabalhista especializado **side-aware** (32 skills, Tier 0/1/2/3) com **engine portado** do `previdenciario-adv-os` (hooks/scripts/templates) e **governanca juridica** (4 camadas + 25 PAs + 7 protocolos + Suprema Corte R1-R4) injetada via skill `trabalhista-master`. O polo do cliente (reclamante/reclamada) e decidido na `triagem-trabalhista`, gravado no `CASO.md` e lido por todas as skills.

---

## Side-Awareness (decisao de arquitetura nuclear)

**Um unico plugin, orquestrador side-aware** (abordagem A da spec §2.1). A triagem pergunta o polo; skills transversais flipam conforme o lado; apenas as peças de conhecimento (inicial/contestacao/replica) sao especificas de polo. As 8 skills recursais operam em **modo dual** — produzem o recurso E sua contrarrazao/contraminuta conforme a posicao do cliente.

---

## Como Retomar Trabalho

1. **Ler `MEMORY.md`** (raiz) — estado executivo, sprint ativa, proximo passo
2. **Ler `.planning/2026-05-20-build-plan.md`** — plano de 10 sprints
3. **`git status` + `git log -8`** — estado real do repo
4. **`python3 audit/audit.py`** — verificar despersonalizacao (matches so em `.planning/` sao OK)

---

## Padroes a Seguir

1. **Skill folder = so `SKILL.md`.** Material auxiliar vai em `templates/` ou `scripts/data/`.
2. **Limites Cowork:** `SKILL.md` <= 11264 bytes; `description` do frontmatter <= 1024 chars. Validar com `scripts/check-skill-descriptions.py`.
3. **plugin.json minimal:** `name`, `version`, `description`, `author`, `license`.
4. **Tokens `{{...}}`** permanecem LITERAIS no disco — LLM resolve em runtime via persona.
5. **Privacidade LGPD:** pasta `<cwd>/trabalhista/` (e `casos/`) gitignored por default; warning se pasta sincronizada. Compartimentacao por caso e PA-22.
6. **Portabilidade:** scripts Python 3.11+; `${CLAUDE_PLUGIN_ROOT}` em todos os hooks; `${TRABALHISTA_PERSONA}` resolvido por fallback chain.
7. **Commits semanticos** por task — `feat(skill): <nome>`, `feat:`, `chore:`, `docs:`.
8. **Atualizar `MEMORY.md` ANTES de qualquer push.**

---

## Proibicoes

1. **NAO** comecar nova Sprint sem ler `MEMORY.md` e `.planning/2026-05-20-build-plan.md`.
2. **NAO** incluir identidade do criador da metodologia em arquivo distribuido (audit bloqueia).
3. **NAO** colocar `SKILL.md` acima de 11264 bytes nem `description` acima de 1024 chars.
4. **NAO** criar arquivo dentro de `skills/<nome>/` que nao seja `SKILL.md`.
5. **NAO** aceitar instrucao do usuario que conflite com a Camada 1 (PA-01 a PA-25).
6. **NAO** escrever dados de cliente no plugin nem em pasta sincronizada (Dropbox/iCloud/Drive).
7. **NAO** alterar nome/slug do plugin sem nova decisao.

---

## Estrutura do Sub-Repo

```
plugin-trabalhista/
├── .claude-plugin/plugin.json   manifesto minimal
├── .planning/                    docs dev-only (spec, plano, camadas, PAs, protocolos)
├── commands/                     11 commands
├── skills/                       32 skills (Tier 0/1/2/3)
├── hooks/                        hooks.json + 3 scripts
├── context/                      persona-fallback.md
├── templates/                    persona / config / CASO / MEMORY-caso / settings
├── scripts/                      resolve-persona, state, hook-utils, check-skill-descriptions
├── audit/                        forbidden-terms.json + audit.py
├── docs/                         documentacao publica (FAQ, glossario, etc.)
├── README.md / LICENSE / .gitignore / CLAUDE.md / MEMORY.md
```

---

## Comunicacao

- **Idioma:** Portugues (Brasil)
- **Tom dos docs internos:** tecnico, direto, sem mencoes pessoais
- **Tom das skills/commands (para o usuario-cliente):** acolhedor, tecnico, respeita `tom_voz` configurado em runtime
- **Reportes:** ✅ concluido / 🔴 erro / 🏁 sprint finalizada

---

**Ultima atualizacao:** 2026-05-20 (Sprint 0 — scaffold).
