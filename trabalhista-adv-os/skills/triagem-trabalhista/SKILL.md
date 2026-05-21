---
name: triagem-trabalhista
description: >
  TRIAGEM TRABALHISTA — Skill Tier 1, porta de entrada de todo caso. Diagnostica a fase processual e o tipo de tarefa e PERGUNTA se o cliente do escritorio e o reclamante (trabalhador que ajuiza) ou a reclamada (empresa/tomador que se defende). Grava o polo no CASO.md. Abre ou retoma a pasta do caso. Use no inicio de qualquer demanda trabalhista, caso novo, ou quando o usuario diz triagem, analisar caso trabalhista.
---

# TRIAGEM TRABALHISTA

> Skill **Tier 1** — Estado-Maior. Porta de entrada operacional de todo caso. Diagnostica a fase, identifica o polo do cliente, abre/retoma o caso e dispara o pipeline. Acionada logo apos a `trabalhista-master`.

---

## 0. ESCOPO E ACIONAMENTO

Primeira skill a rodar em qualquer demanda trabalhista. Acionada pela `trabalhista-master` ou pelo `/caso-trabalhista`. Encerra no **Checkpoint 1** do pipeline.

## 1. POSICAO NA ORQUESTRA

```
trabalhista-master  ->  TRIAGEM-TRABALHISTA  ->  CHECKPOINT 1
                                              ->  auditoria-documental + cct-normas-coletivas
```

A triagem entrega: polo do cliente confirmado, partes, fase processual, tipo de tarefa, e o `CASO.md` aberto. Sem isso, nenhuma skill de produção avança.

---

## 2. A PERGUNTA NUCLEAR — POLO DO CLIENTE

**Antes de qualquer diagnostico**, pergunte:

> "Para conduzir o caso corretamente, preciso saber qual e o lado do seu cliente nesta Reclamacao Trabalhista:
> 1. **Reclamante** — voce atua pelo **trabalhador**, que ajuiza (ou vai ajuizar) a acao contra a empresa.
> 2. **Reclamada** — voce atua pela **empresa ou tomador de servicos**, que se defende da acao.
>
> Qual e o polo do seu cliente?"

A resposta e gravada no `CASO.md` no campo `Polo do cliente`. **Esta e a variavel-mae do plugin** — orienta toda tese, estrategia, pedido e tom. Produzir contra o polo do cliente e PA-05. Se o operador nao souber ainda (ex: consulta pre-contratual), registrar `polo: a definir` e tratar a tarefa como consultiva ate a definicao.

---

## 3. DIAGNOSTICO DA FASE PROCESSUAL

Identificar em que ponto do processo o caso esta:

| Fase | Sinais | Tarefa tipica |
|------|--------|---------------|
| Pre-processual | ainda nao ha acao; consulta, notificacao | parecer, documento extrajudicial, contrato preventivo |
| Conhecimento 1o grau | RT ajuizada / a ajuizar; audiencia marcada | peticao inicial (RC) ou contestacao (RD); replica; razoes finais |
| Recursal | ha sentenca ou acordao | RO, RR, AIRR, ED, agravos, RE; ou contrarrazoes |
| Liquidacao | sentenca transitada, apurando valores | calculo de liquidacao, impugnacao a calculos |
| Execucao | titulo liquido, cobranca | embargos a execucao, agravo de peticao, defesa do executado |

## 4. DIAGNOSTICO DO TIPO DE TAREFA

Classificar a demanda: peca de conhecimento, peca recursal, peca de instrucao/execucao, parecer, calculo, documento extrajudicial, ou analise/consultoria. Isso define qual Tenente Tier 2 sera acionado.

## 5. EXTRACAO DOS DADOS DO CASO

Colher e registrar no `CASO.md`:
- **Partes:** cliente (parte atendida) e parte adversa.
- **Processo:** numero CNJ, vara/TRT, data de audiencia (se houver — e a deadline real).
- **Contrato de trabalho:** admissao, rescisao (ou contrato vigente), funcao, ultima remuneracao, jornada contratual, modalidade de rescisao.
- **Categoria / sindicato:** para identificar a CCT/ACT aplicavel.
- **Marco intertemporal:** contrato anterior, posterior ou "a cavalo" de 11/11/2017 (Reforma — Protocolo 6).

## 6. ALERTAS DA TRIAGEM

A triagem ja sinaliza pontos que orientarao as fases seguintes:

- **Competencia territorial** (art. 651 CLT) — a competencia e, em regra, do local da prestacao de servico. Se houver discrepancia com a vara onde a RT foi ajuizada, sinalizar possivel arguicao de incompetencia (relativa — precisa ser arguida na contestacao).
- **Prescricao** — calcular de imediato a bienal (art. 7o XXIX CF) e a quinquenal (art. 11 CLT). Sinalizar se ha pedido ja prescrito.
- **Rito** — ordinario, sumarissimo (ate 40 salarios minimos — liquidacao obrigatoria dos pedidos, art. 852-B CLT) ou sumario.
- **Multi-reclamada / grupo economico** — se ha mais de uma reclamada ou alegacao de grupo (art. 2o §2o CLT).
- **Tutela de urgencia / gratuidade** — pedidos que disparam resposta processual ou argumentacao especifica.
- **Prazo recursal** (se fase recursal) — cravar conforme o Protocolo 7 (8 dias / ED 5 dias / RE 15 dias).

## 7. ABERTURA OU RETOMADA DO CASO

- **Caso novo:** acionar `memoria-de-caso-trabalhista` para criar a pasta `casos/<cliente>-x-<adverso>/` com `CASO.md` e `MEMORY.md`.
- **Caso existente:** localizar a pasta, ler o `CASO.md` e o `MEMORY.md`, retomar de onde parou.

---

## 8. CHECKPOINT 1

Ao final, apresentar ao advogado:

```
TRIAGEM CONCLUIDA — CHECKPOINT 1

Polo do cliente: <reclamante | reclamada>
Cliente: <X>   |   Parte adversa: <Y>
Fase processual: <fase>
Tipo de tarefa: <tarefa>
Vara/TRT: <orgao>   |   Audiencia: <data ou n/a>
Marco intertemporal: <pre | pos | a cavalo de 11/11/2017>
Alertas: <competencia, prescricao, rito, grupo economico, prazo>

Confirma estes dados para eu avancar para a auditoria documental?
```

No modo `--continuo`, registrar e seguir sem parar.

---

## 9. VEDACOES ESPECIFICAS

- **PA-05** — nunca prosseguir sem o polo definido (ou explicitamente "a definir").
- **PA-04** — nao inventar dados do contrato; o que faltar, perguntar.
- **PA-09** — sempre calcular a prescricao na triagem.
- **PA-22** — cada caso em sua propria pasta; nao misturar.

## 10. INTEGRACAO

Acionada por: `trabalhista-master`. Aciona: `memoria-de-caso-trabalhista` (abrir/retomar). Entrega para: `auditoria-documental-trabalhista` + `cct-normas-coletivas` (fase seguinte do pipeline).
