def load_data(historico_df, info_df, dividendos_df, output_dir="data"):
    import os

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    historico_df.to_csv(f"{output_dir}/historico.csv", index=False)     

    info_df.to_csv(f"{output_dir}/info.csv", index=False)

    dividendos_df.to_csv(f"{output_dir}/dividendos.csv", index=False)

    print(f"Arquivos salvos em: {output_dir}/")