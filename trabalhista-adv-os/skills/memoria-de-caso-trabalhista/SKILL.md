---
name: memoria-de-caso-trabalhista
description: >
  MEMORIA DE CASO TRABALHISTA — Skill Tier 1. Cria e mantem a pasta de cada caso (casos/<cliente>-x-<adverso>/), o CASO.md (polo, partes, dados do contrato, fase, linha estrategica, prazos) e o MEMORY.md evolutivo. Garante a compartimentacao entre casos. Use ao abrir um caso, retomar um caso, atualizar o estado de um caso ou registrar memoria do caso.
---

# MEMORIA DE CASO TRABALHISTA

> Skill **Tier 1** — Estado-Maior, invariante. Gerencia a memoria persistente caso a caso: cria a pasta, mantem o `CASO.md` e o `MEMORY.md`, e garante a compartimentacao (PA-22). Acionada pela triagem na abertura e por todas as skills ao registrar evolucao.

---

## 0. ESCOPO E ACIONAMENTO

Acionada pela `triagem-trabalhista` (abrir/retomar caso), pelo `/caso-trabalhista`, e por qualquer skill ao final de uma etapa (registrar evolucao).

## 1. ESTRUTURA DA MEMORIA DE CASO

```
<cwd>/trabalhista/
├── persona.md          identidade do operador (gerada pelo onboarding)
├── config.md           polos, especialidades, tom, modo de fluxo
└── casos/
    └── <cliente>-x-<adverso>/      1 pasta por caso
        ├── CASO.md                 ficha do caso (fonte unica do polo)
        ├── MEMORY.md               log evolutivo do caso
        ├── documentos/             docs do cliente + CCT/ACT anexada
        ├── pecas/                  pecas produzidas (versionadas)
        └── jurisprudencia/         precedentes localizados e classificados
```

A pasta do caso e nomeada `<parte atendida>-x-<parte adversa>` em slug kebab-case (ex.: `joao-silva-x-construtora-alfa`).

## 2. ABERTURA DE CASO NOVO

1. Definir o slug do caso a partir das partes.
2. Criar `casos/<slug>/` com as subpastas `documentos/`, `pecas/`, `jurisprudencia/`.
3. Gerar o `CASO.md` a partir de `templates/CASO.md.tpl`, preenchendo polo, partes, dados do contrato, fase, marco intertemporal.
4. Gerar o `MEMORY.md` do caso a partir de `templates/MEMORY-caso.md.tpl`.
5. Registrar a abertura na linha do tempo do `MEMORY.md`.

## 3. RETOMADA DE CASO EXISTENTE

1. Localizar a pasta do caso.
2. Ler o `CASO.md` (estado, polo, linha estrategica, prazos) e o `MEMORY.md` (log evolutivo).
3. Apresentar ao operador um resumo: polo, fase, ultima etapa concluida, pendencias, prazos.
4. Retomar de onde parou.

## 4. O CASO.md — FONTE UNICA DO POLO

O `CASO.md` e a **fonte unica da variavel de polo**. Todas as skills leem dali o campo `Polo do cliente`. A `memoria-de-caso-trabalhista` mantem o `CASO.md` atualizado: polo, partes, dados do contrato, fase processual, linha estrategica (apos o Checkpoint 4), prazos, documentos.

Se o `CASO.md` nao tiver o polo definido, nenhuma skill produtora avanca (PA-05).

## 5. O MEMORY.md DO CASO — LOG EVOLUTIVO

A cada etapa do pipeline, registrar no `MEMORY.md` do caso:
- **Linha do tempo** — data + etapa + resultado (triagem, auditoria, trilateral, jurisprudencia, linha estrategica, peca produzida, auditoria R1-R4).
- **Decisoes estrategicas** — a tese central e as subsidiarias validadas no Checkpoint 4.
- **Pendencias e Pontos de Omissao** — documentos faltantes, prazos a confirmar.
- **Pecas produzidas** — cada peca com data e veredito da Suprema Corte.

Anotacoes manuais do operador ("lembre disso", "anote") tambem entram no `MEMORY.md` do caso.

## 6. COMPARTIMENTACAO (PA-22)

- Cada caso vive **so na sua pasta**. Nenhuma skill le ou cita dados de outro caso.
- O `MEMORY.md` de um caso cobre **apenas aquele caso**.
- Pasta de caso e LGPD-sensivel: `trabalhista/` (e `casos/`) e gitignored por default.
- Se o workspace estiver em pasta sincronizada (iCloud/OneDrive/Dropbox/Drive), emitir warning.

## 7. PRAZOS NO CASO.md

Manter a tabela de prazos do `CASO.md` atualizada. Para prazos recursais, cravar conforme o Protocolo 7 (RO/RR/AIRR/Agravo de Peticao 8 dias uteis; Embargos de Declaracao 5 dias uteis; RE/ARE 15 dias uteis) com termo inicial e vencimento.

## 8. VEDACOES ESPECIFICAS

- **PA-22** — jamais misturar informacao de casos diferentes.
- **PA-05** — manter o campo `Polo do cliente` sempre preenchido e consistente.
- Nunca gravar a pasta de caso fora de `<cwd>/trabalhista/casos/`.
- Nunca commitar dados de caso (a pasta e gitignored — confirmar).

## 9. INTEGRACAO

Acionada por: `triagem-trabalhista` (abertura/retomada), `/caso-trabalhista`, e todas as skills ao registrar evolucao. Provê o `CASO.md` para todas as demais skills. O `/status-trabalhista` le o `CASO.md` que esta skill mantem.
