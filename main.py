# -*- coding: utf-8 -*-
import logging
from src.process_execution import run

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    logger.info("Iniciando o processamento dos dados.")
    run(
        input_path='data/raw/info_transportes.csv',
        silver_path='data/processed/info_transportes_clean.csv',
        output_path='data/gold/info_corridas_do_dia.csv'
    )
    logger.info("Processamento finalizado com sucesso.")

if __name__ == '__main__':
    main()
