#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base, os_type_storage
from models import *
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
import models


if os_type_storage == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True,
                                 nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    if os_type_storage == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128),  nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float(), nullable=True)
        longitude = Column(Float(), nullable=True)
        reviews = relationship('Review', cascade="all, delete",
                               backref='place')
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, backref='place_amenities')
    else:
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

        @property
        def get_reviews(self):
            my_list = []
            reviews_dict = models.storage.all(Review)
            for key, value in reviews_dict.items():
                if self.id == reviews_dict['place_id']:
                    my_list.append(value)
            return(my_list)

        @property
        def amenities(self):
            my_list = []
            amen_dict = models.storage.all(models.amenity.Amenity)
            amen_ids = amen_dict['amenity_ids']
            for item in amenity_ids:
                if self.id == item:
                    my_list.append(item)
            return(my_list)

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
