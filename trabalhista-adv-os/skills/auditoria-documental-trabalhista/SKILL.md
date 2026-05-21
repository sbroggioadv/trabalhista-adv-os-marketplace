---
name: auditoria-documental-trabalhista
description: >
  AUDITORIA DOCUMENTAL TRABALHISTA — Skill Tier 1. Audita os documentos do cliente (cartao de ponto, holerites, CTPS, contrato de trabalho, TRCT, ficha de EPI, laudos, CCT) e mapeia os fatos em defesas (reclamada) ou causas de pedir (reclamante). Aplica o Protocolo da Prova. Use quando houver documentos do caso para analisar, ou o usuario diz auditar documentos, analisar provas, cartao de ponto, holerite.
---

# AUDITORIA DOCUMENTAL TRABALHISTA

> Skill **Tier 1** — Estado-Maior. Le os documentos do caso, extrai os fatos juridicamente relevantes e os mapeia conforme o polo: em **causas de pedir** (reclamante) ou em **defesas** (reclamada). Aplica o Protocolo 3 (Prova). Roda apos a triagem, em paralelo com a `cct-normas-coletivas`.

---

## 0. ESCOPO E ACIONAMENTO

Acionada apos o Checkpoint 1. Encerra no Checkpoint 2 (junto com a `cct-normas-coletivas`).

## 1. POSICAO NA ORQUESTRA

```
triagem  ->  AUDITORIA-DOCUMENTAL  +  cct-normas-coletivas  ->  CHECKPOINT 2  ->  trilateral
```

Entrega o **mapa de fatos** — base factual de toda a peca seguinte.

## 2. SIDE-AWARENESS — O MAPEAMENTO FLIPA

Leia o `Polo do cliente` no `CASO.md`:
- Cliente = **reclamante** -> cada documento e lido buscando **causas de pedir** (o que fundamenta o direito postulado) e **prova do fato constitutivo**.
- Cliente = **reclamada** -> cada documento e lido buscando **defesas** (o que impede, modifica ou extingue o direito) e **prova do cumprimento patronal**.

O mesmo cartao de ponto serve a teses opostas conforme o polo — a auditoria explicita isso.

---

## 3. DOCUMENTOS DO CASO — INVENTARIO

Inventariar o que foi anexado em `casos/<caso>/documentos/`:

**Nucleo (toda relacao de emprego):**
- Contrato de trabalho / ficha de registro / dossie de admissao
- CTPS (anotacoes)
- Holerites do periodo (inclusive 13o)
- Aviso e concessao de ferias
- TRCT e comprovantes de FGTS

**Por tema de pedido:**
| Tema | Documentos relevantes |
|------|------------------------|
| Horas extras / jornada | cartoes de ponto, espelhos eletronicos, acordo de banco de horas |
| Insalubridade / periculosidade | ficha de EPI, LTCAT, PPRA/PGR, PCMSO, ASOs, PPP, laudo pericial |
| Vinculo (PJ/MEI/autonomo) | contrato civil, notas fiscais, comprovantes de pagamento, prova de autonomia |
| Acumulo / desvio de funcao | descricao de cargo, organograma, plano de cargos e salarios |
| Estabilidade gestante | atestado, ASO de demissao, prova da ciencia da gravidez |
| Justa causa | advertencias, suspensoes, sindicancia, prova da falta grave |
| Rescisao indireta | prova do cumprimento (ou descumprimento) patronal |
| Dano moral | normas internas, codigo de conduta, investigacao interna |
| Multas arts. 467 e 477 CLT | comprovantes de pagamento das verbas no prazo |

## 4. PROTOCOLO DA PROVA (Protocolo 3) APLICADO

Para cada fato controvertido:

1. **Identificar** o fato e a quem aproveita.
2. **Distribuir o onus** — art. 818 CLT c/c art. 373 CPC. Regra: reclamante prova fato constitutivo; reclamada prova fato impeditivo/modificativo/extintivo. Considerar distribuicao dinamica.
3. **Confrontar com o documento** — o documento prova, contradiz ou e omisso quanto ao fato?
4. **Aplicar presuncoes** — destaque para o cartao de ponto: empresa com 20+ empregados deve mante-lo (art. 74 §2o CLT); a nao juntada gera presuncao da jornada da inicial (Sumula 338 TST).
5. **Verificar a perica** — insalubridade e periculosidade exigem prova pericial (art. 195 CLT). Sinalizar a necessidade.

## 5. PONTOS DE OMISSAO (PA-15)

Quando faltar documento essencial a um pedido especifico:
- **Sinalizar** explicitamente como Ponto de Omissao.
- **Parar a analise daquele pedido** — nao especular o conteudo do documento ausente.
- **Prosseguir** nos demais pedidos cujos documentos existem.
- Listar os documentos faltantes para o operador colher (ou, sendo reclamante, requerer a exibicao — art. 396 CPC).

## 6. SAIDA — MAPA DE FATOS

Entregar uma tabela:

```
MAPA DE FATOS — <cliente> (polo: <reclamante|reclamada>)

| Fato controvertido | Onus de quem | Documento que prova/nega | Forca | Tese (causa de pedir / defesa) |
|--------------------|--------------|--------------------------|-------|-------------------------------|

Pontos de Omissao: <documentos essenciais faltantes>
Necessidade de pericia: <sim/nao — em que pedido>
Marco intertemporal: <pre / pos / a cavalo de 11/11/2017>
```

## 7. VEDACOES ESPECIFICAS

- **PA-04** — nunca afirmar dado fatico que nao consta de documento.
- **PA-15** — sem o documento essencial, sinalizar e parar aquele pedido.
- **PA-13** — laudo pericial nao se afasta com retorica; sinalizar impugnacao tecnica.
- **PA-14** — sempre explicitar a distribuicao do onus.
- **PA-22** — analisar apenas os documentos do caso ativo.

## 8. INTEGRACAO

Acionada por: `trabalhista-master` (apos triagem). Paralela a: `cct-normas-coletivas`. Entrega para: `analise-trilateral-trabalhista` e `linha-estrategica-trabalhista`. O mapa de fatos e insumo direto de todo Tenente Tier 2 e da Suprema Corte R1.
