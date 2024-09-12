"""Module for FileStorage autoinit."""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

class BaseModel:
"""Base class for all models in the AirBnB clone project."""

def __init__(self):
"""Initialize a new instance of BaseModel"""
self.id = str(uuid.uuid4())
self.created_at = datetime.now()
self.updated_at = self.created_at


def save(self):
"""Update the public instance attribute updated_at with the current datetime."""
self.updated_at = datetime.now()

def to_dict(self):
"""
Return a dictionary containing all keys/values of __dict__ of the instance.
- Adds the key __class__ to the dictionary with the class name of the project.
_ Converts created_at and updated_at to ISO format strings.
"""
dict_representation = self.__dict__.copy()
dict_representation['__class__'] = self.__class__.__name__
dict_representation['created_at'] = self.created_at.isoformat()
dict_representation['updated_at'] = self.updated_at.isoformat()
return dict_representation

def __str__(self):
"""Return a string representation of the BaseModel instance."""
return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
