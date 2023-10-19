#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_mode import BaseModel, Base
from models import storage_type
from models.city import City
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class / table model"""
	if getenv('HBNB_TYPE_STORAGE') == 'db':
		

        @property
        def cities(self):
            '''returns the list of City instances with state_id
                equals the current State.id
                FileStorage relationship between State and City
            '''
            from models import storage
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
