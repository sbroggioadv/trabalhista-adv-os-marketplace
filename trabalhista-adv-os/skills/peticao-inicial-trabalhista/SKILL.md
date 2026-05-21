---
name: peticao-inicial-trabalhista
description: >
  PETICAO INICIAL TRABALHISTA — Skill Tier 2 (lado reclamante). Redige a Reclamacao Trabalhista completa: qualificacao, narrativa do vinculo e dos fatos, causas de pedir, pedidos determinados com valores, tutelas de urgencia, requerimentos. Use quando o cliente e o reclamante e o usuario pede peticao inicial, reclamatoria, ajuizar acao trabalhista, processar a empresa.
---

# PETICAO INICIAL TRABALHISTA

> Skill **Tier 2** — Tenente de peca de conhecimento, **lado reclamante**. Produz a Reclamacao Trabalhista (RT) — a peca ativa do trabalhador. Acionada apos o Checkpoint 4, quando o `CASO.md` registra `Polo do cliente: reclamante`.

---

## 0. ESCOPO E ACIONAMENTO

Acionada pela `trabalhista-master` quando a linha estrategica esta validada e o polo e reclamante. Produz a RT em rito ordinario ou sumarissimo.

## 1. VERIFICACAO DE POLO (PA-05)

**Antes de redigir**, confirmar no `CASO.md`: `Polo do cliente: reclamante`. Se for reclamada, **parar** e acionar a `contestacao-trabalhista`. Se o polo estiver indefinido, parar e perguntar.

## 2. POSICAO NA ORQUESTRA

```
linha-estrategica (Checkpoint 4)  ->  PETICAO-INICIAL-TRABALHISTA  ->  suprema-corte-trabalhista (R1-R4)
```

Consome: mapa de fatos (auditoria documental), linha estrategica, jurisprudencia, CCT. Apoio: `estilo-juridico-trabalhista`, `calculos-trabalhistas` (valores dos pedidos).

## 3. ESTRUTURA DA RECLAMACAO TRABALHISTA

```
1. ENDERECAMENTO        — Vara do Trabalho competente (art. 651 CLT — local da prestacao)
2. QUALIFICACAO         — reclamante (nome, CPF, CTPS, endereco) e reclamada(s) (razao social, CNPJ)
3. DOS FATOS            — narrativa do vinculo: admissao, funcao, jornada, remuneracao, fatos
4. DO DIREITO           — blocos FIRAC; cada causa de pedir fundamentada
5. DA TUTELA DE URGENCIA — quando cabivel (ex.: reintegracao de estavel, restabelecimento)
6. DOS PEDIDOS          — discriminados, determinados, com valores (liquidos no sumarissimo)
7. DO VALOR DA CAUSA    — soma dos pedidos
8. DAS PROVAS E REQUERIMENTOS — meios de prova, depoimento pessoal, testemunhas, pericia,
                          gratuidade de justica (art. 790 §§3o/4o CLT), exibicao de documentos
9. FECHO                — local, data, advogado, OAB
```

## 4. NARRATIVA DOS FATOS

Reconstruir o vinculo de forma cronologica e afirmativa: data de admissao, funcao real (e nao so a anotada), jornada efetivamente cumprida, remuneracao (inclusive parcelas "por fora"), e os fatos que fundam cada pedido. A narrativa do reclamante e assertiva — afirma o fato; a prova vem na instrucao.

## 5. CAUSAS DE PEDIR RECORRENTES

| Tema | Tese central do reclamante |
|------|----------------------------|
| Reconhecimento de vinculo | presenca dos requisitos do art. 3o CLT — pessoalidade, habitualidade, subordinacao, onerosidade — apesar da forma (PJ/MEI/autonomo) |
| Horas extras | jornada extraordinaria habitual; cartao de ponto britanico/invalido; onus da reclamada (Sumula 338 TST) |
| Adicional de insalubridade/periculosidade | exposicao a agente nocivo; EPI ineficaz ou nao fornecido; necessidade de pericia (art. 195 CLT) |
| Acumulo/desvio de funcao | exercicio de funcao diversa/superior sem contraprestacao |
| Equiparacao salarial | identidade de funcao com paradigma; art. 461 CLT; Sumula 6 TST |
| Verbas rescisorias | parcelas nao pagas ou pagas a menor; multas dos arts. 467 e 477 CLT |
| Rescisao indireta | falta grave patronal (art. 483 CLT) — descumprimento contratual do empregador |
| Estabilidade gestante | dispensa na vigencia da garantia (art. 10 II b ADCT; Sumula 244 TST) |
| Dano moral | lesao a direito da personalidade no contrato de trabalho |

Cada causa de pedir vira um bloco FIRAC e gera o pedido correspondente.

## 6. PEDIDOS

Pedidos **determinados e especificos**. No rito sumarissimo (ate 40 salarios minimos), a liquidacao de cada pedido e obrigatoria (art. 852-B CLT); no ordinario, indicar valor por pedido (art. 840 §1o CLT pos-Reforma). Os valores vem da `calculos-trabalhistas`. Incluir reflexos (DSR, ferias, 13o, FGTS, aviso previo) e os pedidos acessorios (juros, correcao — ADC 58/59 STF; honorarios contratuais; gratuidade).

## 7. PRESCRICAO E INTERTEMPORAL

- Ajuizar dentro do prazo bienal (art. 7o XXIX CF — 2 anos da extincao do contrato).
- Pedir verbas dos ultimos 5 anos retroativos do ajuizamento (prescricao quinquenal — art. 11 CLT).
- Aplicar a lei do tempo do fato (Protocolo 6) — fato pre-11/11/2017 nao recebe a Reforma (PA-07).

## 8. VEDACOES ESPECIFICAS

- **PA-05** — so redige pela reclamante; confirma o polo no `CASO.md`.
- **PA-04** — nao inventar data, salario, funcao, jornada; o que faltar, Ponto de Omissao.
- **PA-15** — pedido que depende de documento essencial ausente: sinalizar (e considerar pedir exibicao).
- **PA-20** — valores dos pedidos vem de calculo com dado-base; sem dado, sinalizar.
- **PA-01/PA-02/PA-11** — jurisprudencia classificada; CCT confirmada; dispositivo legal existente.
- **PA-21** — nao prometer procedencia nem gratuidade como certas.

## 9. INTEGRACAO

Acionada por: `trabalhista-master` (polo reclamante). Apoio: `estilo-juridico-trabalhista`, `calculos-trabalhistas`, `jurisprudencia-trabalhista`, `cct-normas-coletivas`. Entrega obrigatoriamente para: `suprema-corte-trabalhista` (R1-R4) antes da entrega ao operador (PA-24).
