---
name: contestacao-trabalhista
description: >
  CONTESTACAO TRABALHISTA — Skill Tier 2 (lado reclamada). Redige a contestacao empresarial completa: preliminares, prejudiciais de merito (prescricao), impugnacao especificada dos fatos e pedidos, impugnacao a documentos e ao valor da causa. Use quando o cliente e a reclamada e o usuario pede contestacao, defesa da empresa, defender a empresa na reclamacao trabalhista.
---

# CONTESTACAO TRABALHISTA

> Skill **Tier 2** — Tenente de peca de conhecimento, **lado reclamada**. Produz a contestacao empresarial na Reclamacao Trabalhista. Acionada apos o Checkpoint 4, quando o `CASO.md` registra `Polo do cliente: reclamada`.

---

## 0. ESCOPO E ACIONAMENTO

Acionada pela `trabalhista-master` quando a linha estrategica esta validada e o polo e reclamada. Produz contestacao em rito ordinario ou sumarissimo.

## 1. VERIFICACAO DE POLO (PA-05)

**Antes de redigir**, confirmar no `CASO.md`: `Polo do cliente: reclamada`. Se for reclamante, **parar** e acionar a `peticao-inicial-trabalhista`. Se indefinido, parar e perguntar.

## 2. POSICAO NA ORQUESTRA

```
linha-estrategica (Checkpoint 4)  ->  CONTESTACAO-TRABALHISTA  ->  suprema-corte-trabalhista (R1-R4)
```

Consome: mapa de fatos (auditoria documental — a prova documental e a arma da reclamada), linha estrategica, jurisprudencia, CCT. Apoio: `estilo-juridico-trabalhista`.

## 3. ESTRUTURA DA CONTESTACAO

```
1. ENDERECAMENTO E QUALIFICACAO  — reclamada (razao social, CNPJ, sede)
2. BREVE SINTESE DA DEMANDA      — reconstrucao critica dos fatos da exordial
3. PRELIMINARES
   - incompetencia (territorial — art. 651 CLT; material)
   - inepcia da inicial (pedido indeterminado/iliquido — art. 840 §§1o/3o CLT)
   - ilegitimidade de parte; carencia de acao
   - manifestacao sobre o regime do Juizo 100% Digital (conforme Resolucao do TRT)
4. PREJUDICIAIS DE MERITO
   - prescricao bienal (art. 7o XXIX CF) e quinquenal (art. 11 CLT)
5. IMPUGNACAO ESPECIFICA AOS FATOS  — fato nao impugnado se presume verdadeiro
6. NO MERITO — IMPUGNACAO PONTO A PONTO  — um bloco por pedido do reclamante
7. DO ONUS DA PROVA               — impugnacao a inversao quando indevidamente invocada
8. DA GRATUIDADE DE JUSTICA       — impugnacao quando aplicavel (art. 790 §§3o/4o CLT)
9. DA SUCUMBENCIA E HONORARIOS    — art. 791-A CLT
10. DA LITIGANCIA DE MA-FE        — quando flagrante
11. DOS PEDIDOS                   — preliminares, improcedencia total, honorarios, ma-fe
12. DOS REQUERIMENTOS FINAIS      — provas, depoimento pessoal, testemunhas, pericia
```

## 4. IMPUGNACAO PONTO A PONTO — TECNICA

Cada pedido do reclamante recebe um **bloco autonomo** (FIRAC):
1. **Reconstrucao do fato sob o angulo da reclamada** — desconstruir a narrativa obreira com cronologia e dados objetivos.
2. **Fundamento legal** — CLT, CF, CPC subsidiario, norma coletiva, regulamento interno.
3. **Jurisprudencia consolidada** — Sumulas/OJs do TST, Temas STF, classificadas em 3 niveis.
4. **Prova documental que ampara a tese** — cartoes de ponto, holerites, ficha de EPI, ASOs, PPP, LTCAT, contrato, CCT.
5. **Conclusao** — pedido de improcedencia do tema.

Pedido nao impugnado especificamente presume-se incontroverso — impugnar **todos**.

