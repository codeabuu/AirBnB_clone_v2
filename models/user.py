#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = (
            Column(String(128), nullable=False)
            if storage_type == 'db'
            else ""
            )
    password = Column(String(128), nullable=False) if storage_type == 'db' else ""
    first_name = Column(String(128), nullable=True) if storage_type == 'db' else ""
    last_name = Column(String(128), nullable=True) if storage_type == 'db' else ""

    if storage_type == 'db':
        places = relationship('Place', backref='user', cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user', cascade='all, delete, delete-orphan')
