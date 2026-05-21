---
name: replica-trabalhista
description: >
  REPLICA TRABALHISTA — Skill Tier 2 (lado reclamante). Redige a replica/impugnacao a contestacao: rebate preliminares, prejudiciais e a tese de merito da reclamada e reforca a inicial. Use quando o cliente e o reclamante e ha contestacao a impugnar, ou o usuario pede replica, impugnacao a contestacao, manifestacao sobre a defesa.
---

# REPLICA TRABALHISTA

> Skill **Tier 2** — Tenente de peca de conhecimento, **lado reclamante**. Produz a replica (manifestacao a contestacao). Acionada quando o `CASO.md` registra `Polo do cliente: reclamante` e ja existe contestacao nos autos.

---

## 0. ESCOPO E ACIONAMENTO

Acionada pela `trabalhista-master` quando o polo e reclamante e ha contestacao a impugnar. A replica defende a inicial e ataca a defesa.

## 1. VERIFICACAO DE POLO (PA-05)

Confirmar no `CASO.md`: `Polo do cliente: reclamante`. A replica/impugnacao a contestacao e peca tipica do reclamante; se o polo do cliente for reclamada, **parar** — a defesa da reclamada e a contestacao, nao a replica. Observe-se, porem, que a reclamada tambem pode ser chamada a se manifestar nos autos — por exemplo, sobre **documentos juntados pelo reclamante** com a inicial ou na propria replica (contraditorio sobre prova documental). Essa manifestacao da reclamada nao e replica e segue por outra skill (`acoes-autonomas-impugnacao-trabalhista` ou conforme orientacao do `trabalhista-master`). Se o polo estiver indefinido, parar e perguntar.

## 2. POSICAO NA ORQUESTRA

```
contestacao da reclamada nos autos  ->  REPLICA-TRABALHISTA  ->  suprema-corte-trabalhista (R1-R4)
```

Insumo critico: o **texto integral da contestacao** a impugnar. Sem ele, sinalizar Ponto de Omissao e parar (PA-15).

## 3. FUNCAO DA REPLICA

A replica tem tripla funcao:
1. **Rebater as preliminares** levantadas pela reclamada (incompetencia, inepcia, ilegitimidade).
2. **Rebater as prejudiciais** — sobretudo a prescricao arguida.
3. **Impugnar a tese de merito** da contestacao e **reforcar** as causas de pedir da inicial.

## 4. ESTRUTURA DA REPLICA

```
1. ENDERECAMENTO E REFERENCIA AOS AUTOS
2. DAS PRELIMINARES ARGUIDAS — rebater uma a uma
   - incompetencia: sustentar a competencia (art. 651 CLT — local da prestacao)
   - inepcia: demonstrar que a inicial atende ao art. 840 CLT
   - ilegitimidade: demonstrar a pertinencia subjetiva
3. DA PRESCRICAO ARGUIDA — afastar ou delimitar
   - confrontar o marco bienal/quinquenal; sustentar a tempestividade dos pedidos
4. DA IMPUGNACAO AO MERITO DA CONTESTACAO
   - bloco por bloco, rebater a tese defensiva de cada pedido
   - apontar a impugnacao generica (que nao supre o onus do art. 818 CLT)
   - confrontar a prova documental juntada pela reclamada
5. DA IMPUGNACAO AOS DOCUMENTOS DA RECLAMADA — quando ha documento a impugnar
6. DO REFORCO DAS CAUSAS DE PEDIR — reafirmar a inicial onde a defesa nao a abalou
7. DOS REQUERIMENTOS — provas, manutencao dos pedidos da inicial
```

## 5. TECNICA DE IMPUGNACAO DA DEFESA

Para cada tese defensiva da reclamada:
1. **Identificar** o argumento e a prova em que ele se apoia.
2. **Confrontar** — a tese e generica? contraria a prova? contraria a lei ou a jurisprudencia?
3. **Rebater** com FIRAC: fato, questao, regra, aplicacao, conclusao.
4. **Distribuicao do onus** — apontar quando a reclamada nao se desincumbiu do seu onus (art. 818 CLT; ex.: cartao de ponto nao juntado — Sumula 338 TST).
5. **Reforcar** a causa de pedir original.

## 6. PONTOS DE ATENCAO

- **Impugnacao especifica** — fato da contestacao nao impugnado pode ser tido por aceito; impugnar o que e controvertido.
- **Documentos da reclamada** — manifestar-se sobre os documentos juntados com a defesa (autenticidade, validade, alcance).
- **Prescricao** — se a reclamada arguiu, a replica delimita o periodo efetivamente prescrito (se houver) e preserva o restante.
- **Intertemporal** — sustentar a lei correta do tempo do fato (Protocolo 6); rebater aplicacao retroativa indevida da Reforma pela reclamada (PA-07).

## 7. VEDACOES ESPECIFICAS

- **PA-05** — so redige pela reclamante; confirma o polo.
- **PA-15** — sem o texto da contestacao, nao redigir a replica; sinalizar.
- **PA-14** — explicitar onde a reclamada nao cumpriu o onus probatorio.
- **PA-01/PA-02/PA-11** — jurisprudencia classificada; CCT confirmada; dispositivo existente.
- **PA-17** — atacar a tese da reclamada, nunca a pessoa.

## 8. INTEGRACAO

Acionada por: `trabalhista-master` (polo reclamante). Apoio: `estilo-juridico-trabalhista`, `jurisprudencia-trabalhista`, `auditoria-documental-trabalhista`. Entrega obrigatoriamente para: `suprema-corte-trabalhista` (R1-R4) antes da entrega (PA-24).
