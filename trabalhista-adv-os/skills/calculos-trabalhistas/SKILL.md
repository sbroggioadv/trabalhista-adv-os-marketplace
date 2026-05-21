---
name: calculos-trabalhistas
description: >
  CALCULOS TRABALHISTAS — Skill Tier 2 transversal. Engine de calculo de verbas e reflexos trabalhistas: rescisorias, horas extras, adicionais, FGTS, juros e correcao monetaria (IPCA-E + Selic, Tema ADC 58/59 STF). Nunca calcula sem dado-base. Use quando menciona calculo trabalhista, liquidar valores, verbas rescisorias, valor da causa, planilha de calculo.
---

# CALCULOS TRABALHISTAS

> Skill **Tier 2** de instrucao, transversal. Engine de calculo de verbas trabalhistas, reflexos, juros e correcao. Produz memoria de calculo detalhada. Nunca calcula sem dado-base (PA-20).

---

## 0. ESCOPO E ACIONAMENTO

Acionada sempre que ha valores a apurar: valor da causa, liquidacao de pedidos, atualizacao de verbas. Tambem pelo `/calculo-trabalhista`.

## 1. SIDE-AWARENESS

Leia o `Polo do cliente` no `CASO.md`:
- Cliente = **reclamante** -> calcular os pedidos a postular (valor da causa) e a liquidacao a favor.
- Cliente = **reclamada** -> calcular o valor controvertido para deposito recursal, e conferir/impugnar os calculos do reclamante.

O calculo e tecnico e neutro; o **uso** dele serve ao polo.

## 2. PROTOCOLO 4 — 5 ETAPAS DO CALCULO

1. **Mapear** o periodo contratual e o marco intertemporal (Reforma 11/11/2017).
2. **Apurar cada verba** com a base de calculo correta.
3. **Aplicar reflexos**.
4. **Aplicar juros e correcao** (ADC 58/59 STF).
5. **Memoria detalhada** — fundamento, base, indice, total.

**Sem dado-base, nao calcular (PA-20):** se faltar salario, data, jornada, sinalizar Ponto de Omissao e parar aquele calculo.

## 3. VERBAS RESCISORIAS

| Verba | Calculo |
|-------|---------|
| Saldo de salario | dias trabalhados / 30 x salario |
| Aviso previo indenizado | 30 dias + 3 dias por ano de servico, ate 90 dias (Lei 12.506/2011) |
| 13o proporcional | meses trabalhados / 12 x salario (fracao >= 15 dias conta como mes) |
| Ferias proporcionais + 1/3 | (meses / 12 x salario) + um terco constitucional |
| Ferias vencidas + 1/3 | salario + um terco, se houver periodo aquisitivo completo nao gozado |
| FGTS | 8% sobre a remuneracao do periodo |
| Multa do FGTS | 40% sobre o saldo (dispensa sem justa causa) |

A modalidade de rescisao altera o que e devido — conferir no `CASO.md`.

## 4. HORAS EXTRAS E ADICIONAIS

- **Horas extras** — hora normal + adicional (minimo 50%, CF art. 7o XVI; ou o percentual da CCT). Base: divisor da jornada (220, 200, etc.).
- **Reflexos das horas extras** — a habitualidade das horas extras gera repercussao em DSR, ferias + 1/3, 13o, aviso previo e FGTS. Citar o verbete especifico de cada reflexo so apos confirma-lo (Protocolo 1): a integracao em DSR e a vedacao ao bis in idem ("dobra do DSR" nos demais reflexos) tem disciplina propria — entre os verbetes do TST aplicaveis estao a Sumula 376 e a OJ 394 da SDI-1, conforme o reflexo discutido. Sem confirmacao do verbete, descrever o instituto sem cravar numero.
- **Adicional noturno** — minimo 20% (urbano), hora noturna reduzida (52min30s).
- **Adicional de insalubridade** — 10/20/40% sobre a base legal (apos pericia).
- **Adicional de periculosidade** — 30% sobre o salario base (apos pericia).
- **Intervalo intrajornada** suprimido — pagamento do periodo (atencao a alteracao da Reforma: pos-11/11/2017, so o tempo suprimido, com adicional, natureza indenizatoria — art. 71 §4o CLT).

## 5. JUROS E CORRECAO — ADC 58/59 STF + LEI 14.905/2024

Aplicar o entendimento das ADC 58 e 59 do STF:
- **Fase pre-judicial** (do vencimento ate o ajuizamento) — correcao pelo **IPCA-E** + juros legais (TR / juros da poupanca, conforme a modulacao).
- **Fase judicial** (do ajuizamento em diante) — **taxa Selic** (que ja engloba correcao e juros).

**Lei 14.905/2024** `[VERIFICAR]` — alterou os arts. 389 e 406 do Codigo Civil, fixando nova metodologia legal de juros e correcao monetaria para o periodo posterior a sua vigencia: correcao pelo **IPCA** e juros pela **Selic deduzido o IPCA**. A norma complementa — nao revoga — o decidido nas ADC 58/59; a aplicacao no processo do trabalho e o termo de transicao dependem da regra vigente no momento do calculo. Tratar sempre como `[VERIFICAR]`: confirmar a metodologia em vigor antes de produzir a conta.

## 6. MEMORIA DE CALCULO

A saida e uma **memoria de calculo**: cada verba com fundamento legal, base, periodo, indice, percentual e total; subtotais por verba; total geral. A memoria e auditavel — qualquer terceiro consegue refazer.

## 7. VEDACOES ESPECIFICAS

- **PA-20** — nunca calcular sem dado-base; sem o dado, sinalizar e parar.
- **PA-07** — aplicar a lei do tempo do fato; intervalo, banco de horas e outros institutos mudaram com a Reforma — segmentar contrato "a cavalo".
- **PA-16** — usar o adicional/piso da CCT quando a categoria a possui.
- **PA-06** — o calculo e calculo; nao se mistura com peca ou parecer.

## 8. INTEGRACAO

Acionada por: `trabalhista-master`, `/calculo-trabalhista`, e as skills produtoras (peticao inicial — valores dos pedidos; liquidacao). Apoio: `cct-normas-coletivas` (adicionais convencionais). Entrega para: `suprema-corte-trabalhista` (R1-R4) — a R2 confere a metodologia.
