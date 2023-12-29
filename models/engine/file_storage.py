#!/usr/bin/python3
"""
Module Docs
"""
import json
from os import path


class FileStorage:
    """
    parent class module that assigns storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        all instances or instances of a specific class
        """
        if cls is None:
            return FileStorage.__objects
        else:
            instances = {}
            for key, value in FileStorage.__objects.items():
                class_name = key.split('.')[0]
                if class_name == cls.__name__:
                    instances[key] = value
            return instances

    def new(self, obj):
        """
        new instances
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        save instances
        """
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        delete obj from __objects if it’s inside
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def close(self):
        """
        deserialize the JSON file objects
        """
        self.reload()
