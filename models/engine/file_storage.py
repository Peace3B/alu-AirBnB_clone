#!/usr/bin/python3
"""Module for FileStorage class."""

import datetime
import json
import os

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if it exists."""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                # Assuming there's a logic to recreate instances from dict data
        except FileNotFoundError:
            pass
