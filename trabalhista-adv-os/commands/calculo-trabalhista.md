---
description: Calcula verbas e reflexos trabalhistas — rescisorias, horas extras, adicionais, FGTS, juros e correcao (ADC 58/59 STF).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [o que calcular]
---

Voce foi acionado pelo comando `/calculo-trabalhista` do plugin Trabalhista-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** produzir um calculo trabalhista com memoria detalhada.

## PROTOCOLO

1. **Acionar a skill `calculos-trabalhistas`**.
2. Identificar o que calcular: valor da causa, verbas rescisorias, horas extras, liquidacao, atualizacao.
3. Reunir os dados-base (salario, datas, jornada, modalidade de rescisao) do `CASO.md`. **Sem dado-base, sinalizar Ponto de Omissao e parar** (PA-20).
4. Aplicar as 5 etapas do Protocolo 4: mapear periodo + intertemporal -> apurar verbas -> reflexos -> juros e correcao (ADC 58/59 STF) -> memoria detalhada.
5. Considerar a CCT/ACT (adicionais e piso convencionais) via `cct-normas-coletivas`.
6. Entregar a memoria de calculo auditavel. O calculo e calculo; nao se mistura com peca (PA-06).
7. Apos a producao, auditoria pela `suprema-corte-trabalhista`.

**Skill a acionar:** `calculos-trabalhistas`.
