---
description: Localiza, classifica e prioriza precedentes trabalhistas — busca viva no TST/TRTs/JusBrasil, classificacao em 3 niveis.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch
argument-hint: [tese ou tema a pesquisar]
---

Voce foi acionado pelo comando `/jurisprudencia-trabalhista` do plugin Trabalhista-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** localizar e classificar jurisprudencia trabalhista para uma tese.

## PROTOCOLO

1. **Acionar a skill `jurisprudencia-trabalhista`**.
2. Identificar a tese ou o tema a pesquisar (do argumento ou do caso ativo).
3. Busca viva: `WebSearch`/`WebFetch` nos portais do TST e dos TRTs; `firecrawl` para portais JS-pesados / JusBrasil (se disponivel).
4. Classificar cada precedente nos 3 niveis: Nivel 1 (validada), Nivel 2 (indicativa — `[VERIFICAR]`), Nivel 3 (impossibilidade). **Nunca alucinar** (PA-01).
5. Apresentar os precedentes hierarquizados (STF > TST-SDI > TST-Turmas > TRT), com o uso conforme o polo do cliente.

**Skill a acionar:** `jurisprudencia-trabalhista`.
