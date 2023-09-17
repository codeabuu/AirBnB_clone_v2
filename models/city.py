#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False) if storage_type == 'db' else ''
    state_id = Column(String(60), ForeignKey('states.id'),
                      nullable=False) if storage_type == 'db' else ''

    if storage_type == 'db':
        places = relationship('Place',
                              backref='cities',
                              cascade='all, delete, delete-orphan')
