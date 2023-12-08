#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class that defines all  attributes and methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args
            **kwargs
        """
        form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "created_at" or a == "updated_at":
                    self.__dict__[a] = datetime.strptime(b, form)
                else:
                    self.__dict__[a] = b
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        dict_r = self.__dict__.copy()
        dict_r["created_at"] = self.created_at.isoformat()
        dict_r["updated_at"] = self.updated_at.isoformat()
        dict_r["__class__"] = self.__class__.__name__
        return dict_r

    def __str__(self):
        """ print [<class name>] (<self.id>) <self.__dict__>"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
