# -*- coding: utf-8 -*-
import pandas as pd


def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded data as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path, sep=';', encoding='utf-8')
        return data
    except Exception as ex:
        print(f"Error loading data: {ex}")
        return None