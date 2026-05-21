---
description: Produz a contestacao empresarial em Reclamacao Trabalhista — preliminares, prejudiciais, impugnacao ponto a ponto.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [contexto da contestacao]
---

Voce foi acionado pelo comando `/contestacao-trabalhista` do plugin Trabalhista-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** produzir a contestacao empresarial (lado reclamada).

## PROTOCOLO

1. **Confirmar o polo no `CASO.md`** — esta skill e do lado reclamada. Se o cliente e o reclamante, redirecionar para `/peticao-trabalhista` (peticao inicial / replica).
2. **Acionar a skill `contestacao-trabalhista`**.
3. Garantir que o pipeline foi cumprido (triagem -> auditoria documental + CCT -> trilateral + jurisprudencia -> linha estrategica validada).
4. A contestacao cobre: preliminares, prejudiciais (prescricao), impugnacao especifica aos fatos, impugnacao ponto a ponto dos pedidos, onus da prova, gratuidade, sucumbencia, requerimentos.
5. Apos a redacao, auditoria obrigatoria pela `suprema-corte-trabalhista` (R1-R4).

**Skill a acionar:** `contestacao-trabalhista`.
