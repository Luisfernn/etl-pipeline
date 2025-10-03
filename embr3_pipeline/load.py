def load_data(dfs, output_dir="data"):
    import os
    
    df = {
        "historico": historico_df,
        "info": info_df,
        "dividendos": dividendos_df
    }
     
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, output_dir)

    os.makedirs(output_path, exist_ok=True)

    for name, df in dfs.items():
        df.to_csv(os.path.join(output_path, f"{name}.csv"), index=False)

    print(f"Arquivos salvos em:{output_path}")