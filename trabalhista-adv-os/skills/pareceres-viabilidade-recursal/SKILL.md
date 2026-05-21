---
name: pareceres-viabilidade-recursal
description: >
  PARECERES DE VIABILIDADE RECURSAL — Skill Tier 2 transversal. Produz o parecer previo que avalia se vale a pena recorrer ou contra-arrazoar: cabimento, pressupostos, prequestionamento, transcendencia, prognostico e custo-beneficio. Use quando o usuario pergunta se vale recorrer, viabilidade do recurso, parecer recursal, chance de exito.
---

# PARECERES DE VIABILIDADE RECURSAL

> Skill **Tier 2** transversal. Produz um **parecer** — nao uma peca processual — que responde a pergunta: vale a pena recorrer (ou contra-arrazoar)? Antecede a decisao de interpor qualquer recurso.

---

## 0. ESCOPO E ACIONAMENTO

Acionada antes da producao de um recurso, quando o operador pergunta "vale recorrer?", "qual a chance de exito?", "viabilidade do recurso". Tambem pelo `/parecer-trabalhista`.

## 1. ESCOPO — PARECER, NAO PECA (PA-06)

A saida e um **parecer consultivo** dirigido ao operador, nunca uma peca processual. Compartimentacao de escopos (Protocolo 5): este artefato analisa e recomenda; nao se enderecra a juizo. Se, ao final, o parecer recomenda recorrer, a peca e produzida pela skill recursal especifica.

## 2. SIDE-AWARENESS — DOIS EIXOS

Lido do `CASO.md`:
- **Polo:** reclamante ou reclamada — o parecer avalia o interesse recursal do polo do cliente.
- **Posicao:** avalia tanto **recorrer** (o cliente sucumbiu e cogita recorrer) quanto **contra-arrazoar** (a outra parte recorreu e o cliente avalia a resposta).

## 3. ESTRUTURA DO PARECER (I-VI)

```
I.   INTRODUCAO        — objeto do parecer, decisao a avaliar
II.  OS FATOS          — sintese do caso e da decisao recorrivel
III. AS QUESTOES       — vale recorrer? qual recurso? ha pressupostos?
IV.  FUNDAMENTACAO     — analise de cada criterio (secao 4)
V.   ANALISE CRITICA   — prognostico, custo-beneficio, riscos
VI.  CONCLUSAO         — recomendacao objetiva (recorrer / nao recorrer / contra-arrazoar)
```

## 4. CRITERIOS DE ANALISE

### 4.1 Cabimento e prazo

Identificar o recurso cabivel contra a decisao e cravar o prazo (Protocolo 7): RO/RR/AIRR/Agravo de Peticao/Embargos SDI = 8 dias uteis; ED = 5 dias uteis; RE/ARE = 15 dias uteis. Verificar a tempestividade — recurso intempestivo nao se interpoe.

### 4.2 Pressupostos recursais

- **Objetivos:** cabimento, tempestividade, preparo (deposito recursal e custas, para a reclamada), regularidade formal, dialeticidade.
- **Subjetivos:** legitimidade e interesse recursal (so recorre quem sucumbiu).

### 4.3 Prequestionamento

Para RR e RE: a materia foi enfrentada na decisao recorrida (Sumula 297 TST; Sumula 282/356 STF)? Se nao, e preciso opor ED de prequestionamento antes — o parecer sinaliza.

### 4.4 Transcendencia (para RR)

O RR exige demonstracao de transcendencia (art. 896-A CLT). O parecer avalia se a causa apresenta indicador economico, politico, social ou juridico de transcendencia — sem ele, o RR nao e conhecido.

### 4.5 Repercussao geral (para RE)

O RE exige repercussao geral (art. 102 §3o CF). O parecer avalia se a questao constitucional ultrapassa o interesse das partes.

### 4.6 Merito — chance de reforma

Avaliar a solidez da tese recursal: erro de julgamento ou de procedimento na decisao? jurisprudencia favoravel (classificada nos 3 niveis)? a tese resiste ao prisma do tribunal ad quem?

### 4.7 Custo-beneficio

Confrontar: custo do recurso (deposito recursal, custas, honorarios, tempo) x probabilidade de exito x valor em discussao. Para a reclamada, ponderar o deposito recursal. Considerar a alternativa do acordo quando o prognostico for desfavoravel.

## 5. PROGNOSTICO

Apresentar prognostico **fundamentado** — cenarios e probabilidades — nunca promessa de resultado (PA-21). A recomendacao final e objetiva: recorrer, nao recorrer, ou (no caso de a outra parte ter recorrido) contra-arrazoar com tal estrategia.

## 6. VEDACOES ESPECIFICAS

- **PA-06** — o parecer e parecer; nao se mistura com peca processual.
- **PA-08** — o prazo do recurso analisado e cravado corretamente.
- **PA-21** — prognostico fundamentado, nunca garantia de exito.
- **PA-01** — jurisprudencia citada no parecer e classificada nos 3 niveis.

## 7. INTEGRACAO

Acionada por: `trabalhista-master`, `/parecer-trabalhista`. Antecede as skills recursais (`recurso-ordinario-trabalhista`, `recurso-revista-trabalhista`, etc.). Entrega para: `suprema-corte-trabalhista` (R1-R4) — auditoria de parecer.
