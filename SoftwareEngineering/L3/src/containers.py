from dependency_injector import containers, providers

from config import settings
from database import Neo4jConnectionHelper


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    # Database

    db_helper = providers.Singleton(
        Neo4jConnectionHelper,
        db_url=settings.db_url,
        user=settings.db_user,
        password=settings.db_password,
    )

    # Services
