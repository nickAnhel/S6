from dependency_injector import containers, providers

from config import settings
from database import Neo4jConnectionHelper
from services import HotelsService, RoomsService, ServicesService, BookingsService, ClientsService


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

    hotels_service = providers.Factory(
        HotelsService,
        db=db_helper,
    )

    rooms_service = providers.Factory(
        RoomsService,
        db=db_helper,
    )

    services_service = providers.Factory(
        ServicesService,
        db=db_helper,
    )

    clients_service = providers.Factory(
        ClientsService,
        db=db_helper,
    )

    bookings_service = providers.Factory(
        BookingsService,
        db=db_helper,
    )
