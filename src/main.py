"""Application module."""

from fastapi import FastAPI

from .containers import Container
from src.user import endpoints as user_endpoints
from src.bahan import endpoints as bahan_endpoints


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(user_endpoints.router)
    app.include_router(bahan_endpoints.router)
    return app


app = create_app()



@app.get("/")
def main():
    return {"Hello": "World!"}