from enum import Enum


class Services(str, Enum):
    DAILY_CLEANING = "Daily Cleaning"
    LAUNDRY = "Laundry"
    DRY_CLEANING = "Dry Cleaning"
    RESTAURANT = "Restaurant"
    BAR = "Bar"
    SWIMMING_POOL = "Swimming Pool"
    SAUNA = "Sauna"
