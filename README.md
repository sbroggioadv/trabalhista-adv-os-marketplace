# trabalhista-adv-os — marketplace

Marketplace oficial do plugin **`trabalhista-adv-os`** — assistente Claude Code especializado em **Direito e Processo do Trabalho brasileiro**.

O plugin cobre o ciclo completo de um caso trabalhista — da análise dos documentos do cliente à peça final auditada — e atende **os dois polos** da Reclamação Trabalhista:

- **Reclamante** — o advogado do trabalhador que ajuíza a ação contra a empresa.
- **Reclamada** — o advogado da empresa ou tomador de serviços que se defende.

---

## O que o plugin faz

- **Orquestrador side-aware** — pergunta o polo do cliente na triagem e adapta toda a estratégia, as teses e as peças a partir dele.
- **Triagem trilateral** — analisa o caso por três prismas: Cliente, Parte adversa e Juiz.
- **Auditoria de documentos** — lê cartão de ponto, holerites, CTPS, contrato de trabalho, TRCT, laudos e CCT/ACT, e mapeia os fatos em defesas ou causas de pedir.
- **32 skills em 4 tiers** — petição inicial, contestação, réplica, recursos (RO, RR, AIRR, agravos, embargos de declaração, embargos no TST, recurso extraordinário), ações autônomas de impugnação, perícia, cálculos, liquidação/execução, audiência, acordos, medidas disciplinares e contratos preventivos.
- **Suprema Corte R1-R4** — auditoria obrigatória de 4 etapas sobre todo documento antes da entrega.
- **Busca viva de jurisprudência** — TST, TRTs e demais portais, com classificação por nível de confirmação.
- **Memória de caso** persistente e compartimentada, pasta por caso (`<cliente>-x-<adverso>`).
- **Constituição operacional** — 4 Camadas, 25 Proibições Absolutas, 7 Protocolos Técnicos.

---

## Instalação (Claude Cowork)

1. Abra o **Cowork** → **Settings** → **Plugins**.
2. Na aba **Pessoal**, clique no botão **"+"** → **Uploads locais**.
3. Cole a URL deste repositório.
4. Sincronize e instale o plugin **`trabalhista-adv-os`**.
5. Rode **`/start-trabalhista`** para o onboarding e configuração do seu escritório.

---

## Conteúdo

Este marketplace publica **1 plugin**:

| Plugin | Pasta | Descrição |
|--------|-------|-----------|
| `trabalhista-adv-os` | [`./trabalhista-adv-os`](./trabalhista-adv-os) | 32 skills · 11 commands · 4 hooks |

---

## Licença

Código sob licença **MIT** — ver [`LICENSE`](./LICENSE). Os termos de licenciamento de uso comercial seguem o pacote adquirido.

---

Família **IA Combativa Adv-OS** — plugins jurídicos para Claude Code.
