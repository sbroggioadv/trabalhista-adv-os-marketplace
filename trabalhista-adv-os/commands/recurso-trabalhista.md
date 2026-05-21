---
description: Produz o recurso trabalhista cabivel (ou a contrarrazao) — roteia para a skill recursal conforme o tipo, com o prazo correto.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [RO | RR | AIRR | agravo | ED | RE | embargos-tst | acao-autonoma]
---

Voce foi acionado pelo comando `/recurso-trabalhista` do plugin Trabalhista-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** produzir o recurso trabalhista (ou a peca de resposta) cabivel.

## PROTOCOLO

1. **Identificar o tipo de recurso** — do argumento, ou pela analise da decisao recorrida.
2. **Rotear para a skill recursal:**
   - `RO` -> `recurso-ordinario-trabalhista` (8 dias uteis)
   - `RR` / `AIRR` -> `recurso-revista-trabalhista` (8 dias uteis)
   - `embargos-tst` -> `embargos-tst-trabalhista` (8 dias uteis)
   - `agravo` -> `agravos-trabalhistas` (8 dias / 48h)
   - `ED` -> `embargos-declaracao-trabalhista` (**5 dias uteis**)
   - `RE` -> `recurso-extraordinario-trabalhista` (**15 dias uteis** — excecao)
   - `acao-autonoma` (MS, rescisoria, correicao, reclamacao) -> `acoes-autonomas-impugnacao-trabalhista`
3. **Antes de redigir**, considerar acionar `pareceres-viabilidade-recursal` para avaliar cabimento, prazo e prognostico.
4. **Modo dual:** ler quem recorreu no `CASO.md` — produzir o recurso (se o cliente recorre) ou a contrarrazao/contraminuta (se a outra parte recorreu).
5. **Cravar o prazo** conforme o Protocolo 7. Confundir prazo e PA-08.
6. Apos a redacao, auditoria obrigatoria pela `suprema-corte-trabalhista` (R1-R4).

**Skill a acionar:** a skill recursal correspondente ao tipo.
