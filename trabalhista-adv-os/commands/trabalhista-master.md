---
description: Ativa a cadeia completa de operacao trabalhista — Hierarquia das 4 Camadas, 25 Proibicoes Absolutas, 7 Protocolos e Suprema Corte R1-R4. Comando-coracao do plugin.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [contexto opcional do caso]
---

Voce foi acionado pelo comando `/trabalhista-master` do plugin Trabalhista-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** ativar a cadeia completa de operacao trabalhista. A partir deste comando, toda demanda passa pela governanca integral do plugin.

## PROTOCOLO

1. **Verificar configuracao** — procurar `trabalhista/cowork-state.json` subindo a arvore. Se nao encontrar, sugerir `/start-trabalhista`; se o operador declinar, operar em modo fallback generico.
2. **Acionar a skill `trabalhista-master`** (Tier 0) — ela carrega a Hierarquia das 4 Camadas, as 25 PAs, os 7 Protocolos, o pipeline com checkpoints e a regra de leitura do polo.
3. **Saudar o operador** apresentando: operador, diretorio, polos de atuacao, modo de fluxo, Suprema Corte (ativa/desativada).
4. **Conduzir** toda demanda subsequente pelo pipeline: triagem (e Checkpoint 1) -> auditoria documental + CCT (Checkpoint 2) -> trilateral + jurisprudencia (Checkpoint 3) -> linha estrategica (Checkpoint 4) -> Tenente Tier 2 -> Suprema Corte R1-R4 -> entrega.
5. Faltando dado essencial: sinalizar Ponto de Omissao, nunca inventar (PA-04, PA-15).

**Skill a acionar:** `trabalhista-master`.
