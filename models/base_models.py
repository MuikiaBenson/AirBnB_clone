#!/usr/bin/python3
"""Module defining BaseModel class."""
from typing import Any, Dict
from uuid import uuid4
from datetime import datetime

import models


class BaseModel:
    """Serves as the foundational model for the HBnB project."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initializes a new BaseModel.

        Args:
            *args (Any): Unused.
            **kwargs (Dict): key/value attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_form)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Updates updated_at with the currect datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary of Any of the BaseModel instances."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """Returns the string that contains the class name, id and dict.
        string representation of the BaseModel
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
