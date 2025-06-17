# -*- coding: utf-8 -*-
import logging
from sqlalchemy import create_engine, text
import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

def oracle_connection():
    return create_engine(
        "oracle+oracledb://SYSTEM:SuperPassword@localhost:1521/?service_name=XEPDB1"
    )

def save_to_oracle(
    df,
    table_name,
    dtype_mapping,
    if_exists='replace',
    date_cols=None
):
    if df is None or df.empty:
        logger.info("Nenhum dado para salvar na tabela %s.", table_name)
        return

    engine = oracle_connection()

    if date_cols:
        for col in date_cols:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col])

    try:
        if if_exists == 'replace':
            with engine.connect() as conn:
                try:
                    conn.execute(text(f"DROP TABLE {table_name}"))
                    logger.info(
                        "Tabela %s dropada com sucesso antes da recriação.",
                        table_name
                    )
                except Exception as drop_err:
                    logger.warning(
                        "Não foi possível dropar tabela %s (provavelmente não existe): %s",
                        table_name, drop_err
                    )

        df.to_sql(
            name=table_name,
            con=engine,
            index=False,
            if_exists='append' if if_exists == 'replace' else if_exists,
            dtype=dtype_mapping
        )
        logger.info("Tabela %s salva no Oracle com sucesso.", table_name)

        if table_name == 'INFO_CORRIDAS_DO_DIA':
            with engine.connect() as conn:
                result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
                logger.info(
                    "Registros encontrados no Oracle em %s: %s",
                    table_name, result.scalar()
                )

    except Exception as exc:
        logger.error(
            "Erro ao salvar dados na tabela %s: %s",
            table_name, exc
        )