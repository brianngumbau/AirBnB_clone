#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represenst a place.

    Attributes:
        city_id : city id.
        user_id : User id.
        name: name of the place.
        description : description of the place.
        number_rooms : number of rooms of the place.
        number_bathrooms :  number of bathrooms
        max_guest : maximum number of guest
        price_by_night (int): price by night
        latitude : The latitude of the place
        longitude : The longitude of the place.
        amenity_ids : A list of Amenity ids.
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
