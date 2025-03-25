import yfinance as yf

def get_stock_price(ticker: str) -> float:
    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")["Close"].iloc[-1]  
        return round(price, 2)
    except Exception as e:
        print(f"Error fetching stock price: {e}")
        return 0.0
