---
name: linha-estrategica-trabalhista
description: >
  LINHA ESTRATEGICA TRABALHISTA — Skill Tier 1. Consolida o resultado da analise trilateral e da jurisprudencia e define a linha estrategica mais benefica ao polo do cliente. Apresenta a tese central, as teses subsidiarias e os riscos. Use apos a trilateral, quando o usuario pede a estrategia do caso, a melhor tese, a linha de defesa ou de acao.
---

# LINHA ESTRATEGICA TRABALHISTA

> Skill **Tier 1** — Estado-Maior. Transforma o diagnostico (trilateral + jurisprudencia + auditoria documental) numa **decisao estrategica**: a tese central, as subsidiarias, a ordem de batalha e os riscos. Encerra no Checkpoint 4 — o ultimo antes da redacao.

---

## 0. ESCOPO E ACIONAMENTO

Acionada apos o Checkpoint 3. Encerra no Checkpoint 4 — o advogado **valida a linha** antes de qualquer Tenente Tier 2 redigir.

## 1. POSICAO NA ORQUESTRA

```
trilateral + jurisprudencia  ->  LINHA-ESTRATEGICA  ->  CHECKPOINT 4 (advogado valida)  ->  Tenente Tier 2
```

## 2. SIDE-AWARENESS — A LINHA SERVE AO POLO

Leia o `Polo do cliente` no `CASO.md`. A linha estrategica e sempre **a mais benefica ao polo do cliente**:
- Cliente = **reclamante** -> maximizar o reconhecimento de direitos e o quantum; antecipar e neutralizar as defesas da reclamada.
- Cliente = **reclamada** -> minimizar ou afastar a condenacao; priorizar preliminares e prejudiciais; atacar a prova do reclamante.

---

## 3. CONSOLIDACAO DOS INSUMOS

Reunir:
- **Auditoria documental** — o mapa de fatos e os Pontos de Omissao.
- **Analise trilateral** — diagnostico consolidado, mapa de provas criticas, recomendacao.
- **Jurisprudencia** — precedentes classificados nos 3 niveis.
- **CCT/ACT** — clausulas aplicaveis (ou `[VERIFICAR]`).

## 4. DEFINICAO DA TESE CENTRAL

A tese central e a linha-mestra da peca — a que tem o melhor par **forca probatoria + respaldo juridico Nivel 1**. Critérios:
- Sustentada por fato com prova solida (ou com onus favoravel ao cliente).
- Respaldada por lei vigente e jurisprudencia validada.
- Resistente ao Prisma 2 da trilateral (a parte adversa nao a derruba facilmente).

## 5. TESES SUBSIDIARIAS E ORDEM DE BATALHA

Organizar as demais teses em **escala de comprometimento** — da mais forte a mais fraca:
- **Reclamada:** preliminares (incompetencia, inepcia, ilegitimidade) -> prejudiciais (prescricao bienal/quinquenal) -> merito (impugnacao especificada, fato extintivo) -> impugnacao a documentos e ao valor da causa.
- **Reclamante:** causa de pedir principal -> causas subsidiarias -> pedidos cumulados -> tutelas -> pedidos reflexos.

Cada tese subsidiaria existe para o caso de a anterior nao prosperar (eventualidade).

## 6. MAPA DE RISCOS

Para cada risco relevante: descricao, probabilidade, impacto, e a acao de mitigacao. Riscos tipicos: documento essencial faltante (PA-15), prescricao parcial, jurisprudencia adversa consolidada, fragilidade da prova testemunhal, prova pericial desfavoravel.

## 7. RECOMENDACAO DE DESFECHO

Indicar o caminho recomendado e — quando o risco for alto — sinalizar a alternativa do **acordo** (a `acordo-trabalhista` pode ser acionada). Prognostico fundamentado, nunca promessa (PA-21).

## 8. CHECKPOINT 4

Apresentar ao advogado:

```
LINHA ESTRATEGICA — CHECKPOINT 4

Polo: <reclamante | reclamada>
Tese central: <enunciado>
Teses subsidiarias (escala de comprometimento): <lista ordenada>
Preliminares/prejudiciais (se reclamada): <lista>
Riscos principais: <lista + mitigacao>
Prognostico: <fundamentado>
Recomendacao: <litigar / negociar / etc.>

Voce VALIDA esta linha estrategica para eu acionar a redacao da peca?
```

A redacao so comeca apos a validacao. No modo `--continuo`, registrar e seguir.

---

## 9. VEDACOES ESPECIFICAS

- **PA-05** — a linha serve ao polo do cliente; nunca sustentar tese adversa.
- **PA-21** — prognostico fundamentado, nunca garantia de resultado.
- **PA-01/PA-02** — a linha so se apoia em jurisprudencia e norma coletiva confirmadas.
- Nunca definir a linha sem os insumos da trilateral e da auditoria documental.

## 10. INTEGRACAO

Acionada por: `trabalhista-master` (apos a trilateral). Consome: auditoria documental, trilateral, jurisprudencia, CCT. Entrega para: o Tenente Tier 2 do tipo de peca. A linha validada e registrada no `CASO.md` (campo `Linha estrategica`) pela `memoria-de-caso-trabalhista`.
