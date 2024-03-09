#!/usr/bin/python3i
"""Module for FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents an abstract storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """set in __objects obj with key <obj_class_name>.id"""
        name1 = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(name1, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = (
            {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
                )
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for obj_key, obj_data in obj_dict.items():
                    cls_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    obj_instance = getattr(models, cls_name)(**obj_data)
                    self.new(obj_instance)
        except FileNotFoundError:
            return
