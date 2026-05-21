---
description: Inicia o wizard de configuracao do plugin trabalhista — cria a pasta trabalhista/ com identidade, polos de atuacao, tom e modo de fluxo.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [--update para reconfigurar]
---

Voce foi acionado pelo comando `/start-trabalhista` do plugin Trabalhista-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** configurar o plugin trabalhista no ambiente do operador.

## PROTOCOLO

1. **Acionar a skill `trabalhista-onboarding`** imediatamente — ela conduz o wizard completo.
2. O wizard cria `<cwd>/trabalhista/` com `persona.md`, `config.md`, `casos/` e o `cowork-state.json`, alem de `.claude/settings.local.json`.
3. Se ja existir `trabalhista/cowork-state.json`, a skill oferece continuar / atualizar / recriar (idempotencia).
4. Se o argumento for `--update`, ir direto para o fluxo de atualizacao.

**Atencao LGPD:** a skill avisa se o diretorio estiver em pasta sincronizada (iCloud/OneDrive/Dropbox/Drive).

**Skill a acionar:** `trabalhista-onboarding`.
