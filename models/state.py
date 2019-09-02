#!/usr/bin/python3
"""This is the state class"""
from models.base_model import Base, BaseModel, os_type_storage
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    if os_type_storage == "db":
        __tablename__ = "states"
        name = Column(String(128),  nullable=False)
        cities = relationship('City', cascade="all, delete", backref='state')
    else:
        name = ""

        @property
        def cities(self):
            my_list = []
            dict_city = models.storage.all(models.city.City)
            for key, value in dict_city.items():
                if self.id == value.state_id:
                    my_list.append(value)
            return(my_list)
