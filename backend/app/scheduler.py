from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.services.yfinance_service import fetch_stock_data
from app.db import get_db

scheduler = AsyncIOScheduler()

def start_scheduler():
    db = get_db()

    async def update_stock_data():
        data = await fetch_stock_data()
        db.set("stock:AAPL", data["price"])

    scheduler.add_job(update_stock_data, "interval", minutes=1)
    scheduler.start()
