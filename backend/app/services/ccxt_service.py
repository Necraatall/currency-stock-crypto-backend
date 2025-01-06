import ccxt

async def fetch_crypto_data(exchange_name="binance", symbols=["BTC/USDT", "ETH/USDT"]):
    exchange = getattr(ccxt, exchange_name)()
    data = {}
    for symbol in symbols:
        ticker = exchange.fetch_ticker(symbol)
        data[symbol] = {
            "price": ticker["last"],
            "volume": ticker["quoteVolume"],
            "change": ticker["percentage"]
        }
    return data
