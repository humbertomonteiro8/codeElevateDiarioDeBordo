# 📘 Diário de Bordo – CodeElevate

Este projeto tem como objetivo processar dados de um aplicativo de transporte privado e gerar uma tabela agregada com informações consolidadas sobre as corridas, aplicando a **Arquitetura Medalhão** como estrutura de dados.

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

## 🧰 Estrutura do Projeto

codeElevateDiarioDeBordo/
│
├── data/
│ ├── raw/ # Camada Bronze
│ ├── processed/ # Camada Silver
│ └── gold/ # Camada Gold
│
├── src/ # Scripts principais
│ ├── data_loader.py
│ ├── data_transformations.py
│ ├── process_execution.py
│ └── utils.py
│
├── main.py # Script de execução
├── requirements.txt
└── README.md # Você está aqui


---

## 🚀 Execução

### Requisitos
- Python 3.9+
- Oracle Database XE configurado localmente (ou adaptado)
- Instale os pacotes:
```bash
pip install -r requirements.txt

```bash
python main.py

Esse comando irá:

    1.Carregar os dados da camada bronze.

    2.Realizar o tratamento e salvar como silver.

    3.Agregar os dados e salvar na camada gold.

    4.Inserir os dados agregados no banco Oracle.

✅ Testes
Os testes automatizados estão no diretório testes/ e cobrem os módulos de carregamento, transformação e execução do pipeline.

