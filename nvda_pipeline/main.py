import logging

from extract import extract_data
from transform import transform_data
from load import load_data

logging.basicConfig(level=logging.INFO)

def main():

    ticker = "NVDA"
    logging.info(f"Iniciando pipeline para {ticker}")

    history, info, dividends = extract_data(ticker)
    logging.info("Extração Concluída.")


    historico_df, info_df, dividendos_df = transform_data(history, info, dividends)
    logging.info("Transformação Concluída.")

    load_data(historico_df, info_df, dividendos_df, output_dir="data")
    logging.info("Dados salvos com sucesso na pasta 'data/'.")

    logging.info("Prévia dos dados extraídos e transformados:")
    print("\n Hisórico de preços:")
    print(historico_df.head(), "\n")

    print("Info (metados):")
    print(info_df.head(), "\n")

    print("Dividendos:")
    print(dividendos_df.head(), "\n")


if __name__ == "__main__":
    main()