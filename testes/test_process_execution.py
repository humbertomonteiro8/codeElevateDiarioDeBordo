# -*- coding: utf-8 -*-
import pandas as pd
from src.process_execution import run

def test_run_pipeline(tmp_path):
    df_entrada = pd.DataFrame({
        "DATA_INICIO": ["02-09-2016 10:54", "02-09-2016 11:43", "02-09-2016 14:00"],
        "CATEGORIA": ["Pessoal", "Negocio", "Negocio"],
        "PROPOSITO": [None, "Reunião", "Cliente"],
        "DISTANCIA": [53, 3, 10]
    })

    input_csv = tmp_path / "entrada.csv"
    output_csv = tmp_path / "saida.csv"
    df_entrada.to_csv(input_csv, sep=";", index=False, encoding="utf-8")

    run(input_csv, output_csv)
    assert output_csv.exists()

    df_saida = pd.read_csv(output_csv)
    colunas_esperadas = [
        'DT_REFE', 'QT_CORR', 'QT_CORR_NEG', 'QT_CORR_PESS',
        'VL_MAX_DIST', 'VL_MIN_DIST', 'VL_AVG_DIST',
        'QT_CORR_REUNI', 'QT_CORR_NAO_REUNI'
    ]
    for coluna in colunas_esperadas:
        assert coluna in df_saida.columns

    assert df_saida.iloc[0]["QT_CORR"] == 3
