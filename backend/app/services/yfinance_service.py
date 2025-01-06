import yfinance as yf

async def fetch_stock_data():
    stock = yf.Ticker("AAPL")
    return {
        "symbol": "AAPL",
        "price": stock.history(period="1d")["Close"].iloc[-1]
    }
