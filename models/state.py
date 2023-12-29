#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import city
from models import storage_type
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if storage_type == "db":
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        name = ""


        @property
        def cities(self):
            """
            return the list of city objects linked to current state
            """
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
