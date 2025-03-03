import typing as tp

from database import Neo4jConnectionHelper
from enums import Services


class BaseService:
    def __init__(self, db: Neo4jConnectionHelper) -> None:
        self._db = db


class HotelsService(BaseService):
    def get_hotel_serives(self) -> list[dict[str, tp.Any]]:
        with self._db.session() as session:
            query = """
                MATCH (h:Hotel {name: "Mountain Retreat"})-[o:OFFERS]->(s:Service)
                RETURN s.service_id as id, s.name as name;
            """
            res = session.execute(query)
            return res

    def get_total_revenue(self, hotel_name: str) -> list[dict[str, tp.Any]]:
        with self._db.session() as session:
            query = """
                MATCH (h:Hotel {name: $name})-[:HAS_ROOM]->(r:Room)<-[:INCLUDES]-(b:Booking)
                RETURN SUM(b.total_price) AS total_revenue;
            """
            res = session.execute(query, name=hotel_name)
            return res


class RoomsService(BaseService):
    def get_all(self) -> list[dict[str, tp.Any]]:
        with self._db.session() as session:
            query = """
                MATCH (r:Room)
                RETURN r.room_id as id, r.room_number as room_number, r.capacity as capacity, r.price as price;
            """
            res = session.execute(query)
            return res

    def get_available_double_rooms(self, date: str) -> list[dict[str, tp.Any]]:
        with self._db.session() as session:
            query = """
                MATCH (r:Room {capacity: 2})
                WHERE NOT EXISTS {
                    MATCH (b:Booking)-[:INCLUDES]->(r)
                    WHERE
                        b.check_in_date <= $date AND
                        b.check_out_date >= $date
                }
                RETURN
                    r.room_id as room_id,
                    r.room_number as room_number,
                    r.price as price;
            """
            res = session.execute(query, date=date)
            return res


class ServicesService(BaseService):
    def get_all_ordered_by_usage(self) -> list[dict[str, tp.Any]]:
        with self._db.session() as session:
            query = """
                MATCH (s:Service)
                OPTIONAL MATCH (b:Booking)-[:USES]->(s:Service)
                WITH s, count(b) as total_used
                ORDER BY total_used DESC
                RETURN s.name as name, total_used;
            """
            res = session.execute(query)
            return res


class ClientsService(BaseService):
    def get_client_bookings(self, email: str) -> list[dict[str, tp.Any]]:
        with self._db.session() as session:
            query = """
                MATCH (c:Client {email: $email})-[:BOOKED]->(b:Booking)-[:INCLUDES]->(r:Room)
                RETURN
                    b.booking_id as booking_id,
                    r.room_number as room_number,
                    b.check_in_date as check_in_date,
                    b.check_out_date as check_out_date;
            """
            res = session.execute(query, email=email)
            return res

    def get_clients_used_services(self, service: Services) -> list[dict[str, tp.Any]]:
        with self._db.session() as session:
            query = """
                MATCH (c:Client)-[:BOOKED]->(b:Booking)-[:USES]->(s:Service {name: $service})
                RETURN c.first_name + " " + c.last_name  AS client_name, c.email AS email;
            """
            res = session.execute(query, service=service)
            return res


class BookingsService(BaseService):
    def get_bookings_with_service(self, service: Services) -> list[dict[str, tp.Any]]:
        with self._db.session() as session:
            query = """
                MATCH (s:Service {name: $service})<-[:USES]-(b:Booking)-[:INCLUDES]->(r:Room)
                RETURN
                    b.booking_id AS booking_id,
                    r.room_number AS room_number,
                    b.check_in_date AS check_in,
                    b.check_out_date AS check_out;
            """
            res = session.execute(query, service=service)
            return res
