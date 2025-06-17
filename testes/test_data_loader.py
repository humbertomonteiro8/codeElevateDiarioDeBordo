# -*- coding: utf-8 -*-
import pandas as pd
import pytest

from src.data_loader import load_data

def test_load_data_csv_real(tmp_path):
    df_mock = pd.DataFrame({
        "CATEGORIA": ["Negocio", "Pessoal"],
        "DISTANCIA": [10, 20]
    })

    csv_path = tmp_path / "test_file.csv"
    df_mock.to_csv(csv_path, sep=';', index=False, encoding='utf-8')
    df_carregado = load_data(csv_path)

    assert df_carregado is not None
    assert isinstance(df_carregado, pd.DataFrame)
    pd.testing.assert_frame_equal(df_mock, df_carregado)


def test_load_data_arquivo_inexistente():
    caminho_fake = "data/raw/nao_existe.csv"
    resultado = load_data(caminho_fake)

    assert resultado is None

def test_load_data_csv_malformado(tmp_path):
    csv_ruim = tmp_path / "arquivo_quebrado.csv"
    csv_ruim.write_text("CATEGORIA;DISTANCIA\nNegocio;10\nPessoal")  # linha incompleta
    resultado = load_data(csv_ruim)

    assert resultado is not None
    assert resultado.isnull().values.any()