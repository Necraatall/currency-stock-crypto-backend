from sanic.response import json
from app.services.yfinance_service import fetch_stock_data

def register_routes(app):
    @app.route("/stocks", methods=["GET"])
    async def get_stocks(request):
        data = await fetch_stock_data()
        return json(data)


@ app.route("/currencies", methods=["GET"])
async def get_currency_rates(request):
    from app.services.forex_service import fetch_currency_rates
    data = await fetch_currency_rates()
    return json(data)


@ app.route("/crypto", methods=["GET"])
async def get_crypto_data(request):
    from app.services.ccxt_service import fetch_crypto_data
    data = await fetch_crypto_data()
    return json(data)


@ app.route("/graph", methods=["POST"])
async def get_chart(request):
    from app.services.graph_service import generate_chart
    body = request.json
    data = body.get("data", {"x": [], "y": []})
    title = body.get("title", "Chart")
    x_label = body.get("x_label", "X")
    y_label = body.get("y_label", "Y")
    chart = await generate_chart(data, title, x_label, y_label)
    return json({"chart": chart})


