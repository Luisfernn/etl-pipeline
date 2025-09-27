import pandas as pd

def transform_data(history, info, dividends):

    historico_df = history[["Close", "Volume"]].copy()
    info_df = pd.DataFrame(list(info.items()), columns=["Chave", "Valor"])
    
    if dividends.empty:
        dividendos_df = pd.DataFrame([["N/A"]], columns=["Dividendos"])

    else:
         dividendos_df = dividends.reset_index()
         dividendos_df.columns = ["Data", "Dividendo"]

    return historico_df, info_df, dividendos_df