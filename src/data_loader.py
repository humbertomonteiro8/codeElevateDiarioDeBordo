# -*- coding: utf-8 -*-
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(file_path, sep=';', encoding='utf-8')
    except Exception as ex:
        print(f"Erro ao carregar dados: {ex}")
        return pd.DataFrame()
