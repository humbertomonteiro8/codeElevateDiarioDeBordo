# -*- coding: utf-8 -*-
from src.data_transformations import preprocess_dataframe, generate_aggregation, set_dtype_mappings
from src.data_loader import load_data
from src.utils import oracle_connection
from sqlalchemy import text
import pandas as pd

def run(input_path: str, output_path: str) -> None:
    """
    Execute the data loading and processing pipeline.

    Parameters:
        input_path (str): The path to the input CSV file.
        output_path (str): The path to save the processed data.
    """
    # Load data
    df_loader = load_data(input_path)
    df_preprocess = preprocess_dataframe(df_loader)
    df_agg = generate_aggregation(df_preprocess)

    if df_agg is not None:
        processed_data = df_agg

        # Save processed data on csv
        processed_data.to_csv(output_path, index=False)
        print(f"Processed data saved to {output_path}")

        # Save processed data on oracle database
        engine = oracle_connection()
        # Antes de enviar ao banco, converta para datetime
        processed_data["DT_REFE"] = pd.to_datetime(processed_data["DT_REFE"])

        try:
            # Inserção direta fora de transação explícita (Pandas cuida do commit)
            processed_data.to_sql(
                name='INFO_CORRIDAS_DO_DIA',
                con=engine,
                index=False,
                if_exists='append',
                dtype=set_dtype_mappings()
            )
            with engine.connect() as conn:
                result = conn.execute(text("SELECT COUNT(*) FROM INFO_CORRIDAS_DO_DIA"))
                print(f"Registros encontrados no Oracle: {result.scalar()}")

        except Exception as e:
            print(f"Erro ao inserir dados: {e}")
    else:
        print("Data loading failed. No processing performed.")
