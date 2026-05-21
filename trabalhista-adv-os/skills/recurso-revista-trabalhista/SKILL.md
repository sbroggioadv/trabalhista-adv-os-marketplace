---
name: recurso-revista-trabalhista
description: >
  RECURSO DE REVISTA TRABALHISTA — Skill Tier 2 recursal transversal. Produz o Recurso de Revista ao TST (transcendencia, divergencia/violacao), o Agravo de Instrumento em RR (AIRR) para destrancar revista negada, o Recurso Adesivo e as contrarrazoes de RR / contraminuta de AIRR. Prazo: 8 dias uteis. Use quando menciona recurso de revista, RR, AIRR, agravo de instrumento, transcendencia, TST.
---

# RECURSO DE REVISTA TRABALHISTA

> Skill **Tier 2** recursal, transversal, **modo dual**. Produz o Recurso de Revista (RR), o Agravo de Instrumento em RR (AIRR) e as pecas de resposta. O RR e recurso de fundamentacao vinculada — exige enquadramento tecnico estrito.

---

## 0. ESCOPO E ACIONAMENTO

Acionada quando ha acordao de TRT (em RO) a impugnar perante o TST, ou quando a revista foi negada na origem (cabe AIRR), ou para defender o acordao.

## 1. MODO DUAL — DOIS EIXOS

Side-aware em dois eixos, lidos do `CASO.md`:
- **Polo:** reclamante ou reclamada.
- **Posicao no recurso:**
  - **recorrente** — o cliente recorre do acordao -> **Recurso de Revista**.
  - **recorrente com revista trancada** — o RR do cliente foi negado seguimento -> **AIRR** para destrancar.
  - **recorrido** — a outra parte recorreu -> **contrarrazoes de RR** ou **contraminuta de AIRR**.

Ler quem recorreu no `CASO.md` antes de redigir. A peca serve ao polo do cliente (PA-05).

## 2. PRAZO (Protocolo 7)

**RR, AIRR e contrarrazoes/contraminuta: 8 dias uteis** (art. 896 e art. 897 b CLT; dias uteis — art. 775 CLT). Termo inicial: intimacao do acordao do TRT (RR) ou da decisao denegatoria (AIRR). Nunca 15 dias (PA-08). Reclamada recolhe deposito recursal.

## 3. PRESSUPOSTOS DE CABIMENTO DO RR (fundamentacao vinculada)

O RR (art. 896 CLT) so cabe por:
- **Divergencia jurisprudencial** — interpretacao diversa entre TRTs, ou entre TRT e SDI/Sumula do TST. A divergencia exige cotejo analitico (Sumula 337 TST).
- **Violacao de lei federal ou da Constituicao** — violacao direta e literal de dispositivo.

E indispensavel o **prequestionamento** (Sumula 297 TST): a materia tem de ter sido enfrentada no acordao recorrido.

## 4. TRANSCENDENCIA (art. 896-A CLT)

Todo RR deve demonstrar a **transcendencia** — relevância economica, politica, social ou juridica da questao. Sem transcendencia, o RR nao e conhecido. A peca dedica um topico a demonstrar o(s) indicador(es) de transcendencia da causa.

## 5. MODO RECORRENTE — RECURSO DE REVISTA

```
1. ENDERECAMENTO       — ao TRT (juizo de admissibilidade), dirigido ao TST
2. TEMPESTIVIDADE E PREPARO — 8 dias uteis; deposito recursal
3. DA TRANSCENDENCIA   — topico proprio (art. 896-A CLT)
4. DO PREQUESTIONAMENTO — demonstrar que o acordao enfrentou a materia
5. DAS RAZOES — por pressuposto:
   - divergencia: cotejo analitico (acordao recorrido x paradigma; Sumula 337 TST)
   - violacao: indicar o dispositivo violado e a violacao direta
6. DOS PEDIDOS         — conhecimento e provimento; reforma do acordao
```

## 6. MODO AIRR — DESTRANCAR REVISTA NEGADA

Negado seguimento ao RR na origem, cabe **AIRR** (art. 897 b CLT) ao TST, no prazo de 8 dias, para que o TST reexamine a admissibilidade. O AIRR ataca os fundamentos da decisao denegatoria, demonstrando que os pressupostos do RR estavam presentes.

## 7. MODO RECORRIDO — CONTRARRAZOES / CONTRAMINUTA

- **Contrarrazoes de RR** — sustentar a ausencia de transcendencia, de prequestionamento, ou de divergencia/violacao; subsidiariamente, defender o merito do acordao.
- **Contraminuta de AIRR** — sustentar o acerto da decisao que negou seguimento ao RR.

## 8. VEDACOES ESPECIFICAS

- **PA-08** — RR/AIRR e 8 dias uteis; nunca 15.
- **PA-05** — a peca serve ao polo do cliente nos dois eixos.
- **PA-01/PA-11** — paradigma de divergencia real e existente; dispositivo de violacao existente.
- Nunca omitir a transcendencia (no modo recorrente) — sem ela o RR nao e conhecido.

## 9. INTEGRACAO

Acionada por: `trabalhista-master`, `/recurso-trabalhista`. Apoio: `estilo-juridico-trabalhista`, `jurisprudencia-trabalhista`, `pareceres-viabilidade-recursal` (avalia cabimento e transcendencia antes). Entrega para: `suprema-corte-trabalhista` (R1-R4) — a R2 confere prazo e a R3 confere transcendencia/prequestionamento.
