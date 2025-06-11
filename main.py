# -*- coding: utf-8 -*-
from src.process_execution import run


def main():
    run(
        input_path='data/raw/info_transportes.csv',
        output_path='data/processed/info_corridas_do_dia.csv'
    )


if __name__ == '__main__':
    main()