import yfinance as yf 

def extract_data(ticker="AAPL"):
    tk = yf.Ticker(ticker)

    historico = tk.history(perior="1y")
    info = tk.info
    dividendos = tk.dividends

    return historico, info, dividendos

