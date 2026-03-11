# Relatório de Operação Logística Hospitalar

**Operação:** Distribuição Emergencial de Insumos Médicos  
**Base Operacional:** Hospital (Centro Logístico)  
**Frota Utilizada:** Moto_01, Van_01, Caminhao_01  
**Geração do Planejamento:** Algoritmo de Otimização de Rotas  
**Distância Total Otimizada:** 309.762.180,88 (unidades do modelo)

---

# 1. Resumo Executivo da Missão

Esta operação logística foi planejada para garantir a **distribuição eficiente de insumos médicos** a múltiplas unidades de saúde, respeitando dois princípios operacionais fundamentais:

1. **Prioridade absoluta para pontos críticos (🚨)** — locais com maior urgência de abastecimento.
2. **Otimização da eficiência logística** — minimização de deslocamentos improdutivos e melhor aproveitamento da frota.

A estratégia adotada consistiu em **segmentar a rota global entre três tipos de veículos**, cada um desempenhando uma função logística específica:

| Veículo | Função Operacional | Característica |
|---|---|---|
| Moto_01 | Resposta rápida | Alta mobilidade urbana |
| Van_01 | Distribuição intermediária | Equilíbrio entre capacidade e agilidade |
| Caminhao_01 | Transporte de maior volume | Cobertura de áreas mais distantes |

Os **pontos classificados como críticos receberam destaque pelo Protocolo de Emergência 🚨**, garantindo atendimento prioritário.

Para preservar a eficiência operacional, **paradas regulares foram estrategicamente inseridas entre atendimentos críticos**, evitando deslocamentos com capacidade ociosa e reduzindo custos logísticos totais.

---

# 2. Rotas Operacionais da Frota

---

# 2.1 Rota Operacional — Moto_01

**Perfil:** resposta rápida e mobilidade urbana elevada.

| Ordem | Local | Status |
|---|---|---|
| 1 | Hospital (Saída) | Base |
| 2 | Posto A | 🚨 Crítico |
| 3 | Centro M | Regular |
| 4 | Unidade O | 🚨 Crítico |
| 5 | Clinica J | Regular |
| 6 | Unidade E | 🚨 Crítico |
| 7 | Posto L | 🚨 Crítico |
| 8 | Centro F | Regular |
| 9 | Farmacia R | 🚨 Crítico |
| 10 | Posto S | Regular |
| 11 | Hospital (Retorno) | Base |

---

# 2.2 Rota Operacional — Van_01

**Perfil:** transporte intermediário com maior capacidade de carga.

| Ordem | Local | Status |
|---|---|---|
| 1 | Hospital (Saída) | Base |
| 2 | Posto A | 🚨 Crítico |
| 3 | Clinica B | Regular |
| 4 | Posto D | Regular |
| 5 | Farmacia C | 🚨 Crítico |
| 6 | Posto P | Regular |
| 7 | UPA I | 🚨 Crítico |
| 8 | Clinica Q | Regular |
| 9 | Lab G | Regular |
| 10 | Hospital (Retorno) | Base |

---

# 2.3 Rota Operacional — Caminhao_01

**Perfil:** transporte de maior volume e alcance.

| Ordem | Local | Status |
|---|---|---|
| 1 | Hospital (Saída) | Base |
| 2 | Posto A | 🚨 Crítico |
| 3 | Lab N | Regular |
| 4 | Posto L | 🚨 Crítico |
| 5 | Clinica B | Regular |
| 6 | Posto H | 🚨 Crítico |
| 7 | Farmacia K | Regular |
| 8 | Posto P | Regular |
| 9 | Hospital (Retorno) | Base |

---

# 3. Protocolo de Emergência (Itens Críticos 🚨)

Locais classificados como **Críticos** possuem prioridade operacional máxima.

Para cada parada crítica devem ser executados os seguintes procedimentos:

- Entrega imediata de insumos prioritários
- Confirmação de recebimento pela unidade
- Comunicação de status com a central logística
- Atualização de estoque emergencial

Esses pontos foram distribuídos na frota de forma a **reduzir o tempo médio de atendimento emergencial**.

---

# 4. Justificativa Técnica da Estratégia Logística

A estratégia utilizada equilibra **duas métricas fundamentais de logística hospitalar**:

1. **Tempo de resposta para emergências**
2. **Custo operacional da frota**

Para atingir esse equilíbrio foram aplicadas três decisões técnicas principais.

---

## 4.1 Priorização de Pontos Críticos

Locais classificados como **prioridade 10** foram inseridos como marcos estruturais da rota.

Esses pontos determinam:

- a ordem principal de deslocamento
- o eixo geográfico da missão
- a alocação do tipo de veículo mais adequado

Assim, os veículos foram distribuídos para que **nenhum ponto crítico fique concentrado em apenas um veículo**, reduzindo risco operacional.

---

## 4.2 Inserção Estratégica de Paradas Regulares

Paradas regulares foram intercaladas entre pontos críticos para:

- evitar deslocamentos com carga ociosa
- aproveitar proximidade geográfica
- manter o fluxo logístico contínuo

Isso reduz significativamente:

- quilometragem improdutiva
- consumo de combustível
- tempo de retorno da frota.

---

## 4.3 Especialização da Frota

Cada veículo foi designado para uma função específica:

**Moto_01**

- maior agilidade
- resposta rápida em áreas densas
- suporte emergencial urbano

**Van_01**

- distribuição equilibrada
- integração entre rotas críticas e regulares
- capacidade média de carga

**Caminhao_01**

- transporte de maior volume
- atendimento de regiões mais distantes
- abastecimento consolidado

---

# 5. Conclusão Operacional

A missão foi estruturada para garantir que:

- todos os **pontos críticos sejam atendidos com prioridade**
- a **capacidade da frota seja plenamente utilizada**
- o **custo logístico total seja minimizado**

A combinação de **priorização emergencial + otimização de rota** permite manter **alto nível de serviço hospitalar sem comprometer a eficiência operacional**.

Esse modelo de planejamento pode ser reutilizado para:

- operações de abastecimento hospitalar
- logística farmacêutica
- resposta a emergências médicas regionais.
