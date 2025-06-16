# -*- coding: utf-8 -*-
import logging
import pandas as pd
from src.data_transformations import (
    preprocess_dataframe,
    generate_aggregation,
    set_dtype_mappings,
    get_bronze_dtype_mappings,
    get_silver_dtype_mappings,
)
from src.data_loader import load_data
from src.utils import save_to_oracle

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

def run(input_path: str, silver_path: str, output_path: str) -> None:
    """
    Executa o pipeline de ETL com base na arquitetura medalhão.
    """
    # CAMADA BRONZE: Leitura do dado bruto
    df_raw = load_data(input_path)

    # Salvar camada BRONZE no Oracle
    save_to_oracle(
        df_raw,
        table_name='INFO_TRANSPORTE_BRUTO',
        dtype_mapping=get_bronze_dtype_mappings(),
        if_exists='replace'
    )

    # CAMADA SILVER: Limpeza e transformação
    df_silver = preprocess_dataframe(df_raw)
    df_silver.to_csv(silver_path, index=False)
    logger.info("Silver data saved to %s", silver_path)

    # Salvar camada SILVER no Oracle
    save_to_oracle(
        df_silver,
        table_name='INFO_TRANSPORTE_LIMPO',
        dtype_mapping=get_silver_dtype_mappings(),
        if_exists='replace',
        date_cols=['DT_REFE']
    )

    # CAMADA GOLD: Agregações de negócio
    df_gold = generate_aggregation(df_silver)

    if df_gold is not None:
        df_gold.to_csv(output_path, index=False)
        logger.info("Gold data saved to %s", output_path)

        # Salvar camada GOLD no Oracle
        save_to_oracle(
            df_gold,
            table_name='INFO_CORRIDAS_DO_DIA',
            dtype_mapping=set_dtype_mappings(),
            if_exists='replace',
            date_cols=['DT_REFE']
        )
    else:
        logger.error("Falha no processamento. Nenhum dado gerado.")
