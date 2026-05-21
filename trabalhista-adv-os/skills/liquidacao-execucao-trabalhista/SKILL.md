---
name: liquidacao-execucao-trabalhista
description: >
  LIQUIDACAO E EXECUCAO TRABALHISTA — Skill Tier 2 transversal. Atua na fase de liquidacao e execucao: liquidacao de sentenca, impugnacao aos calculos de liquidacao, embargos a execucao, defesa do executado. Use quando menciona liquidacao de sentenca, impugnacao aos calculos, embargos a execucao, fase de execucao trabalhista, penhora.
---

# LIQUIDACAO E EXECUCAO TRABALHISTA

> Skill **Tier 2** de execucao, transversal. Atua na fase posterior a sentenca de merito: liquidacao, impugnacao a calculos, embargos a execucao, defesa do executado. Serve aos dois polos.

---

## 0. ESCOPO E ACIONAMENTO

Acionada quando o caso esta na fase de liquidacao (apurar o quantum) ou de execucao (cobrar o titulo). Tambem pelo operador que pede "liquidacao", "impugnacao aos calculos", "embargos a execucao".

## 1. SIDE-AWARENESS

Leia o `Polo do cliente` no `CASO.md`:
- Cliente = **reclamante (exequente)** -> apresentar/defender a conta de liquidacao a maior; promover a execucao.
- Cliente = **reclamada (executada)** -> impugnar a conta a maior; opor embargos a execucao; defender-se da constricao.

A peca serve ao polo do cliente (PA-05).

## 2. FASE DE LIQUIDACAO

Liquidacao = apurar o valor do que a sentenca reconheceu. Modalidades (art. 879 CLT):
- **Por calculos** — a regra; aplica-se a memoria de calculo aos parametros da sentenca.
- **Por arbitramento** — quando depende de avaliacao tecnica.
- **Por artigos** — quando ha fato novo a provar.

Apos a apresentacao da conta, o juizo abre prazo comum de **8 dias** para as partes se manifestarem (art. 879 §2o CLT) — momento da impugnacao.

## 3. IMPUGNACAO AOS CALCULOS DE LIQUIDACAO

Conferir a conta contra a sentenca:
- os parametros da conta correspondem ao que a sentenca determinou (nem mais, nem menos)?
- a base de calculo, os indices, os juros e a correcao estao corretos? Conferir a metodologia: ADC 58/59 do STF e, para o periodo posterior a sua vigencia, a **Lei 14.905/2024** `[VERIFICAR]` (nova redacao dos arts. 389 e 406 do Codigo Civil — correcao por IPCA e juros pela Selic deduzido o IPCA). A norma complementa as ADC 58/59; confirmar a regra em vigor no momento da conta.
- ha verba incluida que a sentenca nao reconheceu, ou excluida que reconheceu?
- os reflexos e a contribuicao previdenciaria/IR estao calculados corretamente?

A impugnacao aponta, item a item, o erro e apresenta a conta correta. Apoio da `calculos-trabalhistas`.

## 4. EMBARGOS A EXECUCAO

Garantido o juizo (penhora, deposito), o executado pode opor **embargos a execucao** (art. 884 CLT), no prazo de **5 dias**. Materia: cumprimento da decisao, quitacao, prescricao da execucao, e os vicios da propria execucao. Os embargos sao a defesa de merito do executado na fase de execucao.

> O **agravo de peticao** (8 dias) e o recurso contra a decisao que julga os embargos a execucao ou a impugnacao a liquidacao — produzido pela skill `agravos-trabalhistas`.

## 5. ATOS DE CONSTRICAO

Na execucao, orientar quanto a penhora (inclusive penhora online — SISBAJUD), avaliacao, e as defesas cabiveis contra constricao indevida (impenhorabilidade, excesso de penhora). A defesa do executado e tecnica e tempestiva.

## 6. PRESCRICAO INTERCORRENTE

A Reforma 13.467/2017 introduziu a **prescricao intercorrente** na execucao trabalhista (art. 11-A CLT) — 2 anos de inercia do exequente. Atencao ao marco intertemporal (Protocolo 6): aplica-se a execucoes conforme o entendimento sobre o termo inicial.

## 7. VEDACOES ESPECIFICAS

- **PA-05** — a peca serve ao polo do cliente (exequente ou executado).
- **PA-20** — toda conta de liquidacao com dado-base; sem ele, sinalizar.
- **PA-08** — embargos a execucao 5 dias; agravo de peticao 8 dias — nao confundir.
- **PA-07** — prescricao intercorrente: respeitar o marco intertemporal.
- **PA-09** — verificar a prescricao da pretensao executiva.

## 8. INTEGRACAO

Acionada por: `trabalhista-master`. Apoio: `calculos-trabalhistas` (a conta), `estilo-juridico-trabalhista`. Aciona: `agravos-trabalhistas` (agravo de peticao contra a decisao da execucao). Entrega para: `suprema-corte-trabalhista` (R1-R4).
