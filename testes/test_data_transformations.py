# -*- coding: utf-8 -*-
import pandas as pd
import pytest

from src.data_transformations import preprocess_dataframe, generate_aggregation

def test_preprocess_dataframe():
    df_raw = pd.DataFrame({
        "DATA_INICIO": ["02-09-2016 10:54", "02-09-2016 11:43"],
        "CATEGORIA": [" pessoal ", "Negocio"],
        "PROPOSITO": [None, " reunião  "],
        "DISTANCIA": [53, 3]
    })

    df_proc = preprocess_dataframe(df_raw)

    assert "DT_REFE" in df_proc.columns
    assert df_proc.loc[0, "PROPOSITO"] == "Indefinido"
    assert df_proc.loc[1, "PROPOSITO"] == "Reunião"
    assert df_proc.loc[0, "CATEGORIA"] == "Pessoal"
    assert df_proc.loc[1, "CATEGORIA"] == "Negocio"

def test_generate_aggregation():
    df_proc = pd.DataFrame({
        "DATA_INICIO": pd.to_datetime(["02-09-2016 10:54", "02-09-2016 11:43", "02-09-2016 14:00"]),
        "DT_REFE": ["2016-02-09", "2016-02-09", "2016-02-09"],
        "CATEGORIA": ["Pessoal", "Negocio", "Negocio"],
        "PROPOSITO": ["Indefinido", "Reunião", "Cliente"],
        "DISTANCIA": [53, 3, 10]
    })

    df_agg = generate_aggregation(df_proc)

    assert df_agg.shape[0] == 1  # só uma data
    row = df_agg.iloc[0]

    assert row["QT_CORR"] == 3
    assert row["QT_CORR_NEG"] == 2
    assert row["QT_CORR_PESS"] == 1
    assert row["QT_CORR_REUNI"] == 1
    assert row["QT_CORR_NAO_REUNI"] == 1  # apenas o "Cliente" conta
    assert row["VL_MAX_DIST"] == 53
    assert row["VL_MIN_DIST"] == 3
    assert row["VL_AVG_DIST"] == round((53 + 3 + 10) / 3, 1)
