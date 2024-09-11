#!/usr/bin/python3
"""Unittest module for Amenity class."""

from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
from models import storage
import json
import re
import os
import time
import unittest


class TestAmenity(unittest.TestCase):

"""Test cases for the Amenity class."""

def setUp(self):
"""Tears down test methods."""
pass

def tearDown(self):
"""Tears down reset methods."""
self.resetStorage()
pass

def resetStorage(self):
"""Resets FileStorage data."""
FileStorage._FileStorage__objects = {}
if os.path.isfile(FileStorage._FileStorage__file_path):
os. remove(FileStorage._FileStorage__file_path)

def test_8_instantiation(self):
"""Tests instantiation of Amenity class."""

b = Amenity()
self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
self.assertIsInstance(b, Amenity)
self.assertTrue(issubclass(type(b),BaseModel))

def test_8_attributes(self):
"""Tests the attributes of Amenity class."""
attributes = storage.attributes()["Amenity"]
o = Amenity()
for k, v in attributes.items():
self.assertTrue(hasattr(o,k))
self.assertEqual(type(getattr(o,k,None)), v)

if __name__ = "__main__":
unittest.main()