---
name: agravos-trabalhistas
description: >
  AGRAVOS TRABALHISTAS — Skill Tier 2 recursal transversal. Produz o Agravo de Peticao (impugna decisao na execucao), o Agravo Regimental/Interno (contra decisao monocratica), o Pedido de Revisao do valor de alcada e a contraminuta de agravo. Prazos: 8 dias / 48h. Use quando menciona agravo de peticao, agravo regimental, agravo interno, contraminuta de agravo, recorrer na execucao.
---

# AGRAVOS TRABALHISTAS

> Skill **Tier 2** recursal, transversal, **modo dual**. Produz os agravos do processo do trabalho — Agravo de Peticao, Agravo Regimental/Interno, Pedido de Revisao de alcada — e as contraminutas.

---

## 0. ESCOPO E ACIONAMENTO

Acionada na fase de execucao (Agravo de Peticao), contra decisao monocratica de relator (Agravo Regimental/Interno), ou para revisar o valor de alcada arbitrado.

## 1. MODO DUAL — DOIS EIXOS

Side-aware, lido do `CASO.md`:
- **Polo:** reclamante ou reclamada.
- **Posicao:**
  - **agravante** — o cliente recorre -> produz o agravo.
  - **agravado** — a outra parte recorreu -> produz a **contraminuta de agravo**.

A peca serve ao polo do cliente (PA-05).

## 2. PRAZOS (Protocolo 7)

| Peca | Prazo |
|------|-------|
| Agravo de Peticao | **8 dias uteis** (art. 897 a CLT) |
| Agravo Regimental / Interno | **8 dias uteis** (regimentos dos tribunais; art. 1.021 CPC subsid.) |
| Contraminuta de agravo | **8 dias uteis** |
| Pedido de Revisao do valor de alcada | **48 horas** (art. 2o §1o Lei 5.584/1970) |

Contagem em dias uteis (art. 775 CLT) para os recursos de 8 dias. Nunca 15 dias (PA-08).

## 3. AGRAVO DE PETICAO (art. 897 "a" CLT)

Recurso cabivel na **fase de execucao**, contra decisoes do juizo da execucao (ex.: decisao em embargos a execucao, em impugnacao a sentenca de liquidacao, sentenca que julga a liquidacao).

```
1. ENDERECAMENTO       — ao juizo da execucao, dirigido ao TRT
2. TEMPESTIVIDADE      — 8 dias uteis
3. DELIMITACAO DE VALORES E MATERIAS — art. 897 §1o CLT: o agravo de peticao
   so e recebido se delimitar, justificadamente, as materias e os valores
   impugnados, permitindo a execucao imediata da parte incontroversa
4. DAS RAZOES          — bloco FIRAC por materia impugnada (calculo, penhora, etc.)
5. DOS PEDIDOS         — reforma da decisao da execucao
```

A **delimitacao de valores e materias** (art. 897 §1o CLT) e pressuposto especifico — sem ela o agravo de peticao nao e conhecido.

## 4. AGRAVO REGIMENTAL / INTERNO

Cabivel contra **decisao monocratica** de relator (que nega seguimento a recurso, indefere liminar, etc.), para levar a materia ao colegiado. Ataca os fundamentos da decisao monocratica. Prazo de 8 dias uteis.

## 5. PEDIDO DE REVISAO DO VALOR DE ALCADA

Quando o valor da causa e arbitrado de forma divergente da realidade economica, cabe Pedido de Revisao ao TRT (art. 2o §1o Lei 5.584/1970), em **48 horas**. Relevante porque o valor de alcada define o cabimento de recurso no rito de menor valor.

## 6. MODO AGRAVADO — CONTRAMINUTA

Sustentar o nao conhecimento (vicio formal, ausencia de delimitacao no agravo de peticao) ou o desprovimento, defendendo a decisao agravada no que ela favorece o cliente.

## 7. VEDACOES ESPECIFICAS

- **PA-08** — agravos de 8 dias uteis; revisao de alcada 48h; nunca 15 dias.
- **PA-05** — a peca serve ao polo do cliente nos dois modos.
- **PA-20** — no agravo de peticao sobre calculo, nenhum valor sem dado-base.
- Nunca interpor agravo de peticao sem a delimitacao do art. 897 §1o CLT.

## 8. INTEGRACAO

Acionada por: `trabalhista-master`, `/recurso-trabalhista`. Apoio: `estilo-juridico-trabalhista`, `liquidacao-execucao-trabalhista` (agravo de peticao sobre calculos), `calculos-trabalhistas`. Entrega para: `suprema-corte-trabalhista` (R1-R4).
