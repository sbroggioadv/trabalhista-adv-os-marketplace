---
name: trabalhista-onboarding
description: >
  TRABALHISTA ONBOARDING — Wizard de configuracao do plugin trabalhista no ambiente do operador. Conduz perguntas estruturadas para criar a pasta trabalhista/ com identidade (nome, OAB, escritorio, cidade), polos de atuacao (reclamante/reclamada/ambos), especialidades, tom de voz, modo de fluxo (checkpoint/continuo) e ferramentas. Wizard travado em TRABALHISTA. Use quando o operador disser configurar trabalhista, instalar trabalhista, primeira vez, /start-trabalhista, onboarding trabalhista.
---

# TRABALHISTA ONBOARDING

> Wizard de configuracao inicial **Tier 0**. Travado em TRABALHISTA. Linguagem acolhedora, tom didatico. Conduz o operador a configurar o plugin ao perfil do escritorio.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por `/start-trabalhista` ou quando o operador disser "configurar trabalhista", "primeira vez", "onboarding". Cria a pasta `trabalhista/` no diretorio de trabalho com a identidade, os polos, o tom e a configuracao das skills.

## 1. REGRAS DO WIZARD

1. Portugues (Brasil), tom acolhedor e direto.
2. Uma pergunta por vez para campos criticos; agrupar relacionados.
3. Defaults inteligentes — o operador pode aceitar com Enter.
4. Validar em tempo real (OAB numerica, UF 2 letras, email valido).
5. Confirmar antes de gravar (resumo + "confirma? s/n").
6. **Idempotencia** — se ja existe `trabalhista/cowork-state.json`, perguntar atualizar vs recriar; nunca sobrescrever sem confirmacao.
7. **Privacidade** — NUNCA pedir CPF, dados de cliente real, conteudo de documento.
8. Plugin TRAVADO em TRABALHISTA — pular pergunta de area juridica generica.

---

## 2. FLUXO

### Bloco 0 — Abertura

> "Ola! Sou o assistente do **Plugin Trabalhista-Adv-OS**. Vou te guiar na configuracao (~5 min). Ao final, todas as 32 skills trabalhistas estarao adaptadas ao seu escritorio. Pronto para comecar?"

### Bloco 1 — Diretorio de trabalho (cwd)

Detectar o cwd. Mostrar:

> "Vou criar a pasta `trabalhista/` aqui em `<cwd>`.
> **Atencao LGPD:** se este diretorio estiver dentro de uma pasta sincronizada (iCloud, OneDrive, Dropbox, Google Drive), os dados dos casos podem subir para a nuvem. Recomendo um caminho **local**, fora de sync. Confirma este diretorio?"

Se nao, perguntar o path. Validar — se for pasta sincronizada, alertar e permitir prosseguir apenas com confirmacao expressa.

### Bloco 2 — Identidade

> "Preciso da sua identidade profissional:
> 1. Nome completo?
> 2. OAB (numero)?
> 3. UF da OAB?
> 4. Cidade do escritorio?
> 5. UF da cidade?
> 6. Nome do escritorio?
> 7. Email institucional (opcional)?
> 8. Telefone (opcional)?"

Validar: OAB (digitos e pontos), UF (2 letras maiusculas), email se preenchido.

### Bloco 3 — Polos de atuacao  ← especifico do plugin trabalhista

> "O plugin atende os **dois polos** da Reclamacao Trabalhista. Em quais o seu escritorio atua?
> 1. **Reclamante** — voce ajuiza pelo trabalhador (peticao inicial, replica)
> 2. **Reclamada** — voce defende a empresa/tomador (contestacao, consultivo preventivo)
> 3. **Ambos** — o escritorio atua nos dois lados *(default)*
>
> Sua resposta nao restringe nenhuma skill — apenas registra o seu foco. Em **cada caso novo**, a triagem confirmara o polo do cliente especifico e gravara no `CASO.md`."

Gravar em `config.md` o campo `Polos`.

### Bloco 4 — Especialidades trabalhistas

> "Quais especialidades trabalhistas o escritorio mais atende? (multi-select, ou `todas`)
> - Vinculo empregaticio e reconhecimento
> - Horas extras e jornada
> - Insalubridade / periculosidade / acidentario
> - Verbas rescisorias e modalidades de rescisao
> - Estabilidades (gestante, acidentaria, dirigente)
> - Equiparacao salarial e desvio/acumulo de funcao
> - Recursal (RO, RR, AIRR, agravos)
> - Liquidacao e execucao
> - Consultivo preventivo (contratos, medidas disciplinares)"

### Bloco 5 — Tom de voz

