# trabalhista-adv-os

> Plugin Claude Code especializado em **Direito e Processo do Trabalho brasileiro**.
> Cobre o ciclo completo de um caso trabalhista — da análise dos documentos do
> cliente à peça final auditada — para **os dois polos** da Reclamação Trabalhista.

---

## O que é

`trabalhista-adv-os` é um plugin profissional para advogados trabalhistas. Ele
diagnostica o caso, conduz por etapas com checkpoint, redige a peça nos termos da
legislação vigente (CLT + CPC subsidiário + CCT/ACT da categoria) e mantém memória
persistente caso a caso.

O plugin é **side-aware**: na entrada, a triagem pergunta se o cliente do
escritório é o **reclamante** (trabalhador que ajuíza) ou a **reclamada** (empresa
ou tomador que se defende). A resposta orienta toda a estratégia e a redação.

---

## Como funciona

- **Orquestrador side-aware** — a `trabalhista-master` carrega a Hierarquia das 4
  Camadas, faz cumprir as 25 Proibições Absolutas, aciona os 7 Protocolos Técnicos
  e garante a auditoria final R1-R4.
- **Pipeline com checkpoint** — triagem → auditoria documental + CCT → análise
  trilateral + jurisprudência → linha estratégica → peça → Suprema Corte. Em cada
  fase o plugin para e confirma com o advogado (modo `--continuo` disponível).
- **Memória de caso** — cada caso vive em `trabalhista/casos/<cliente>-x-<adverso>/`
  com sua ficha, log evolutivo, documentos, peças e jurisprudência. Pasta gitignored
  por padrão (LGPD).
- **Suprema Corte R1-R4** — toda peça passa por auditoria de 4 etapas antes da
  entrega: coleta de dados → base jurídica → tese → completude.

---

## As 32 skills

| Tier | Conteúdo |
|------|----------|
| **Tier 0** (2) | `trabalhista-master` (orquestrador sempre ativo) · `trabalhista-onboarding` (wizard de configuração) |
| **Tier 1** (8) | Estado-Maior transversal: triagem, análise trilateral, auditoria documental, linha estratégica, jurisprudência, CCT/normas coletivas, memória de caso, estilo jurídico |
| **Tier 2 — conhecimento** (3) | Petição inicial (reclamante), contestação (reclamada), réplica (reclamante) |
| **Tier 2 — recursal** (8) | Recurso Ordinário, Recurso de Revista/AIRR, Embargos no TST, Agravos, Embargos de Declaração, Recurso Extraordinário, ações autônomas de impugnação, pareceres de viabilidade recursal — cada um em **modo dual** (recurso + contrarrazão/contraminuta) |
| **Tier 2 — instrução/execução** (7) | Razões finais, perícia, quesitos/assistente técnico, audiência, cálculos, liquidação/execução, acordo |
| **Tier 2 — consultivo/preventivo** (3) | Medidas disciplinares, contratos preventivos, documentos extrajudiciais |
| **Tier 3** (1) | `suprema-corte-trabalhista` — auditoria final R1-R4 |

---

## Instalação

O plugin é distribuído via marketplace GitHub público. Para instalar no Cowork:

1. Abra **Settings → Plugins → aba Pessoal**.
2. Clique em **"+" Uploads locais**.
3. Cole a URL do repositório do marketplace.
4. Rode `/start-trabalhista` para configurar o plugin ao perfil do seu escritório.

---

## Commands

`/start-trabalhista` · `/trabalhista-master` · `/caso-trabalhista` ·
`/peticao-trabalhista` · `/contestacao-trabalhista` · `/recurso-trabalhista` ·
`/parecer-trabalhista` · `/calculo-trabalhista` · `/jurisprudencia-trabalhista` ·
`/revisao-trabalhista-final` · `/status-trabalhista`

---

## Privacidade

A pasta `trabalhista/` do seu workspace — onde vivem persona, configuração e os
casos — é gitignored por padrão. O plugin emite um aviso se o workspace estiver em
uma pasta sincronizada (iCloud/OneDrive/Dropbox/Drive). Nenhum dado de cliente é
enviado para fora do seu ambiente.

---

**Licença:** MIT · **Família:** IA Combativa Adv-OS
