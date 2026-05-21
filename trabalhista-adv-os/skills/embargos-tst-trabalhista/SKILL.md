---
name: embargos-tst-trabalhista
description: >
  EMBARGOS NO TST — Skill Tier 2 recursal transversal. Produz os Embargos a SDI-1 (art. 894 CLT, divergencia entre Turmas do TST), os Embargos infringentes da SDC (dissidio coletivo) e a impugnacao/contrarrazoes aos embargos. Prazo: 8 dias uteis. Use quando menciona embargos no TST, embargos a SDI, embargos de divergencia, embargos infringentes.
---

# EMBARGOS NO TST

> Skill **Tier 2** recursal, transversal, **modo dual**. Produz os Embargos no ambito do TST — Embargos a SDI-1 e Embargos infringentes da SDC — e as respectivas contrarrazoes. Recurso interno do TST, de cabimento estrito.

---

## 0. ESCOPO E ACIONAMENTO

Acionada quando ha acordao de Turma do TST (cabe Embargos a SDI-1) ou acordao nao unanime da SDC em dissidio coletivo (cabe Embargos infringentes), a impugnar ou a defender.

## 1. MODO DUAL — DOIS EIXOS

Side-aware, lido do `CASO.md`:
- **Polo:** reclamante ou reclamada.
- **Posicao:**
  - **embargante** — o cliente embarga -> produz os Embargos.
  - **embargado** — a outra parte embargou -> produz as **contrarrazoes/impugnacao aos embargos**.

A peca serve ao polo do cliente (PA-05).

## 2. PRAZO (Protocolo 7)

**Embargos no TST e contrarrazoes: 8 dias uteis** (art. 894 CLT; dias uteis — art. 775 CLT). Termo inicial: intimacao do acordao embargado. Nunca 15 dias (PA-08).

## 3. EMBARGOS A SDI-1 (art. 894 II CLT)

Cabem contra **acordao de Turma do TST** que, em Recurso de Revista, divergir:
- de outra Turma do TST; ou
- da propria SDI (Sumula ou OJ); ou
- de Sumula do STF ou de tese de repercussao geral.

```
1. ENDERECAMENTO       — a SDI-1 do TST
2. TEMPESTIVIDADE      — 8 dias uteis
3. DA DIVERGENCIA      — cotejo analitico: acordao da Turma x paradigma (Sumula 337 TST)
4. DAS RAZOES          — demonstrar a tese correta a ser uniformizada
5. DO PEDIDO           — conhecimento e provimento; prevalencia da tese embargada
```

Os Embargos a SDI-1 sao recurso de **uniformizacao** — exigem divergencia atual e especifica; nao reabrem o reexame de fatos e provas (Sumula 126 TST).

## 4. EMBARGOS INFRINGENTES DA SDC (art. 894 I CLT)

Cabem contra **decisao nao unanime** da SDC (Secao de Dissidios Coletivos) proferida em processo de dissidio coletivo de competencia originaria — limitados a materia objeto da divergencia. Atacam o(s) ponto(s) em que houve voto vencido.

> Escopo: o plugin cobre apenas a **faceta recursal** do dissidio coletivo. A redacao de instrumento de negociacao coletiva esta fora de escopo (spec §11).

## 5. MODO EMBARGADO — CONTRARRAZOES / IMPUGNACAO

Sustentar:
- a **ausencia de divergencia** atual e especifica (Embargos a SDI-1) — ou que o paradigma e inservivel;
- ou a **unanimidade** / o nao cabimento (Embargos infringentes);
- subsidiariamente, o acerto do acordao embargado.

## 6. PONTOS DE ATENCAO

- **Divergencia atual** — paradigma superado nao serve (Sumula 333 TST).
- **Sumula 126 TST** — Embargos nao reexaminam fato e prova.
- **Prequestionamento** — a tese deve ter sido enfrentada no acordao da Turma.

## 7. VEDACOES ESPECIFICAS

- **PA-08** — Embargos e 8 dias uteis; nunca 15.
- **PA-05** — a peca serve ao polo do cliente nos dois modos.
- **PA-01/PA-11** — paradigma de divergencia real, atual e existente.
- Nunca usar os Embargos para rediscutir fato e prova (Sumula 126 TST).

## 8. INTEGRACAO

Acionada por: `trabalhista-master`, `/recurso-trabalhista`. Apoio: `estilo-juridico-trabalhista`, `jurisprudencia-trabalhista`, `pareceres-viabilidade-recursal`. Entrega para: `suprema-corte-trabalhista` (R1-R4) — a R2 confere prazo e cabimento.
