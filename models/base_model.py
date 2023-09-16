#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATETIME
from models import storage_type

Base = declarative_base


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(string(60), nullable=False, primary_key=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        def_attr = {
                'id': str(uuid.uuid4())
                'created_at': datetime.now(),
                'updated_at': datetime.now(),
                }
        for attr, default_value in def_attr.items():
            setattr(self, attr, kwargs.get(attr, defualt_value))

        for k, v in kwargs.items():
            if k not in ['__class', *def_attr.keys()]:
                setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""

        exclude_keys = ['_sa_instance_state']  # Add other keys to exclude if needed
        return {
                k: v.isoformat() if isinstance(v, datetime) else v
                for k, v in self.__dict__.items()
                if k not in exclude_keys
                }

    def delete(self):
        '''deletes the current instance from the storage'''

        from models import storage
        storage.delete(self)


