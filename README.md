# 📊 Diário de Bordo - Análise de Corridas de Transporte Privado

Este projeto tem como objetivo processar e analisar dados de um aplicativo de transporte privado, fornecendo insights sobre o uso diário do serviço. Através de transformações e agregações dos dados, buscamos entender padrões de uso, categorias de corridas e propósitos dos deslocamentos aplicando a **Arquitetura Medalhão** como estrutura de dados.

---

## 📌 Índice

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Estrutura de Diretórios](#estrutura-de-diretórios)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Como Rodar o Projeto](#como-rodar-o-projeto)
5. [Testes](#testes)
6. [Licença](#licença)
7. [Contribuições](#contribuições)
8. [Autores](#autores)

---

## 📝 Sobre o Projeto

O projeto visa gerar uma tabela agregada chamada `info_corridas_do_dia`, que contém informações diárias sobre as corridas realizadas, incluindo:

- Quantidade total de corridas
- Quantidade de corridas por categoria (Negócio e Pessoal)
- Distâncias máximas, mínimas e médias percorridas
- Quantidade de corridas com o propósito de "Reunião" e outras finalidades

A análise é realizada a partir de um arquivo CSV contendo os dados brutos das corridas, com as seguintes colunas:

- `DATA_INICIO`: Data e hora de início da corrida
- `DATA_FIM`: Data e hora de término da corrida
- `CATEGORIA`: Categoria da corrida (Negócio ou Pessoal)
- `LOCAL_INICIO`: Local de início da corrida
- `LOCAL_FIM`: Local de término da corrida
- `PROPOSITO`: Propósito da corrida
- `DISTANCIA`: Distância percorrida na corrida

---

## 📂 Estrutura de Diretórios

📦 codeElevateDiarioDeBordo
├── 📁 data
│ ├── 📁 raw
│ ├── 📁 processed
│ └── 📁 gold
├── 📁 docker-oracle
├── 📁 src
│ ├── 📄 data_loader.py
│ ├── 📄 data_transformations.py
│ ├── 📄 process_execution.py
│ └── 📄 utils.py
├── 📁 testes
│ ├── 📄 test_data_loader.py
│ ├── 📄 test_data_transformations.py
│ └── 📄 test_process_execution.py
├── 📄 main.py
├── 📄 README.md
└── 📄 requirements.txt

---

## 🏗️ Arquitetura Medalhão

O projeto segue a abordagem **Medallion Architecture**, dividida em três camadas:

### 🥉 Bronze (Camada Bruta)
- Dados originais, sem tratamento.
- **Local**: `data/raw/info_transportes.csv`
- **Ação**: Apenas leitura do CSV com os dados das corridas.

### 🥈 Silver (Camada Processada)
- Dados limpos, padronizados e prontos para agregação.
- **Local**: `data/processed/info_transportes_clean.csv`
- **Ação**: Tratamento de datas, remoção de nulos, padronização de strings.

### 🥇 Gold (Camada de Negócio)
- Dados agregados prontos para análise e consumo.
- **Local**: `data/gold/info_corridas_do_dia.csv`
- **Ação**: Agrupamento por data com métricas de negócio.

---

## 🧪 Exemplo da Tabela Final (`info_corridas_do_dia`)

| DT_REFE    | QT_CORR | QT_CORR_NEG | QT_CORR_PESS | VL_MAX_DIST | VL_MIN_DIST | VL_AVG_DIST | QT_CORR_REUNI | QT_CORR_NAO_REUNI |
|------------|---------|-------------|--------------|-------------|-------------|-------------|----------------|--------------------|
| 2022-01-01 | 20      | 12          | 8            | 2.2         | 0.7         | 1.1         | 6              | 10                 |

---


## 🚀 Execução

### Pré-requisitos

- Python 3.8 ou superior
- Docker (opcional, para ambiente isolado)
- Oracle Database (configurado conforme necessidade)

### Instalação / Configuração

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/codeElevateDiarioDeBordo.git
   cd codeElevateDiarioDeBordo

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt

3. (Opcional) Configure o Docker para executar o Oracle Database.
   ```bash
   cd docker-oracle
   docker compose up -d

### Execução do projeto
1. Para processar os dados e gerar a tabela agregada:
    ```bash
    python main.py

✅ Testes
1. Os testes estão localizados na pasta testes e podem ser executados utilizando o pytest:
    ```bash
    pytest testes/

👨‍💻 Autor
Humberto Monteiro da Cruz - Desenvolvedor Principal - [humbertomonteiro8](https://github.com/humbertomonteiro8)

