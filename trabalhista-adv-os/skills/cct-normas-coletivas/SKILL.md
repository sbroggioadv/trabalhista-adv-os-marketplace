---
name: cct-normas-coletivas
description: >
  CCT E NORMAS COLETIVAS — Skill Tier 1. Trata a Convencao/Acordo Coletivo de Trabalho da categoria: le a norma anexada ao caso, indexa as clausulas e aplica na peca; se faltar, tenta localizar no sistema Mediador do MTE e em portais sindicais, sempre marcando [VERIFICAR]. Nunca inventa clausula. Use quando o caso envolver CCT, ACT, convencao coletiva, acordo coletivo, norma da categoria, sindicato, piso normativo.
---

# CCT E NORMAS COLETIVAS

> Skill **Tier 1** — Estado-Maior. A norma coletiva e fonte autonoma de direito (CF art. 7o XXVI). Esta skill le, indexa e aplica a CCT/ACT do caso; nunca inventa clausula (PA-02); nunca omite norma aplicavel (PA-16). Roda em paralelo com a `auditoria-documental-trabalhista`.

---

## 0. ESCOPO E ACIONAMENTO

Acionada apos a triagem (em paralelo com a auditoria documental) e sempre que houver categoria com norma coletiva. Encerra no Checkpoint 2.

## 1. POSICAO NA ORQUESTRA

```
triagem  ->  auditoria-documental  +  CCT-NORMAS-COLETIVAS  ->  CHECKPOINT 2
```

## 2. CCT x ACT — O QUE A SKILL TRATA

- **CCT (Convencao Coletiva de Trabalho)** — pactuada entre o sindicato dos empregados e o sindicato patronal; vale para toda a categoria.
- **ACT (Acordo Coletivo de Trabalho)** — pactuado entre o sindicato dos empregados e uma ou mais empresas; vale so para aquelas empresas. Em conflito, prevalece a norma mais especifica/favoravel conforme o caso e o art. 620 CLT.

## 3. PROTOCOLO 2 — FLUXO DA NORMA COLETIVA

### 3.1 Upload por caso (caminho principal)

O operador anexa a CCT/ACT vigente em `casos/<caso>/documentos/`. A skill:
1. **Le** a norma integralmente.
2. **Confirma** o periodo de vigencia e o enquadramento da categoria (a norma so se aplica se vigente no periodo do contrato e se a categoria do caso e a da norma).
3. **Indexa** as clausulas relevantes — ver §4.
4. **Aplica** a clausula confirmada a tese e ao calculo.

### 3.2 Fallback de busca

Se a norma nao foi anexada:
1. Tentar localizar no **sistema Mediador do MTE** (registro publico de normas coletivas) e em portais do sindicato da categoria — via WebSearch/WebFetch.
2. Toda clausula obtida por busca, sem o documento oficial em maos, entra marcada **`[VERIFICAR]`**.
3. Pedir ao operador o documento oficial para confirmar.

## 4. CLAUSULAS A INDEXAR

| Tema | O que a clausula pode fixar |
|------|------------------------------|
| Piso salarial | salario minimo da categoria |
| Reajustes | indices e datas-base |
| Jornada | banco de horas, compensacao, turnos, escala |
| Intervalo | reducao de intrajornada (limites pos-Reforma e Tema 1046 STF) |
| Adicionais | horas extras, noturno, insalubridade convencional |
| Beneficios | vale-refeicao/alimentacao, cesta, plano de saude, PLR |
| Garantias | estabilidades convencionais, aviso previo ampliado |
| Contribuicoes | contribuicao assistencial/negocial (atencao a jurisprudencia STF) |

## 5. SIDE-AWARENESS — A NORMA SERVE AOS DOIS POLOS

Leia o `Polo do cliente` no `CASO.md`. A mesma clausula tem usos opostos:
- Cliente = **reclamante** -> a CCT pode fundar pedidos (piso, adicional convencional, beneficio nao pago).
- Cliente = **reclamada** -> a CCT pode **validar flexibilizacoes** (banco de horas, intervalo reduzido) e afastar pedidos, com apoio do Tema 1046 STF (limites do negociado x legislado).

A skill aponta os dois usos e aplica o que serve ao polo do cliente.

## 6. INTERTEMPORAL E NEGOCIADO x LEGISLADO

- Norma coletiva vencida nao se aplica ao periodo posterior a sua vigencia (verificar ultratividade — tema controvertido).
- A Reforma 13.467/2017 ampliou a prevalencia do negociado sobre o legislado (art. 611-A CLT), com limites (art. 611-B CLT — direitos indisponiveis). O Tema 1046 STF fixou os contornos. Aplicar conforme o marco intertemporal (Protocolo 6).

## 7. SAIDA

```
NORMA COLETIVA — <categoria>

Norma: <CCT ou ACT, sindicatos, vigencia>   |   Status: <confirmada | [VERIFICAR]>
Clausulas relevantes ao caso:
- <clausula N>: <teor> -> uso: <causa de pedir / defesa, conforme polo>

Alerta: <norma faltante / vigencia a confirmar / categoria a confirmar>
```

## 8. VEDACOES ESPECIFICAS

- **PA-02** — nunca afirmar clausula que nao foi lida na norma ou confirmada; sem confirmacao, `[VERIFICAR]`.
- **PA-16** — nunca ignorar a norma coletiva quando a categoria a possui.
- Nunca aplicar norma coletiva vencida ou de categoria diversa.
- Vigencia e categoria sempre confirmadas antes de aplicar.

## 9. INTEGRACAO

Acionada por: `trabalhista-master` (apos triagem). Paralela a: `auditoria-documental-trabalhista`. Entrega para: `analise-trilateral-trabalhista`, `linha-estrategica-trabalhista`, `calculos-trabalhistas` e os Tenentes Tier 2. A `suprema-corte-trabalhista` (R1/R2) verifica se a CCT aplicavel foi considerada.
