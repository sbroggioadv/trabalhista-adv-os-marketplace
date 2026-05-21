---
description: Submete um documento trabalhista a auditoria final da Suprema Corte (R1-R2-R3-R4) antes da entrega.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [documento a auditar]
---

Voce foi acionado pelo comando `/revisao-trabalhista-final` do plugin Trabalhista-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** auditar um documento trabalhista pela Suprema Corte antes da entrega.

## PROTOCOLO

1. **Acionar a skill `suprema-corte-trabalhista`**.
2. Identificar o documento a auditar e o polo do cliente (`CASO.md`).
3. Executar a sequencia obrigatoria: **R1** (coleta de dados) -> **R2** (base juridica — inclui prazo recursal correto e prescricao) -> **R3** (tese — inclui coerencia de polo) -> **R4** (completude e estilo).
4. Cada etapa emite APROVADO / APROVADO COM RESSALVAS / REPROVADO. Reprovacao bloqueia e devolve ao Tenente produtor.
5. Apresentar o relatorio final consolidado.

Bypass disponivel: `--no-corte`, `--quick`.

**Skill a acionar:** `suprema-corte-trabalhista`.
