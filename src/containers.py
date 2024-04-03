"""Containers module."""

from dependency_injector import containers, providers

from src.bahan.repositories import BahanRepository
from src.bahan.services import BahanService

from .database import Database
from src.user.repositories import UserRepository
from src.user.services import UserService

import os, sys
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[
        "src.user.endpoints",
        "src.bahan.endpoints"
    ])

    config = providers.Configuration(yaml_files=["docker-compose.yml"])

    db = providers.Singleton(Database, db_url=os.environ["DATABASE_URL"])

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )
    
    bahan_repository = providers.Factory(
        BahanRepository,
        session_factory=db.provided.session,
    )

    bahan_service = providers.Factory(
        BahanService,
        bahan_repository=bahan_repository,
    )