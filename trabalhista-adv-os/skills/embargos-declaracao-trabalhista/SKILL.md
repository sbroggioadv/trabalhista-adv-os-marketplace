---
name: embargos-declaracao-trabalhista
description: >
  EMBARGOS DE DECLARACAO TRABALHISTA — Skill Tier 2 recursal transversal. Produz os Embargos de Declaracao contra sentenca e acordao (omissao, contradicao, obscuridade, erro material, prequestionamento) e as contrarrazoes aos ED com efeitos infringentes. Prazo: 5 dias uteis (art. 897-A CLT). Use quando menciona embargos de declaracao, ED, omissao na sentenca, prequestionar.
---

# EMBARGOS DE DECLARACAO TRABALHISTA

> Skill **Tier 2** recursal, transversal, **modo dual**. Produz os Embargos de Declaracao (ED) — contra sentenca e contra acordao — e as contrarrazoes. **Prazo de 5 dias**, distinto dos demais recursos.

---

## 0. ESCOPO E ACIONAMENTO

Acionada quando ha sentenca ou acordao com vicio de omissao, contradicao, obscuridade ou erro material, ou quando se precisa prequestionar materia para recurso futuro.

## 1. MODO DUAL — DOIS EIXOS

Side-aware, lido do `CASO.md`:
- **Polo:** reclamante ou reclamada.
- **Posicao:**
  - **embargante** — o cliente embarga -> produz os ED.
  - **embargado** — a outra parte embargou -> produz as **contrarrazoes aos ED** (com atencao especial quando os ED da outra parte buscam **efeitos infringentes**).

A peca serve ao polo do cliente (PA-05).

## 2. PRAZO (Protocolo 7) — ATENCAO: 5 DIAS

**Embargos de Declaracao e contrarrazoes aos ED: 5 dias uteis** (art. 897-A CLT; dias uteis — art. 775 CLT). Termo inicial: intimacao da decisao embargada. **Este e o unico recurso trabalhista de 5 dias** — nao confundir com os 8 dias dos demais nem com os 15 do CPC (PA-08).

## 3. HIPOTESES DE CABIMENTO (art. 897-A CLT c/c art. 1.022 CPC)

| Vicio | O que e |
|-------|---------|
| **Omissao** | a decisao deixou de apreciar ponto/pedido sobre o qual deveria pronunciar-se |
| **Contradicao** | proposicoes inconciliaveis dentro da propria decisao |
| **Obscuridade** | falta de clareza que impede a compreensao |
| **Erro material** | equivoco evidente (calculo, nome, data) — corrigivel de oficio |
| **Manifesto equivoco no exame dos pressupostos extrinsecos do recurso** | hipotese propria do art. 897-A CLT |

## 3.1. PREQUESTIONAMENTO VIA ED — ESTRATEGIA OBRIGATORIA PRE-RR

O prequestionamento e **pressuposto de admissibilidade** do Recurso de Revista e do Recurso Extraordinario: o Tribunal so revisa materia sobre a qual a decisao recorrida **expressamente se pronunciou** (Sumula 297 do TST). Sempre que a decisao do TRT for **omissa** quanto a tese, dispositivo de lei ou questao constitucional que o cliente pretende levar ao TST/STF, **opor ED de prequestionamento e regra, nao opcao** — sem eles, o RR/RE futuro nao e conhecido por ausencia de prequestionamento.

**Procedimento operacional:**

1. Antes de redigir o RR/RE, mapear cada tese e cada dispositivo (de lei federal ou da CF) que fundamentara o recurso.
2. Conferir, ponto a ponto, se o acordao do TRT se pronunciou expressamente sobre cada um.
3. Para todo ponto **nao enfrentado**, opor ED de prequestionamento — apontando a omissao especifica e indicando o dispositivo cuja aplicacao se quer ver examinada.
4. Considera-se prequestionada a materia ainda que a decisao dos ED rejeite a tese, desde que adote tese explicita a respeito (Sumula 297, II e III, do TST `[VERIFICAR]`).
5. So apos esgotado o prequestionamento, redigir o RR/RE.

**Sinalizar ao operador:** quando a skill recursal (RR/RE) for acionada sobre acordao com pontos nao prequestionados, devolver alerta recomendando ED de prequestionamento antes — evitar a perda do recurso por vicio sanavel.

Os ED tambem servem, fora da estrategia recursal, para **integrar** decisao viciada — provocar o juizo a manifestar-se sobre ponto omitido.

## 4. EFEITOS

- Efeito **integrativo** (regra) — completam a decisao.
- **Efeito interruptivo** — os ED interrompem o prazo para outros recursos (art. 897-A §3o CLT); apos o julgamento dos ED, o prazo do recurso cabivel recomeca integralmente.
- **Efeito modificativo (infringente)** — excepcional: quando o saneamento do vicio altera o resultado. Exige contraditorio previo (intimacao da parte contraria — Sumula 278 TST e art. 1.023 §2o CPC).

## 5. MODO EMBARGANTE — EMBARGOS DE DECLARACAO

```
1. ENDERECAMENTO       — ao mesmo juizo que proferiu a decisao
2. TEMPESTIVIDADE      — 5 dias uteis (art. 897-A CLT)
3. DO VICIO            — apontar com precisao: qual vicio, em que ponto da decisao
4. DO PREQUESTIONAMENTO — quando o objetivo e viabilizar recurso futuro
5. DO PEDIDO           — sanar o vicio (e, se for o caso, atribuir efeito modificativo)
```

ED nao e instrumento de mero inconformismo — embargos protelatorios sujeitam a parte a multa (art. 1.026 §2o CPC).

## 6. MODO EMBARGADO — CONTRARRAZOES AOS ED

- Sustentar a **inexistencia do vicio** apontado — a decisao nao e omissa/contraditoria/obscura.
- Quando os ED adversos buscam **efeitos infringentes**, rebater a pretensao de rejulgamento sob o disfarce de ED; sustentar que a via correta seria o recurso proprio.
- Pedir a rejeicao dos ED e, se protelatorios, a multa.

## 7. VEDACOES ESPECIFICAS

- **PA-08** — ED e **5 dias uteis** (art. 897-A CLT); nunca 8, nunca 15.
- **PA-05** — a peca serve ao polo do cliente nos dois modos.
- Nunca usar ED como sucedaneo de recurso (mero inconformismo) — risco de multa.
- Efeito modificativo exige contraditorio previo.

## 8. INTEGRACAO

Acionada por: `trabalhista-master`, `/recurso-trabalhista`. Apoio: `estilo-juridico-trabalhista`. Frequentemente antecede `recurso-ordinario-trabalhista` ou `recurso-revista-trabalhista` (prequestionamento). Entrega para: `suprema-corte-trabalhista` (R1-R4) — a R2 confere o prazo de 5 dias (PA-08).
