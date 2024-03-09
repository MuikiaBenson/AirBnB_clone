#!/usr/bin/python3
"""Place class module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place.
    Attributes:
        user_id (str): User id
        name (str): Name of place
        city_id (str): City id
        description (str): Description of a place
        number_rooms (int): number of rooms of the place
        number_bathrooms (int): number of bathrooms of the place
        max_guest(int): Maximum number of guests of the place
        price_by_night (int): Price of the night ny place
        latitude (float): The latitude of the place
        longitude (float): The longitude of the place
        amenity_ids (list): A list of amenity ids.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
