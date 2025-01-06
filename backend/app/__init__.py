from sanic import Sanic
from app.routes import register_routes
from app.db import initialize_db

def create_app():
    app = Sanic("CurrencyApp")
    register_routes(app)
    initialize_db()
    return app