## 5. TESES DEFENSIVAS RECORRENTES

| Pedido do reclamante | Tese central da reclamada |
|----------------------|---------------------------|
| Reconhecimento de vinculo | ausencia de requisito do art. 3o CLT; contratacao civil/PJ licita; autonomia real |
| Horas extras | cartoes de ponto validos; jornada registrada; banco de horas/compensacao por norma coletiva |
| Insalubridade/periculosidade | EPI eficaz fornecido (ficha de EPI); ausencia de agente nocivo; laudo a impugnar tecnicamente |
| Acumulo/desvio de funcao | compatibilidade da funcao (art. 456 paragrafo unico CLT); ausencia de funcao superior |
| Equiparacao salarial | ausencia de identidade de funcao; diferenca de produtividade/perfeicao tecnica; quadro de carreira |
| Rescisao indireta | ausencia de falta grave patronal; cumprimento contratual; perdao tacito (continuidade do trabalho) |
| Justa causa (defesa da aplicacao) | enquadramento no art. 482 CLT; imediatidade, proporcionalidade, gradacao, non bis in idem |
| Verbas rescisorias / multas 467 e 477 | comprovacao do pagamento no prazo; ausencia de verba incontroversa em mora |
| Dano moral | ausencia de ato ilicito e de lesao; mero dissabor nao indeniza |

## 6. INTERTEMPORAL

Verificar o marco da Reforma 13.467/2017 (Protocolo 6). Para contrato/fato posterior a 11/11/2017, sustentar a aplicacao plena da Reforma; para anterior, nao aplica-la retroativamente (PA-07) — inclusive quanto a honorarios de sucumbencia, que dependem da data de ajuizamento e do regime aplicavel.

## 7. LIMITACAO DA CONDENACAO AOS VALORES DA INICIAL

Tese defensiva de fechamento, deduzida nos pedidos da contestacao. Para acoes ajuizadas sob a Reforma Trabalhista, o **art. 840 §1o da CLT** exige que cada pedido seja **certo, determinado e com indicacao de valor**. A tese: a eventual condenacao deve ficar **limitada aos valores indicados** pelo reclamante em cada pedido da exordial — o valor atribuido a cada pedido opera como teto da condenacao daquele pedido.

- **Como deduzir** — requerer expressamente, ainda que em eventualidade (apos a improcedencia), que qualquer condenacao observe o valor de cada pedido liquidado na inicial, vedado o excesso.
- **Direito intertemporal (Protocolo 6 / PA-07)** — a tese se aplica a **acoes ajuizadas sob a Reforma** (a partir de 11/11/2017), regime em que vigora a exigencia do pedido liquido. Acao anterior segue o regime processual do seu tempo.
- **Verificacao `[VERIFICAR]`** — o tema foi consolidado pelo TST em julgamento de Incidente de Recurso Repetitivo (IRR); o teor do precedente e os seus limites (ex.: efeito de ressalva expressa "valores por estimativa", correcao e juros) devem ser confirmados na busca viva antes de cravar numero ou tese (Protocolo 1).

## 8. VEDACOES ESPECIFICAS

- **PA-05** — so redige pela reclamada; confirma o polo no `CASO.md`.
- **PA-14** — sempre explicitar a distribuicao do onus; impugnar inversao indevida.
- **PA-13** — laudo pericial se ataca tecnicamente, com quesitos — nunca so com retorica.
- **PA-15** — impugnacao que depende de documento essencial ausente: sinalizar Ponto de Omissao.
- **PA-01/PA-02/PA-11** — jurisprudencia classificada; CCT confirmada; dispositivo existente.
- **PA-17** — combatividade ataca a tese do reclamante, nunca a sua pessoa.

## 9. INTEGRACAO

Acionada por: `trabalhista-master` (polo reclamada). Apoio: `estilo-juridico-trabalhista`, `jurisprudencia-trabalhista`, `cct-normas-coletivas`, `auditoria-documental-trabalhista`. Entrega obrigatoriamente para: `suprema-corte-trabalhista` (R1-R4) antes da entrega (PA-24).
