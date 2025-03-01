from database import Neo4jConnectionHelper


class BaseService:
    def __init__(self, db: Neo4jConnectionHelper) -> None:
        self._db = db


class HotelsService(BaseService):
    pass


class RoomsService(BaseService):
    pass


class ServicesService(BaseService):
    pass


class ClientsService(BaseService):
    pass


class BookingsService(BaseService):
    pass
