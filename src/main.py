"""Application module."""

from fastapi import FastAPI

from .containers import Container
from src.user import endpoints


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)
    return app


app = create_app()