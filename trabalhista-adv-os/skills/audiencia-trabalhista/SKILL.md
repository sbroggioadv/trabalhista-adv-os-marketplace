---
name: audiencia-trabalhista
description: >
  AUDIENCIA TRABALHISTA — Skill Tier 2 transversal. Prepara a audiencia una/de instrucao: roteiro de depoimento pessoal, perguntas para testemunhas, pontos controvertidos, estrategia de acordo. Use quando menciona audiencia trabalhista, audiencia de instrucao, depoimento, testemunhas, preparar audiencia.
---

# AUDIENCIA TRABALHISTA

> Skill **Tier 2** de instrucao, transversal. Prepara a parte para a audiencia trabalhista — una ou de instrucao — e estrutura a ata pos-audiencia. Serve aos dois polos.

---

## 0. ESCOPO E ACIONAMENTO

Acionada antes da audiencia (preparacao) e depois (ata e proximos passos). Tambem pelo operador que pede "preparar audiencia", "roteiro de depoimento".

## 1. SIDE-AWARENESS

Leia o `Polo do cliente` no `CASO.md`. A preparacao serve ao polo:
- Cliente = **reclamante** -> roteiro que reforce as causas de pedir; perguntas que extraiam da prova oral a confirmacao dos fatos.
- Cliente = **reclamada** -> roteiro que reforce a defesa; perguntas que evidenciem a fragilidade da tese obreira.

## 2. A AUDIENCIA NO PROCESSO DO TRABALHO

- **Audiencia una** (rito sumarissimo e, na pratica, muitos casos do ordinario) — concentra conciliacao, defesa, instrucao e razoes finais.
- **Audiencia de instrucao** — quando ha fracionamento; colhe depoimentos e prova oral.
- **Ausencia das partes:** a ausencia do reclamante a audiencia importa arquivamento; a da reclamada importa **revelia e confissao ficta** (art. 844 CLT) — alerta critico.

## 3. PREPARACAO — ROTEIRO

### 3.1 Depoimento pessoal

Preparar a parte (reclamante ou preposto da reclamada) para o depoimento:
- alinhar a versao com a peca (inicial ou contestacao) — incoerencia gera confissao;
- antecipar as perguntas dificeis da parte adversa e do juizo;
- orientar postura: responder o perguntado, sem inventar, sem hostilidade.
- **Preposto** (reclamada): deve conhecer os fatos; suas declaracoes obrigam a empresa (Sumula 74 e art. 843 §1o CLT).

### 3.2 Perguntas as testemunhas

- Listar os pontos controvertidos a comprovar por prova oral.
- Para cada ponto, formular perguntas objetivas as proprias testemunhas.
- Preparar a **contradita** de testemunhas da parte adversa (suspeicao, amizade intima, interesse — art. 829 CLT).
- Antecipar as perguntas que se fara as testemunhas adversas.

### 3.3 Pontos controvertidos

Mapear, a partir da inicial e da contestacao, os fatos controvertidos — sao eles que a instrucao vai resolver e que orientam toda a prova oral.

## 4. ESTRATEGIA DE ACORDO

A audiencia e o momento natural da conciliacao. A skill avalia, conforme a linha estrategica e o prognostico, se ha espaco para acordo e em que faixa — acionando a `acordo-trabalhista` quando o operador decidir negociar.

## 5. ATA E POS-AUDIENCIA

Apos a audiencia, estruturar a ata/resumo: o que foi decidido, depoimentos colhidos (sintese), provas deferidas/indeferidas, proximos prazos (ex.: razoes finais, pericia). Registrar no `MEMORY.md` do caso.

## 6. VEDACOES ESPECIFICAS

- **PA-05** — a preparacao serve ao polo do cliente.
- **PA-06** — esta skill produz dois artefatos de escopos distintos — o **roteiro de preparacao** (uso interno/cliente) e a **ata/resumo pos-audiencia** (registro do caso). Nunca misturar os dois num so output: entregar artefatos separados, cada um no seu escopo (Protocolo 5).
- **PA-21** — nao prometer resultado da audiencia ao cliente.
- **PA-04** — orientar a parte a depor com verdade; nunca construir versao falsa.
- Alertar sempre sobre o risco de revelia/confissao por ausencia (art. 844 CLT).

## 7. INTEGRACAO

Acionada por: `trabalhista-master`. Apoio: `estilo-juridico-trabalhista`, `analise-trilateral-trabalhista` (pontos controvertidos). Aciona: `acordo-trabalhista` (se ha conciliacao). Alimenta: `razoes-finais-trabalhistas`. Entrega para: `suprema-corte-trabalhista` (R1-R4).
