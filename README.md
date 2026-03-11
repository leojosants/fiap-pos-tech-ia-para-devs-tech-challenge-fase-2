# 🏥 Logística 4.0: Otimização de Rotas Hospitalares com Algoritmo Genético e IA

Este projeto resolve o desafio complexo de distribuir insumos médicos em uma rede hospitalar, priorizando vidas através de uma **Hierarquia de Valor**.

## 🚀 Sobre o Projeto

Diferente de sistemas de logística tradicionais, este software utiliza um **Algoritmo Genético** para garantir que locais em estado **Crítico** 🚨 recebam atendimento prioritário, sacrificando a distância total em favor do tempo de resposta vital. Além disso, integra **Inteligência Artificial (LLM)** para traduzir dados técnicos em instruções claras para os motoristas.

## 📂 Estrutura do Projeto

```text
.
├── config/             # Configurações do algoritmo (taxas, frotas)
├── data/               # Dados de entrada e saída (JSON)
├── docs/               # Relatórios e documentação técnica
├── outputs/            # Mapas e resultados visuais
└── src/                # Código-fonte (AG, IA e Visualizador)
```

## ⚙️ Como Executar

Recomenda-se o uso de um ambiente virtual para manter as dependências isoladas.

- Prepare o Ambiente Virtual
  - No Windows:

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

  - No Linux/macOS:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  
    ```

- Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

- Execute o algoritmo principal:

    ```bash
    python src/tsp.py
    ```

- Gere o mapa final após a execução:

    ```bash
    python src/generate_map.py
    ```

## 🤖 Camada de Comunicação (IA)

- O projeto utiliza Modelos de Linguagem de Grande Escala (LLMs) como uma ferramenta de apoio operacional.

- Metodologia:
  - Os resultados gerados pelo algoritmo (JSON) são processados via prompting para converter coordenadas e dados técnicos em Boletins de Missão humanizados.
  - [Vide relatório](/docs/hospital_logistics_operation_report.md)

- Objetivo:
  - Garantir que a complexidade matemática da rota seja traduzida em instruções claras e urgentes para os motoristas, mantendo o foco no Protocolo de Emergência.

## 🗺️ Mapa de rotas

![image](/outputs/final_routes_map.png)
