---
name: acoes-autonomas-impugnacao-trabalhista
description: >
  ACOES AUTONOMAS DE IMPUGNACAO TRABALHISTA — Skill Tier 2 transversal. Produz os meios autonomos de impugnacao de decisoes trabalhistas: Mandado de Seguranca contra ato judicial, Acao Rescisoria, Correicao Parcial e Reclamacao, alem da defesa/resposta quando o cliente e o requerido. Use quando menciona mandado de seguranca contra liminar trabalhista, acao rescisoria trabalhista, correicao parcial, reclamacao ao TST.
---

# ACOES AUTONOMAS DE IMPUGNACAO TRABALHISTA

> Skill **Tier 2** transversal, **modo dual**. Produz os meios **autonomos** de impugnacao de decisoes — nao sao recursos, sao acoes/medidas proprias — e as respectivas defesas/respostas.

---

## 0. ESCOPO E ACIONAMENTO

Acionada quando a impugnacao a uma decisao trabalhista nao se faz por recurso, mas por uma acao autonoma: Mandado de Seguranca, Acao Rescisoria, Correicao Parcial ou Reclamacao.

## 1. MODO DUAL — DOIS EIXOS

Side-aware, lido do `CASO.md`:
- **Polo:** reclamante ou reclamada.
- **Posicao:**
  - **impetrante / autor / requerente** — o cliente prope a acao autonoma.
  - **requerido / litisconsorte / autoridade interessada** — o cliente responde/defende-se da acao autonoma proposta pela outra parte.

A peca serve ao polo do cliente (PA-05).

## 2. MANDADO DE SEGURANCA CONTRA ATO JUDICIAL

Cabivel contra **ato judicial** ilegal ou abusivo, quando nao haja recurso proprio com efeito suspensivo (Sumula 414 TST). Uso tipico: atacar liminar/tutela de urgencia, ato de penhora abusivo, decisao interlocutoria irrecorrivel de imediato.

```
1. ENDERECAMENTO       — ao TRT (ou TST), conforme a autoridade coatora
2. PARTES              — impetrante; autoridade coatora (o juiz); litisconsorte passivo (a parte beneficiada pelo ato)
3. DO ATO COATOR       — descricao do ato ilegal/abusivo
4. DO DIREITO LIQUIDO E CERTO — prova pre-constituida, documental
5. DA LIMINAR          — fundamento + perigo da demora
6. DO PEDIDO           — concessao da seguranca
```

Pressupostos: direito liquido e certo (prova documental pre-constituida), ato de autoridade, ilegalidade/abuso. Prazo decadencial de 120 dias (art. 23 Lei 12.016/2009).

## 3. ACAO RESCISORIA

Acao autonoma para **desconstituir decisao de merito transitada em julgado**, nas hipoteses do art. 966 CPC (aplicavel ao processo do trabalho — Sumula 100 TST trata do prazo). Hipoteses tipicas: violacao manifesta de norma juridica, prova falsa, documento novo, erro de fato.

- **Prazo decadencial: 2 anos** do transito em julgado (art. 975 CPC; Sumula 100 TST detalha a contagem).
- Competencia: TRT ou TST, conforme o orgao que proferiu a decisao rescindenda.
- Pode exigir deposito previo (art. 968 II CPC).

## 4. CORREICAO PARCIAL

Medida administrativo-processual contra **erro de procedimento (error in procedendo)** do juiz que cause tumulto processual e inversao tumultuaria dos atos, quando nao haja recurso proprio. Dirigida a Corregedoria do TRT (ou do TST). Prazo conforme o regimento do Tribunal (em regra, 5 dias).

## 5. RECLAMACAO

Cabivel para **preservar a competencia** do tribunal ou **garantir a autoridade de suas decisoes** — inclusive de tese vinculante (sumula vinculante do STF, decisao em controle concentrado, tese de repercussao geral, IRDR). Dirigida ao tribunal cuja autoridade/competencia se busca resguardar (STF, TST).

## 6. MODO REQUERIDO — DEFESA / RESPOSTA

Quando o cliente e o requerido:
- **MS** — a parte beneficiada pelo ato presta informacoes como litisconsorte; sustentar a legalidade do ato e a ausencia de direito liquido e certo.
- **Acao Rescisoria** — contestar: inexistencia da hipotese rescisoria, decadencia do biénio, pressupostos.
- **Correicao / Reclamacao** — sustentar o acerto do procedimento ou a inexistencia de usurpacao/descumprimento.

## 7. VEDACOES ESPECIFICAS

- **PA-05** — a peca serve ao polo do cliente nos dois modos.
- **PA-09** — observar os prazos decadenciais (MS 120 dias; Rescisoria 2 anos).
- **PA-01/PA-11** — Sumulas (414, 100 TST) e dispositivos classificados e existentes.
- Nao usar acao autonoma como sucedaneo de recurso cabivel — cada via tem seu pressuposto.

## 8. INTEGRACAO

Acionada por: `trabalhista-master`, `/recurso-trabalhista`. Apoio: `estilo-juridico-trabalhista`, `jurisprudencia-trabalhista`. Entrega para: `suprema-corte-trabalhista` (R1-R4) — a R2 confere prazo decadencial e cabimento.
