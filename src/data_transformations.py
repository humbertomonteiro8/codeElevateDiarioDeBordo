# -*- coding: utf-8 -*-
import logging
import pandas as pd
from sqlalchemy import Date, Numeric, Integer, String, Float

# Configuração básica do logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)


def preprocess_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Iniciando pré-processamento do DataFrame.")
    df['DATA_INICIO'] = pd.to_datetime(df['DATA_INICIO'], format='%m-%d-%Y %H:%M')
    df['DT_REFE'] = df['DATA_INICIO'].dt.strftime('%Y-%m-%d')

    df['PROPOSITO'] = df['PROPOSITO'].fillna('Indefinido')
    df['CATEGORIA'] = df['CATEGORIA'].str.strip().str.title()
    df['PROPOSITO'] = df['PROPOSITO'].str.strip().str.title()

    logger.info("Pré-processamento concluído.")
    return df


def normalize_text(s: pd.Series) -> pd.Series:
    logger.debug("Normalizando texto.")
    return (
        s.str.normalize('NFKD')
        .str.encode('ascii', errors='ignore')
        .str.decode('utf-8')
        .str.lower()
    )


def generate_aggregation(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Gerando agregações.")
    df['PROP_NORM'] = normalize_text(df['PROPOSITO'])

    grouped = df.groupby('DT_REFE').agg(
        QT_CORR=('DISTANCIA', 'count'),
        QT_CORR_NEG=('CATEGORIA', lambda x: (x == 'Negocio').sum()),
        QT_CORR_PESS=('CATEGORIA', lambda x: (x == 'Pessoal').sum()),
        VL_MAX_DIST=('DISTANCIA', 'max'),
        VL_MIN_DIST=('DISTANCIA', 'min'),
        VL_AVG_DIST=('DISTANCIA', 'mean'),
        QT_CORR_REUNI=('PROP_NORM', lambda x: (x == 'reuniao').sum()),
        QT_CORR_NAO_REUNI=('PROP_NORM', lambda x: (~x.isin(['reuniao', 'indefinido'])).sum())
    ).reset_index()

    grouped['VL_AVG_DIST'] = grouped['VL_AVG_DIST'].round(1)
    logger.info("Agregações geradas com sucesso.")
    return grouped


def set_dtype_mappings():
    logger.debug("Definindo mapeamentos de tipos para gold.")
    return {
        'DT_REFE': Date(),
        'QT_CORR': Integer(),
        'QT_CORR_NEG': Integer(),
        'QT_CORR_PESS': Integer(),
        'VL_MAX_DIST': Numeric(10, 2),
        'VL_MIN_DIST': Numeric(10, 2),
        'VL_AVG_DIST': Numeric(10, 2),
        'QT_CORR_REUNI': Integer(),
        'QT_CORR_NAO_REUNI': Integer()
    }


def get_bronze_dtype_mappings():
    logger.debug("Definindo mapeamentos de tipos para bronze.")
    return {
        'DATA_INICIO': String(50),
        'DATA_FIM': String(50),
        'CATEGORIA': String(20),
        'LOCAL_INICIO': String(100),
        'LOCAL_FIM': String(100),
        'PROPOSITO': String(100),
        'DISTANCIA': Float()
    }


def get_silver_dtype_mappings():
    logger.debug("Definindo mapeamentos de tipos para silver.")
    return {
        'DATA_INICIO': Date(),
        'DATA_FIM': String(50),
        'CATEGORIA': String(20),
        'LOCAL_INICIO': String(100),
        'LOCAL_FIM': String(100),
        'PROPOSITO': String(100),
        'DISTANCIA': Float(),
        'DT_REFE': Date()
    }