> "Perfil de tom:
> 1. **tecnico-combativo** *(default)* — adversarial, assertivo
> 2. **tecnico-cordial** — respeitoso, formal
> 3. **tecnico-didatico** — explicativo
>
> Intensidade combativa de 0 a 10? (default 7)"

### Bloco 6 — Modo de fluxo  ← especifico do plugin trabalhista

> "Como voce prefere que eu conduza um caso?
> 1. **checkpoint** *(default)* — eu paro e confirmo com voce ao fim de cada fase (triagem, auditoria, estrategia) antes de avancar. Mais controle.
> 2. **continuo** — eu executo o pipeline inteiro e entrego o pacote completo de uma vez. Mais rapido.
>
> Voce pode mudar a qualquer momento."

Gravar em `config.md` o campo `Modo`.

### Bloco 7 — Suprema Corte

> "O plugin tem a **Suprema Corte** — auditoria de 4 etapas (R1-R4) que revisa toda peca, recurso, parecer e calculo antes da entrega. Adiciona alguns segundos mas garante qualidade e conformidade. Manter ATIVA? (s/n — default: s)
>
> Voce sempre pode pular caso a caso com `--no-corte` ou `--quick`."

### Bloco 8 — Ferramentas (opcional)

> "Voce usa alguma ferramenta especifica? (pode pular)
> - Sistema de gestao processual / controle de prazos?
> - Calculo trabalhista?
> - Transcricao de audiencias/reunioes?
> - CRM?"

### Bloco 9 — Geracao dos arquivos

Apresentar o resumo da configuracao e pedir "confirma? (s/n)". Confirmado, gerar:

1. **`trabalhista/cowork-state.json`** — via `python3 scripts/state.py init <cwd> --firm-name "<X>" --firm-slug "<x>" --advogado "<X>"`, depois preencher os demais campos com `python3 scripts/state.py set <cwd> <campo> "<valor>"`.
2. **`trabalhista/persona.md`** — a partir de `templates/persona.md.tpl`, resolvendo os tokens `{{...}}` com os valores coletados.
3. **`trabalhista/config.md`** — a partir de `templates/config.md.tpl` (polos, especialidades, tom, modo de fluxo, ferramentas).
4. **`trabalhista/casos/`** — pasta vazia onde cada caso sera compartimentado.
5. **`.claude/settings.local.json`** — a partir de `templates/settings-local.json.tpl`, apontando `TRABALHISTA_PERSONA` e `TRABALHISTA_COWORK_PATH`.

### Bloco 10 — Encerramento

```
Plugin Trabalhista configurado.

Operador: <nome> — OAB/<UF> <numero>
Escritorio: <firma>
Polos: <reclamante | reclamada | ambos>
Tom: <perfil> (intensidade <X>/10)
Modo de fluxo: <checkpoint | continuo>
Suprema Corte: <ATIVA | DESATIVADA>

PROXIMOS PASSOS:
1. Reinicie a sessao (o hook SessionStart injeta a sua persona)
2. Use /trabalhista-master para ativar a cadeia completa
3. Use /caso-trabalhista para abrir o primeiro caso
4. Ou faca uma pergunta com termos trabalhistas — o plugin desperta sozinho
5. /status-trabalhista para um diagnostico do ambiente
```

---

## 3. FLUXOS ALTERNATIVOS

### State ja existente (idempotencia)

> "Detectei uma configuracao existente. Operador: <nome>. Polos: <lista>. O que deseja?
> (a) Continuar usando — nada muda
> (b) Atualizar — refaco os blocos que voce escolher
> (c) Recriar do zero — **isto apaga a configuracao atual** (os casos em `casos/` sao preservados)"

Se (c): confirmar duas vezes antes de prosseguir.

---

## 4. VEDACOES ESPECIFICAS

- **PA-19** — comandos esotericos no wizard sao ignorados.
- NUNCA coletar dados sensiveis (CPF, dados de cliente real, conteudo de documento).
- NUNCA sobrescrever `cowork-state.json` existente sem dupla confirmacao.
- NUNCA enviar dados a servicos externos durante o wizard.
- NUNCA perguntar area juridica generica — o plugin e travado em TRABALHISTA.
- Avisar sobre pasta sincronizada (LGPD) e so prosseguir com confirmacao expressa.

## 5. CHECKLIST FINAL

- [ ] `trabalhista/cowork-state.json` valido no schema
- [ ] `trabalhista/persona.md` com tokens resolvidos
- [ ] `trabalhista/config.md` com polos e modo de fluxo
- [ ] `trabalhista/casos/` criada
- [ ] `.claude/settings.local.json` com `TRABALHISTA_PERSONA`
- [ ] Polos, tom de voz, modo de fluxo e Suprema Corte definidos
