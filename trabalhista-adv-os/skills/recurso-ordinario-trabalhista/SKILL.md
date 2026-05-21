---
name: recurso-ordinario-trabalhista
description: >
  RECURSO ORDINARIO TRABALHISTA — Skill Tier 2 recursal transversal. Produz o Recurso Ordinario contra sentenca (e contra acordao originario de TRT), o Recurso Adesivo e as contrarrazoes de RO quando o cliente e o recorrido. Prazo: 8 dias uteis. Use quando o usuario menciona recurso ordinario, RO, recorrer da sentenca trabalhista, contrarrazoes de recurso ordinario.
---

# RECURSO ORDINARIO TRABALHISTA

> Skill **Tier 2** recursal, transversal, **modo dual**. Produz o Recurso Ordinario (RO) — e tambem o Recurso Adesivo e as contrarrazoes — conforme a posicao do cliente. Acionada apos a linha estrategica recursal.

---

## 0. ESCOPO E ACIONAMENTO

Acionada pela `trabalhista-master` ou pelo `/recurso-trabalhista` quando ha sentenca de Vara do Trabalho (ou acordao originario de TRT) a impugnar ou a defender.

## 1. MODO DUAL — DOIS EIXOS DE SIDE-AWARENESS

Esta skill e side-aware em **dois eixos**, lidos do `CASO.md`:

- **Eixo 1 — polo do cliente:** reclamante (`RC`) ou reclamada (`RD`).
- **Eixo 2 — posicao no recurso:**
  - **recorrente** — o cliente recorre da sentenca -> produz o **Recurso Ordinario**.
  - **recorrido** — a outra parte recorreu -> produz as **contrarrazoes de RO**.

Combinacao: o cliente reclamante derrotado em parte recorre (RO); o cliente reclamada vencedora contra-arrazoa o RO do reclamante; e vice-versa. **Antes de redigir, ler quem recorreu** no `CASO.md`. Em ambos os modos, a peca serve ao polo do cliente (PA-05).

## 2. PRAZO (Protocolo 7)

**Recurso Ordinario e contrarrazoes de RO: 8 dias uteis** (art. 895 CLT; contagem em dias uteis — art. 775 CLT). Termo inicial: intimacao da sentenca. **Nunca importar os 15 dias do CPC** (PA-08). A reclamada recorrente recolhe deposito recursal e custas.

## 3. CABIMENTO E EFEITOS

- RO contra **sentenca** de Vara do Trabalho (art. 895 I CLT).
- RO contra **acordao** de TRT em processo de competencia originaria do Regional (art. 895 II CLT).
- Efeito **devolutivo** (regra; art. 899 CLT — recurso recebido no efeito devolutivo). Devolve ao TRT a materia impugnada (tantum devolutum quantum appellatum) e as questoes de ordem publica.
- **Recurso Adesivo** — cabivel quando ambas as partes sucumbiram; a parte que nao recorreu autonomamente pode aderir ao recurso da outra, no prazo das contrarrazoes (Sumula 283 TST).

## 4. MODO RECORRENTE — RECURSO ORDINARIO

```
1. ENDERECAMENTO       — ao juizo de origem, dirigido ao TRT
2. TEMPESTIVIDADE E PREPARO — 8 dias uteis; deposito recursal e custas (se reclamada)
3. SINTESE DA SENTENCA — o que foi decidido e o que se impugna
4. RAZOES DE RECURSO   — bloco FIRAC por capitulo impugnado:
   - error in judicando (erro de julgamento) ou error in procedendo (erro de atividade)
   - fundamento legal + jurisprudencia classificada + prova dos autos
5. DO PREQUESTIONAMENTO — provocar o TRT a se manifestar (prepara RR futuro)
6. DOS PEDIDOS         — reforma/anulacao dos capitulos impugnados
```

## 5. MODO RECORRIDO — CONTRARRAZOES DE RO

```
1. ENDERECAMENTO E REFERENCIA AO RO INTERPOSTO
2. PRELIMINAR DE NAO CONHECIMENTO — quando ha vicio (intempestividade, deserção,
   ausencia de dialeticidade — Sumula 422 TST)
3. NO MERITO — rebater cada razao do RO, capitulo a capitulo, sustentando a sentenca
4. DO PEDIDO           — nao conhecimento ou desprovimento do RO; manutencao da sentenca
```

As contrarrazoes defendem a sentenca no que ela favorece o cliente; podem vir acompanhadas de **Recurso Adesivo** no que a sentenca o prejudicou.

## 6. PONTOS DE ATENCAO

- **Dialeticidade** — o RO deve atacar especificamente os fundamentos da sentenca (Sumula 422 TST); razoes genericas levam ao nao conhecimento.
- **Deposito recursal** — pressuposto objetivo para a reclamada; conferir o valor vigente.
- **Prequestionamento** — sem ele, o futuro RR esbarra (Sumula 297 TST).
- **Intertemporal** — Protocolo 6; nao aplicar a Reforma a fato anterior (PA-07).

## 7. VEDACOES ESPECIFICAS

- **PA-08** — RO e 8 dias uteis; nunca 15.
- **PA-05** — a peca serve ao polo do cliente nos dois modos.
- **PA-01/PA-11** — jurisprudencia classificada; dispositivo existente.
- **PA-17** — atacar a sentenca/o recurso adverso, nunca o juiz nem o advogado.

## 8. INTEGRACAO

Acionada por: `trabalhista-master`, `/recurso-trabalhista`. Apoio: `estilo-juridico-trabalhista`, `jurisprudencia-trabalhista`, `pareceres-viabilidade-recursal` (antes — avalia se vale recorrer). Entrega para: `suprema-corte-trabalhista` (R1-R4) — a R2 confere o prazo de 8 dias (PA-08, PA-24).
