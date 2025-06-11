# -*- coding: utf-8 -*-
from src.data_loader import load_data
from src.data_transformations import preprocess_dataframe, generate_aggregation


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

        # Save processed data
        processed_data.to_csv(output_path, index=False)
        print(f"Processed data saved to {output_path}")
    else:
        print("Data loading failed. No processing performed.")
