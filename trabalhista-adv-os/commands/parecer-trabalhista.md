---
description: Produz um parecer de viabilidade recursal — avalia se vale recorrer ou contra-arrazoar (cabimento, transcendencia, prognostico).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [decisao a avaliar]
---

Voce foi acionado pelo comando `/parecer-trabalhista` do plugin Trabalhista-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** produzir um parecer que avalie a viabilidade de um recurso.

## PROTOCOLO

1. **Acionar a skill `pareceres-viabilidade-recursal`**.
2. Identificar a decisao a avaliar e o polo do cliente (`CASO.md`).
3. O parecer analisa: cabimento e prazo (Protocolo 7), pressupostos recursais, prequestionamento, transcendencia (RR) / repercussao geral (RE), chance de reforma, e custo-beneficio.
4. Entregar a recomendacao objetiva — recorrer / nao recorrer / contra-arrazoar — com prognostico fundamentado (nunca promessa — PA-21).
5. O parecer e parecer; nao se mistura com peca processual (PA-06). Se recomendar recorrer, a peca e produzida depois pela skill recursal.
6. Apos a redacao, auditoria pela `suprema-corte-trabalhista`.

**Skill a acionar:** `pareceres-viabilidade-recursal`.
