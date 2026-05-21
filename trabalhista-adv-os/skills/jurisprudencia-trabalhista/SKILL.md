---
name: jurisprudencia-trabalhista
description: >
  JURISPRUDENCIA TRABALHISTA — Skill Tier 1. Localiza, classifica e prioriza precedentes trabalhistas. Busca viva via WebSearch/WebFetch/firecrawl nos portais do TST, TRTs e JusBrasil; classifica em 3 niveis (validada/indicativa/impossibilidade); nunca alucina. Conhece Sumulas do TST, OJs da SDI-1/SDI-2 e Precedentes Normativos. Use quando precisar de jurisprudencia, sumula, precedente, OJ, entendimento do TST/TRT.
---

# JURISPRUDENCIA TRABALHISTA

> Skill **Tier 1** — Estado-Maior. Localiza precedentes trabalhistas por **busca viva**, classifica em 3 niveis e prioriza por hierarquia. Nunca alucina (PA-01). Roda em paralelo com a `analise-trilateral-trabalhista`.

---

## 0. ESCOPO E ACIONAMENTO

Acionada sempre que uma tese precisa de respaldo jurisprudencial — pela `trabalhista-master`, pela trilateral, pela linha estrategica ou por um Tenente Tier 2. Tambem pelo `/jurisprudencia-trabalhista`.

## 1. POSICAO NA ORQUESTRA

```
trilateral  +  JURISPRUDENCIA-TRABALHISTA  ->  CHECKPOINT 3  ->  linha-estrategica
```

## 2. OS 3 NIVEIS DE CLASSIFICACAO (Protocolo 1)

| Nivel | Significado | Como citar |
|-------|-------------|------------|
| **Nivel 1 — Validada** | orgao, numero, relator, data e ementa confirmados | citacao plena, sem ressalva |
| **Nivel 2 — Indicativa** | existencia provavel, dados incompletos | citar com tag `[VERIFICAR]` + ressalva expressa |
| **Nivel 3 — Impossibilidade** | nao foi possivel confirmar | declarar a impossibilidade — NUNCA preencher |

Todo precedente entregue carrega o nivel. Inventar Sumula, OJ, Precedente Normativo, numero, relator ou ementa e PA-01.

## 3. HIERARQUIA DAS FONTES

```
STF (repercussao geral — ex.: Tema 1046 sobre negociado x legislado)
  > TST — SDI-1 e SDI-2 (Sumula / OJ / Precedente Normativo da SDC)
  > TST — Turmas
  > TRT da regiao do caso
  > demais TRTs (uso comparativo / persuasivo)
```

Precedente da regiao do caso pesa mais que o de outra regiao.

## 4. ESTRATEGIA DE BUSCA VIVA

Nao ha API publica gratuita de jurisprudencia trabalhista. Estrategia (ver spec §8):

1. **Busca dirigida** — `WebSearch` com queries `site:`-scoped: `jurisprudencia.tst.jus.br`, `trt<N>.jus.br`, numero de Sumula/OJ, ementa-chave.
2. **Extracao** — `WebFetch` nas paginas de resultado para capturar processo, orgao, relator, data, ementa.
3. **Portais JS-pesados / JusBrasil** — `firecrawl` (plugin opt-in; o cliente precisa te-lo instalado). JusBrasil pode exigir login — cobertura parcial assumida.
4. **Deep research** — quando a tese e incomum, varredura ampla antes de concluir.
5. **Fallback offline** — usar o catalogo curado abaixo quando a busca viva nao for possivel.

## 5. CATALOGO CURADO (fallback offline)

Sumulas e entendimentos frequentes — **confirmar vigencia e dados antes de citar como Nivel 1**:

- **Sumula 6 TST** — equiparacao salarial.
- **Sumula 85 TST** — compensacao de jornada e horas extras.
- **Sumula 90 TST** — horas in itinere (atencao a alteracao pela Reforma 13.467/2017).
- **Sumula 212 TST** — onus de provar o termino do contrato.
- **Sumula 244 TST** — estabilidade da gestante.
- **Sumula 291 TST** — supressao de horas extras habituais.
- **Sumula 331 TST** — terceirizacao e responsabilidade subsidiaria.
- **Sumula 338 TST** — registro de jornada; nao juntada de cartao de ponto gera presuncao.
- **Sumula 366 TST** — minutos residuais.
- **Sumula 437 TST** — intervalo intrajornada.
- **Sumula 443 TST** — dispensa discriminatoria (presuncao).
- **STF Tema 1046** — limites da negociacao coletiva (negociado x legislado).
- **STF ADC 58/59** — indices de correcao e juros (IPCA-E + Selic).

> O catalogo e ponto de partida — toda citacao passa pela classificacao em 3 niveis. Sumula citada de memoria sem confirmacao entra, no maximo, como Nivel 2 `[VERIFICAR]`.

## 6. SAIDA

```
JURISPRUDENCIA — <tese>

Nivel 1 (validada): <precedente — orgao, numero, relator, data, ementa-sintese>
Nivel 2 (indicativa) [VERIFICAR]: <precedente provavel, dados a confirmar>
Nivel 3 (impossibilidade): <tese sem precedente localizado — seguir so com lei/doutrina>

Hierarquia/aplicacao: <como cada precedente sustenta a tese do polo do cliente>
```

## 7. VEDACOES ESPECIFICAS

- **PA-01** — nunca inventar precedente, numero, relator, ementa ou data.
- Nunca tratar Sumula como lei (PA-03) — Sumula orienta, lei vincula.
- Nivel 3 e declaracao honesta — preencher Nivel 3 como se fosse Nivel 1 e a violacao mais grave da skill.
- Precedente cancelado ou superado nao se cita como vigente.

## 8. INTEGRACAO

Acionada por: `trabalhista-master`, trilateral, linha estrategica e Tenentes Tier 2. Entrega para: `linha-estrategica-trabalhista` e a peca. A `suprema-corte-trabalhista` (R2) reaudita a classificacao de cada precedente citado.
