import logging
from extract import extract_data
from transform import transform_data
from load import load_data

logging.basicConfig(level=logging.INFO)

def main():
    ticker = "EMBR3"
    logging.info(f"[INFO] iniciando pipeline para {ticker}")

    history, info, dividends = extract_data(ticker)
    logging.info(f"Extração concluída.")

    historico_df, info_df, dividendos_df = transform_data(history, info, dividends)
    logging.info(f"Transformação concluída.")

    load_data(historico_df, info_df, dividendos_df, output_dir="data")
    logging.info(f"Tudo salvo na pasta 'data/'.")

    logging.info(f"Prévia dos dados salvos e tranformados:")
    print("\nHistórico de preços:")
    print(historico_df.head(), "\n")

    print("Info (metados):")
    print(info_df.head(), "\n")

    print("Dividendos:")
    print(dividendos_df.head, "\n")


if __name__ == '__main__':
    main()


