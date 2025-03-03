from pydantic import BaseModel


class Room(BaseModel):
    id: int
    room_number: str
    capacity: int
    price: int
