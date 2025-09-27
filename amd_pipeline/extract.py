import yfinance as yf

def extract_data(ticker="AMD"):
     tk = yf.Ticker(ticker)

     histórico = tk.history(period="6mo")
     informações = tk.info
     dividendos = tk.dividends

     return histórico, informações, dividendos