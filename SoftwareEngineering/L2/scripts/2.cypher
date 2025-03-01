// 1
MATCH (n) RETURN n;

// 2
MATCH (r:Room)
RETURN r.room_id as id, r.room_number as room_number, r.capacity as capacity, r.price as price;

// 3
MATCH (s:Service)
OPTIONAL MATCH (b:Booking)-[:USES]->(s:Service)
WITH s, count(b) as total_used
ORDER BY total_used DESC
RETURN s.name as name, total_used;

// 4
MATCH (c:Client {email: "john.doe@example.com"})-[:BOOKED]->(b:Booking)-[:INCLUDES]->(r:Room)
RETURN
    b.booking_id as booking_id,
    r.room_number as room_number,
    b.check_in_date as check_in_date,
    b.check_out_date as check_out_date;

// 5
MATCH (h:Hotel {name: "Mountain Retreat"})-[o:OFFERS]->(s:Service)
RETURN h, o, s;

// 6
MATCH (s:Service {name: "Restaurant"})<-[:USES]-(b:Booking)-[:INCLUDES]->(r:Room)
RETURN
    b.booking_id AS booking_id,
    r.room_number AS room_number,
    b.check_in_date AS check_in,
    b.check_out_date AS check_out;

// 7
MATCH (r:Room {capacity: 2})
WHERE NOT EXISTS {
    MATCH (b:Booking)-[:INCLUDES]->(r)
    WHERE
        b.check_in_date <= "2023-10-03" AND
        b.check_out_date >= "2023-10-03"
}
RETURN
    r.room_id as room_id,
    r.room_number as room_number,
    r.price as price;

// 8
MATCH (c:Client)-[:BOOKED]->(b:Booking)-[:USES]->(s:Service {name: "Bar"})
RETURN c.first_name + " " + c.last_name  AS client_name, c.email AS email;

// 9
MATCH (h:Hotel {name: "Sunset Paradise"})-[:HAS_ROOM]->(r:Room)<-[:INCLUDES]-(b:Booking)
RETURN SUM(b.total_price) AS total_revenue;

// 10
MATCH (c:Client)-[:BOOKED]->Lab3App(b:Booking)-[:INCLUDES]->(r:Room)<-[:HAS_ROOM]-(h:Hotel {stars: 5})
MATCH (b)-[:USES]->(s:Service {name: "Restaurant"})
WITH c, COUNT(b) as booking_count
ORDER BY booking_count DESC
RETURN DISTINCT c.first_name + " " + c.last_name AS client_name, c.email AS email, booking_count;