import yfinance as yf 

def extract_data(ticker="MSFT"):
    tk = yf.Ticker(ticker)

    historico = tk.history(perior="1y")
    info = tk.info
    dividendos = tk.dividends

    return historico, info, dividendos

