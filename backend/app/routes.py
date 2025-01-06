from sanic.response import json
from app.services.yfinance_service import fetch_stock_data

def register_routes(app):
    @app.route("/stocks", methods=["GET"])
    async def get_stocks(request):
        data = await fetch_stock_data()
        return json(data)
