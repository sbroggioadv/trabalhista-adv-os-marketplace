---
description: Roteia para a peca de conhecimento conforme o polo do cliente — peticao inicial (reclamante) ou contestacao (reclamada).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [contexto da peca]
---

Voce foi acionado pelo comando `/peticao-trabalhista` do plugin Trabalhista-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** produzir a peca de conhecimento do caso, conforme o polo.

## PROTOCOLO

1. **Ler o `Polo do cliente` no `CASO.md`** do caso ativo.
2. **Rotear conforme o polo:**
   - Polo = **reclamante** -> acionar `peticao-inicial-trabalhista` (a Reclamacao Trabalhista).
   - Polo = **reclamada** -> acionar `contestacao-trabalhista` (a defesa empresarial).
   - Polo indefinido -> acionar `triagem-trabalhista` para defini-lo antes.
3. Antes de redigir, garantir que o pipeline foi cumprido (triagem -> auditoria + CCT -> trilateral + jurisprudencia -> linha estrategica validada no Checkpoint 4).
4. Apos a redacao, a peca passa obrigatoriamente pela `suprema-corte-trabalhista` (R1-R4) antes da entrega (PA-24).

**Skill a acionar:** `peticao-inicial-trabalhista` OU `contestacao-trabalhista` conforme o polo.
