---
name: recurso-extraordinario-trabalhista
description: >
  RECURSO EXTRAORDINARIO TRABALHISTA — Skill Tier 2 recursal transversal. Produz o Recurso Extraordinario ao STF (materia constitucional, repercussao geral, prequestionamento) e o Agravo em RE (ARE) contra a inadmissao, alem das contrarrazoes/contraminuta. Prazo: 15 dias uteis (excecao — segue o CPC, nao a CLT). Use quando menciona recurso extraordinario, RE, STF, repercussao geral, ARE.
---

# RECURSO EXTRAORDINARIO TRABALHISTA

> Skill **Tier 2** recursal, transversal, **modo dual**. Produz o Recurso Extraordinario (RE) ao STF e o Agravo em RE (ARE), alem das pecas de resposta. **Prazo de 15 dias** — a excecao do sistema recursal trabalhista.

---

## 0. ESCOPO E ACIONAMENTO

Acionada quando ha acordao do TST (em ultima instancia trabalhista) que contraria a Constituicao, comportando RE ao STF, ou quando o RE foi inadmitido na origem (cabe ARE).

## 1. MODO DUAL — DOIS EIXOS

Side-aware, lido do `CASO.md`:
- **Polo:** reclamante ou reclamada.
- **Posicao:**
  - **recorrente** — o cliente recorre -> **Recurso Extraordinario**.
  - **recorrente com RE inadmitido** — o RE do cliente foi barrado -> **ARE**.
  - **recorrido** — a outra parte recorreu -> **contrarrazoes ao RE** ou **contraminuta ao ARE**.

A peca serve ao polo do cliente (PA-05).

## 2. PRAZO (Protocolo 7) — ATENCAO: 15 DIAS, EXCECAO

**RE, ARE e contrarrazoes/contraminuta: 15 dias uteis.** Esta e a **excecao** do sistema recursal trabalhista: o RE e o ARE ao STF **nao seguem a CLT** — seguem o CPC (art. 1.003 §5o CPC), com prazo de **15 dias uteis**. Aplicar 8 dias (prazo trabalhista tipico) ao RE e erro — PA-08. A skill crava expressamente os 15 dias e justifica a excecao.

## 3. PRESSUPOSTOS DO RE (art. 102 III CF)

O RE so cabe contra causa decidida em ultima instancia quando a decisao:
- contrariar dispositivo da Constituicao; ou
- declarar a inconstitucionalidade de lei ou tratado; ou
- julgar valida lei/ato local contestado em face da Constituicao; ou
- julgar valida lei local contestada em face de lei federal.

Pressupostos especificos:
- **Prequestionamento** — a materia constitucional tem de ter sido enfrentada no acordao do TST (Sumula 282 e 356 STF). ED de prequestionamento sao frequentemente necessarios antes.
- **Repercussao geral** (art. 102 §3o CF; art. 1.035 CPC) — topico obrigatorio: demonstrar a relevancia economica, politica, social ou juridica que ultrapassa o interesse das partes. Sem preliminar formal e fundamentada de repercussao geral, o RE nao e admitido.
- **Ofensa direta** — a violacao a Constituicao deve ser direta e frontal; ofensa reflexa (que depende de exame de lei infraconstitucional) nao enseja RE.

## 4. MODO RECORRENTE — RECURSO EXTRAORDINARIO

```
1. ENDERECAMENTO       — ao TST (juizo de admissibilidade), dirigido ao STF
2. TEMPESTIVIDADE E PREPARO — 15 dias uteis; preparo conforme regras do STF
3. DO PREQUESTIONAMENTO — demonstrar o enfrentamento da materia constitucional
4. DA REPERCUSSAO GERAL — preliminar formal e fundamentada (art. 1.035 CPC)
5. DAS RAZOES          — a violacao direta ao dispositivo constitucional
6. DO PEDIDO           — conhecimento e provimento; reforma do acordao
```

## 5. MODO ARE — AGRAVO EM RE

Inadmitido o RE na origem, cabe **ARE** ao STF (art. 1.042 CPC), em 15 dias uteis, para destrancar o RE. O ARE ataca os fundamentos da decisao de inadmissao.

## 6. MODO RECORRIDO — CONTRARRAZOES / CONTRAMINUTA

Sustentar a ausencia de prequestionamento, a ausencia de repercussao geral, a natureza meramente reflexa da alegada ofensa constitucional, ou a aplicacao de tese de repercussao geral ja firmada em sentido contrario ao recorrente. Subsidiariamente, defender o acordao.

## 7. VEDACOES ESPECIFICAS

- **PA-08** — RE e ARE sao **15 dias uteis** (excecao — CPC, nao CLT); nunca 8 dias.
- **PA-05** — a peca serve ao polo do cliente nos dois eixos.
- **PA-01/PA-11** — Temas de repercussao geral classificados; dispositivo constitucional existente.
- Nunca omitir a preliminar de repercussao geral — sem ela o RE nao e admitido.
- Nao deduzir como RE ofensa meramente reflexa a Constituicao.

## 8. INTEGRACAO

Acionada por: `trabalhista-master`, `/recurso-trabalhista`. Apoio: `estilo-juridico-trabalhista`, `jurisprudencia-trabalhista` (Temas STF), `pareceres-viabilidade-recursal`. Entrega para: `suprema-corte-trabalhista` (R1-R4) — a R2 confere o prazo de 15 dias e a R3 a repercussao geral e o prequestionamento.
