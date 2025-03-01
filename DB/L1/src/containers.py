from dependency_injector import containers, providers

from config import settings
from database import DBHelper
from services import CustomersService, PartsService, SalesService
from repositories import CustomersRepository, PartsRepository, SalesRepository


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    # Database

    db_helper = providers.Singleton(
        DBHelper,
        host=settings.db_host,
        port=settings.db_port,
        user=settings.db_user,
        password=settings.db_password,
        db=settings.db_name,
    )

    # Repositories

    customers_repository = providers.Factory(
        CustomersRepository,
        db=db_helper,
    )

    parts_repository = providers.Factory(
        PartsRepository,
        db=db_helper,
    )

    sales_repository = providers.Factory(
        SalesRepository,
        db=db_helper,
    )

    # Services

    customers_service = providers.Factory(
        CustomersService,
        repo=customers_repository,
    )

    parts_service = providers.Factory(
        PartsService,
        repo=parts_repository,
    )

    sales_service = providers.Factory(
        SalesService,
        repo=sales_repository,
    )
