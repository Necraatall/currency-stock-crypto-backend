from forex_python.converter import CurrencyRates

async def fetch_currency_rates(base_currency="USD", target_currencies=["EUR", "GBP", "CZK"]):
    c = CurrencyRates()
    rates = {}
    for target in target_currencies:
        rates[target] = c.get_rate(base_currency, target)
    return rates
