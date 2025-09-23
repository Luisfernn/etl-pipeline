import yfinance as yf

def extract_data (ticker="NVDA"):
    tk = yf.Ticker(ticker)

    historico = tk.history(period="1mo")
    info = tk.info
    dividendos = tk.dividends

    return historico, info, dividendos