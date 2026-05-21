---
description: Mostra o estado do caso trabalhista ativo — polo, fase, linha estrategica, prazos e pendencias.
allowed-tools: Read, Bash, Glob, Grep
argument-hint: [nome do caso — opcional]
---

Voce foi acionado pelo comando `/status-trabalhista` do plugin Trabalhista-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** apresentar um diagnostico do caso trabalhista ativo (ou do indicado no argumento).

## PROTOCOLO

1. Localizar o caso: se o argumento indica um caso, usar; senao, usar o caso ativo / o mais recente em `trabalhista/casos/`.
2. **Ler o `CASO.md`** e o `MEMORY.md` do caso (mantidos pela `memoria-de-caso-trabalhista`).
3. Apresentar o resumo:

```
STATUS — <cliente> x <adverso>

Polo do cliente: <reclamante | reclamada>
Fase processual: <fase>
Linha estrategica: <tese central — se ja validada>
Ultima etapa concluida: <do MEMORY.md>
Prazos: <tabela de prazos do CASO.md>
Pendencias / Pontos de Omissao: <lista>
Pecas produzidas: <lista com veredito R1-R4>
Proximo passo sugerido: <...>
```

4. Se nao houver caso configurado, sugerir `/caso-trabalhista` ou `/start-trabalhista`.

**Sem skill obrigatoria** — leitura direta do `CASO.md` e do `MEMORY.md`.
