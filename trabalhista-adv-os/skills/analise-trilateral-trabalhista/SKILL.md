---
name: analise-trilateral-trabalhista
description: >
  ANALISE TRILATERAL TRABALHISTA — Skill Tier 1. Antes de qualquer producao, analisa o caso por tres prismas obrigatorios: Cliente (o que sustenta a tese), Parte adversa (a defesa/ataque adversarial mais forte) e Juiz (como o caso aparece para quem decide). O prisma Cliente flipa conforme o polo. Gera matriz de pontos fortes, fragilidades e contra-teses. Acionada apos a triagem, antes da redacao.
---

# ANALISE TRILATERAL TRABALHISTA

> Skill **Tier 1** — Estado-Maior. Submete o caso a um teste de resistencia: 3 prismas em sequencia (Cliente, Parte adversa, Juiz) + sintese. O resultado alimenta a `linha-estrategica-trabalhista` e os Tenentes Tier 2 com inteligencia tatica testada.

---

## 0. ESCOPO E ACIONAMENTO

Acionada apos os Checkpoints 1 e 2, em paralelo com a `jurisprudencia-trabalhista`. Encerra no Checkpoint 3.

## 1. POSICAO NA ORQUESTRA

```
auditoria-documental + cct  ->  ANALISE-TRILATERAL  +  jurisprudencia  ->  CHECKPOINT 3
                                                                       ->  linha-estrategica
```

## 2. SIDE-AWARENESS — O PRISMA "CLIENTE" FLIPA

Leia o `Polo do cliente` no `CASO.md`. O prisma "Cliente" assume o lado do polo:
- Cliente = **reclamante** -> o prisma 1 fortalece a tese de quem postula direito.
- Cliente = **reclamada** -> o prisma 1 fortalece a tese de quem rebate o pedido.

O prisma "Parte adversa" e sempre o **outro lado**. O prisma "Juiz" e imparcial.

---

## 3. PRISMA 1 — CLIENTE (o lado do polo do cliente)

Assuma o papel de advogado senior do mesmo lado do cliente. Objetivo: **fortalecer a posicao**.

1. **Melhores argumentos** — os 5 mais fortes, em ordem de impacto.
2. **Provas favoraveis** — documentais (cartao de ponto, holerite, CTPS, contrato, TRCT, laudos, CCT), testemunhais, periciais.
3. **Jurisprudencia a favor** — hierarquizada (STF > TST-SDI > TST-Turmas > TRT). Classificar nos 3 niveis do Protocolo 1.
4. **Distribuicao do onus** — quais fatos o cliente precisa provar e quais cabem a parte adversa (art. 818 CLT / 373 CPC).
5. **Estrategia ofensiva** — como atacar os pontos fracos da parte adversa.
6. **Pontos subutilizados** — fatos ou circunstancias a explorar.

## 4. PRISMA 2 — PARTE ADVERSA

Assuma o papel do advogado adversario. Objetivo: **destruir os argumentos do cliente**.

1. **Fragilidades** — onde a tese do cliente e mais vulneravel.
2. **Contra-argumentos** — os 5 melhores, fundamentados.
3. **Provas contra** — fatos e documentos que enfraquecem a posicao do cliente.
4. **Jurisprudencia contraria** — precedentes favoraveis ao adversario.
5. **Preliminares / prejudiciais** — incompetencia, inepcia, prescricao, ilegitimidade.
6. **Estrategia adversaria** — como o outro lado vai desconstruir cada argumento.

Encontrar TODAS as fraquezas — omitir vulnerabilidade aqui e falha grave.

## 5. PRISMA 3 — JUIZ

Assuma o papel do magistrado julgador. Objetivo: **decidir com base na lei, na prova e na jurisprudencia**, sem vies.

1. **Fatos incontroversos** — o que ambas as partes admitem.
2. **Pontos controvertidos** — o que depende de prova.
3. **Peso das provas** — para cada ponto controvertido, qual lado tem a prova mais forte e a quem cabe o onus.
4. **Enquadramento juridico** — CLT, CF, CPC subsidiario, CCT/ACT aplicaveis.
5. **Jurisprudencia determinante** — precedentes que o juizo tende a seguir.
6. **Tendencia de julgamento** — resultado mais provavel, por pedido.
7. **O que mudaria a decisao** — o que cada lado precisaria provar.

Nao contaminar este prisma com vies favoravel ao cliente.

---

## 6. SINTESE ESTRATEGICA

Com os 3 prismas completos:

1. **Diagnostico consolidado** — pontos fortes confirmados (Cliente + Juiz concordam); vulnerabilidades reais (Adversa + Juiz concordam); pontos genuinamente controversos.
2. **Mapa de provas criticas** — para cada ponto: status da prova, impacto se provado, impacto se nao provado, acao recomendada.
3. **Recomendacao** — argumentos a priorizar (confirmados pelo teste), argumentos a abandonar (fragilizados), prognostico fundamentado (nunca promessa — PA-21), e, quando o risco for alto, alternativas ao litigio (acordo).

---

## 7. VEDACOES ESPECIFICAS

- **PA-05** — o prisma Cliente segue o polo do `CASO.md`; nunca inverter.
- **PA-01** — nao fabricar jurisprudencia em nenhum prisma.
- Nunca pular um prisma — os 3 sao obrigatorios e sequenciais.
- Nunca omitir vulnerabilidade identificada no Prisma 2.
- **PA-21** — prognostico, nunca promessa de resultado.

## 8. INTEGRACAO

Acionada por: `trabalhista-master` (apos triagem e auditoria). Trabalha em paralelo com: `jurisprudencia-trabalhista`. Entrega para: `linha-estrategica-trabalhista`. A `suprema-corte-trabalhista` (R3) verifica se a estrategia derivada da trilateral foi implementada na peca.
