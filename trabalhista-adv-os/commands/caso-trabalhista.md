---
description: Abre um caso trabalhista novo ou retoma um caso existente — cria/le a pasta do caso, o CASO.md e o MEMORY.md.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [nome do caso — ex: joao-silva-x-construtora-alfa]
---

Voce foi acionado pelo comando `/caso-trabalhista` do plugin Trabalhista-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** abrir um caso novo ou retomar um caso existente.

## PROTOCOLO

1. **Acionar a skill `memoria-de-caso-trabalhista`**.
2. Se o argumento corresponde a um caso existente em `trabalhista/casos/`, **retomar** — ler o `CASO.md` e o `MEMORY.md`, apresentar resumo (polo, fase, ultima etapa, pendencias, prazos).
3. Se nao existe, **abrir caso novo** — acionar a `triagem-trabalhista` para colher o polo e os dados, e criar a pasta `casos/<cliente>-x-<adverso>/` com `CASO.md`, `MEMORY.md` e as subpastas.
4. Confirmar com o operador antes de criar.

**Skill a acionar:** `memoria-de-caso-trabalhista` (e `triagem-trabalhista` se for caso novo).
