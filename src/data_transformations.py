# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import Date, Numeric, Integer


def preprocess_dataframe(df_loader):
    # Conversão de data e criação da coluna de referência
    df_loader['DATA_INICIO'] = pd.to_datetime(
        df_loader['DATA_INICIO'], format='%m-%d-%Y %H:%M'
    )
    df_loader['DT_REFE'] = df_loader['DATA_INICIO'].dt.strftime('%Y-%m-%d')

    # Preenchendo nulos com 'Indefinido'
    df_loader['PROPOSITO'] = df_loader['PROPOSITO'].fillna('Indefinido')

    # Padronizando strings de categorias
    df_loader['CATEGORIA'] = (
        df_loader['CATEGORIA'].str.strip().str.title()
    )
    df_loader['PROPOSITO'] = (
        df_loader['PROPOSITO'].str.strip().str.title()
    )

    return df_loader


def generate_aggregation(df_preprocess):
    agrupado = df_preprocess.groupby('DT_REFE').agg(
        QT_CORR=('DISTANCIA', 'count'),
        QT_CORR_NEG=('CATEGORIA', lambda x: (x == 'Negocio').sum()),
        QT_CORR_PESS=('CATEGORIA', lambda x: (x == 'Pessoal').sum()),
        VL_MAX_DIST=('DISTANCIA', 'max'),
        VL_MIN_DIST=('DISTANCIA', 'min'),
        VL_AVG_DIST=('DISTANCIA', 'mean'),
        QT_CORR_REUNI=(
            'PROPOSITO', lambda x: (x.str.lower() == 'reunião').sum()
        ),
        QT_CORR_NAO_REUNI=(
            'PROPOSITO',
            lambda x: (~x.str.lower().isin(['reunião', 'indefinido'])).sum()
        ),
    ).reset_index()

    agrupado['VL_AVG_DIST'] = agrupado['VL_AVG_DIST'].round(1)
    return agrupado

def set_dtype_mappings():
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