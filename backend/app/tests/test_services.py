import pytest
from app.services.forex_service import fetch_currency_rates
from app.services.ccxt_service import fetch_crypto_data
from app.services.graph_service import generate_chart

@pytest.mark.asyncio
async def test_fetch_currency_rates():
    rates = await fetch_currency_rates()
    assert "EUR" in rates
    assert rates["EUR"] > 0

@pytest.mark.asyncio
async def test_fetch_crypto_data():
    data = await fetch_crypto_data()
    assert "BTC/USDT" in data
    assert data["BTC/USDT"]["price"] > 0

@pytest.mark.asyncio
async def test_generate_chart():
    data = {"x": [1, 2, 3], "y": [10, 20, 30]}
    chart = await generate_chart(data)
    assert chart.startswith("iVBOR")  # Base64 PNG začíná těmito znaky
