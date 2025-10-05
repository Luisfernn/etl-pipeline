import yfinance as yf

def extract_data(ticker="MGLU3"):
    tk = yf.ticker(ticker)

    historico = tk.history(period="1y")
    info = tk.info
    dividendos = tk.dividends

    return historico, info, dividendos