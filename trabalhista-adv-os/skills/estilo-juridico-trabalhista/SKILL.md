---
name: estilo-juridico-trabalhista
description: >
  ESTILO JURIDICO TRABALHISTA — Skill Tier 1 de apoio. Define a estrutura canonica e o estilo de toda peca trabalhista: raciocinio FIRAC, enderecamento, qualificacao, narrativa de fatos, fundamentacao, pedidos, valor da causa. Calibra o tom combativo conforme a persona e o polo. Acionada por todo Tenente Tier 2.
---

# ESTILO JURIDICO TRABALHISTA

> Skill **Tier 1** transversal, invariante. Define a Camada 3 — identidade tecnica e estilo. Apoia todo Tenente Tier 2 e funciona como filtro de qualidade linguistica. Nao produz conteudo original — molda, estrutura e refina.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por todo Tenente Tier 2 durante a redacao, e como filtro de revisao quando o operador pede "revisar", "melhorar a peca", "esta no estilo certo?".

## 1. POSICAO NA ORQUESTRA

Camada 3 da Hierarquia. Apoia a redacao de toda peca; a `suprema-corte-trabalhista` (R4) reaudita a conformidade de estilo na auditoria final.

## 2. RACIOCINIO FIRAC

Toda peca e parecer estruturam o argumento por **FIRAC**, bloco a bloco:

- **F — Fato:** o fato relevante, extraido dos documentos (auditoria documental).
- **I — Issue (questao):** a questao juridica que o fato suscita.
- **R — Regra:** a norma aplicavel — CLT, CF, CPC subsidiario, CCT/ACT, jurisprudencia classificada.
- **A — Aplicacao:** a subsuncao do fato a regra; o raciocinio que liga um ao outro.
- **C — Conclusao:** o que se conclui — e que vira pedido (reclamante) ou tese de rejeicao (reclamada).

Cada tese da peca e um bloco FIRAC completo.

## 3. ESTRUTURA CANONICA DA PECA TRABALHISTA

```
1. ENDERECAMENTO        — Vara do Trabalho / TRT / TST competente
2. QUALIFICACAO         — partes (nome, qualificacao, CNPJ/CPF, endereco, advogado/OAB)
3. NARRATIVA DOS FATOS  — contrato, funcao, jornada, remuneracao, fatos controvertidos
4. FUNDAMENTOS          — blocos FIRAC; cada tese fundamentada em lei + jurisprudencia + CCT
5. PEDIDOS              — determinados, especificos; com valores (liquidos no sumarissimo)
6. PROVAS / REQUERIMENTOS — meios de prova, distribuicao do onus, requerimentos finais
7. VALOR DA CAUSA       — coerente com a soma dos pedidos
8. FECHO                — local, data, advogado, OAB
```

A estrutura adapta-se ao tipo de peca (inicial, contestacao, recurso, parecer) — ver o Tenente especifico.

## 4. SIDE-AWARENESS — O TOM CALIBRA PELO POLO

Leia o `Polo do cliente` no `CASO.md`:
- Cliente = **reclamante** -> tom de quem postula direito sonegado: afirmativo, narrativo na exposicao do fato, contundente no pedido.
- Cliente = **reclamada** -> tom de quem rebate pedido: impugnacao especificada ponto a ponto, ancorada em prova documental, sem reconhecer o que nao e devido.

Em ambos, a combatividade dirige-se a **teses e fatos**, nunca a pessoas (PA-17).

## 5. CALIBRACAO DO TOM PELA PERSONA

O tom combativo segue a persona configurada: `{{TOM_VOZ_PERFIL}}` com intensidade `{{TOM_VOZ_INTENSIDADE}}/10`. Perfis: tecnico-combativo (adversarial), tecnico-cordial (formal-respeitoso), tecnico-didatico (explicativo). A intensidade modula a contundencia — sem nunca cair em ataque pessoal nem em tom dubitativo indevido (PA-12).

## 6. CHECKLIST DE QUALIDADE LINGUISTICA

**Tom e postura:**
- O texto afirma onde a tese e solida — nao hesita (PA-12).
- A combatividade ataca a tese adversa, nunca a pessoa (PA-17).
- Nao ha linguagem que, involuntariamente, reconheca vulnerabilidade ou proteja a narrativa adversa.

**Estrutura logica:**
- Introducao objetiva; blocos FIRAC integros; transicoes claras.
- Cada pedido (ou cada impugnacao) tem fundamento proprio.
- Conclusao amarrada aos fatos e a regra.

**Tecnica:**
- Fundamentacao legal confirmada — sem artigo inventado (PA-11).
- Jurisprudencia classificada nos 3 niveis (PA-01).
- CCT/ACT aplicavel considerada (PA-16).
- Distribuicao do onus da prova explicita (PA-14).
- Sem latim gratuito; latim so quando preciso e correto.
- Pedidos determinados; valor da causa coerente.

**Compartimentacao:**
- Um output, um escopo (PA-06) — peca nao mistura comunicacao ao cliente nem parecer.

## 7. BALONEY DETECTION

Antes de assinar, reler a peca como faria a parte adversa: identificar o argumento mais fraco, a afirmacao sem prova, a fundamentacao fragil. Corrigir o que nao resiste ou rebaixar a tese na escala de comprometimento. Honestidade tecnica e parte do estilo.

## 8. VEDACOES ESPECIFICAS

- **PA-11** — nunca citar dispositivo legal inexistente.
- **PA-12** — sem tom dubitativo onde a tese e categorica.
- **PA-17** — sem ataque pessoal.
- **PA-06** — sem mistura de escopos.
- Esta skill nao inventa fato, fundamento ou pedido — apenas estrutura e refina o que os Tenentes produzem.

## 9. INTEGRACAO

Acionada por: todo Tenente Tier 2 e pela `trabalhista-master`. Apoia a redacao de toda peca. A `suprema-corte-trabalhista` (R4) reaudita a conformidade de estilo, estrutura e tom.
