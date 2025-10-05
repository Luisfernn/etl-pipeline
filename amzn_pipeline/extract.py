import yfinance as yf

def extract_data(ticker="AMZN"):
    tk = yf.Ticker(ticker)

    historico = tk.history(period="1y")
    info = tk.info
    dividendos = tk.dividends

    return historico, info, dividendos