#!/usr/bin/python3
"""Defines FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        objcname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objcname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {ob: odict[obj].to_dict() for ob in odict.keys()}
        with open(FileStorage.__file_path, "w") as k:
            json.dump(objdict, k)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if the JSON file exists."""
        try:
            with open(FileStorage.__file_path) as k:
                objdict = json.load(k)
                for i in objdict.values():
                    class_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls_name)(**i))
        except FileNotFoundError:
            return
