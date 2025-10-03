import yfinance as yf

def extract_data(ticker="ERJ"):
     tk = yf.Ticker(ticker)
    
     historico = tk.history(period='6mo')
     informações = tk.info
     dividendos = tk.dividends

     return historico, informações, dividendos