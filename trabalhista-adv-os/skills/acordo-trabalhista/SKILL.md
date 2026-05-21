---
name: acordo-trabalhista
description: >
  ACORDO TRABALHISTA — Skill Tier 2 transversal. Calcula e redige acordos trabalhistas judiciais e extrajudiciais, inclusive via Comissao de Conciliacao Previa (CCP) e acordo extrajudicial homologado. Use quando menciona acordo trabalhista, conciliacao, proposta de acordo, CCP, acordo extrajudicial.
---

# ACORDO TRABALHISTA

> Skill **Tier 2**, transversal. Estrutura, calcula e redige acordos trabalhistas — judiciais e extrajudiciais. Serve aos dois polos: avalia a proposta e protege o interesse do cliente na transacao.

---

## 0. ESCOPO E ACIONAMENTO

Acionada quando ha conciliacao em vista — em audiencia, antes do ajuizamento, ou para encerrar o processo. Tambem pelo operador que pede "acordo", "proposta de conciliacao", "CCP".

## 1. SIDE-AWARENESS

Leia o `Polo do cliente` no `CASO.md`:
- Cliente = **reclamante** -> avaliar se o valor proposto e adequado frente ao que se postula e ao prognostico; nao aceitar quitacao ampla por valor vil.
- Cliente = **reclamada** -> estruturar o acordo que encerra o risco pelo menor custo, com a quitacao mais ampla e segura possivel.

A skill serve ao polo do cliente (PA-05).

## 2. MODALIDADES DE ACORDO

| Modalidade | O que e |
|------------|---------|
| **Acordo judicial** | celebrado nos autos da RT, homologado pelo juizo; extingue o processo com resolucao de merito |
| **Acordo extrajudicial homologado** | art. 855-B a 855-E CLT (pos-Reforma) — peticao conjunta de empregado e empregador, com advogados distintos, para homologacao judicial |
| **Comissao de Conciliacao Previa (CCP)** | art. 625-A e ss. CLT — conciliacao previa ao processo; o termo de conciliacao tem eficacia liberatoria geral, salvo ressalva expressa |

## 3. CALCULO DA PROPOSTA

Antes de qualquer acordo, calcular (apoio da `calculos-trabalhistas`):
- o **valor postulado/devido** conforme os pedidos e a prova;
- o **prognostico** — chance de exito por pedido (apoio da linha estrategica);
- a **faixa de acordo** — o intervalo racional entre o piso (reclamante) e o teto (reclamada), ponderando risco, tempo e custo (deposito recursal, honorarios, juros que correm).

Apresentar ao operador a faixa fundamentada — nunca um numero sem memoria (PA-20).

## 4. REDACAO DO ACORDO — CLAUSULAS

O termo de acordo deve definir com clareza:
- **valor** total e forma de pagamento (a vista / parcelado; consequencia da inadimplencia);
- **natureza das parcelas** — discriminar parcelas indenizatorias e remuneratorias (impacta INSS e IR; o juizo e a Receita conferem);
- **objeto da quitacao** — o que esta sendo quitado. Atencao: definir se a quitacao e do **objeto do processo** ou do **extinto contrato de trabalho** (quitacao ampla) — a redacao da clausula de quitacao e o ponto mais sensivel e serve de modo oposto a cada polo;
- **obrigacoes acessorias** — baixa na CTPS, liberacao de FGTS/guias, levantamento de depositos;
- **honorarios e custas** — quem arca.

## 5. CUIDADOS

- A homologacao do acordo extrajudicial exige **advogados distintos** para empregado e empregador (art. 855-B CLT) — nao ha como o mesmo advogado representar os dois.
- O juizo pode recusar a homologacao se vislumbrar fraude ou prejuizo a direito indisponivel.
- O acordo e transacao — uma vez homologado, faz coisa julgada nos limites do que foi pactuado.

## 6. VEDACOES ESPECIFICAS

- **PA-05** — a estrategia de acordo serve ao polo do cliente; clausula de quitacao redigida conforme o interesse do cliente.
- **PA-20** — a faixa de acordo vem de calculo com dado-base.
- **PA-21** — nao prometer a homologacao nem o resultado; apresentar prognostico.
- **PA-06** — o termo de acordo e um artefato; a comunicacao ao cliente sobre o acordo e outro.
- Nao representar os dois polos no mesmo acordo (art. 855-B CLT).

## 7. INTEGRACAO

Acionada por: `trabalhista-master`, `audiencia-trabalhista` (conciliacao em audiencia). Apoio: `calculos-trabalhistas`, `linha-estrategica-trabalhista` (prognostico), `estilo-juridico-trabalhista`. Entrega para: `suprema-corte-trabalhista` (R1-R4).
