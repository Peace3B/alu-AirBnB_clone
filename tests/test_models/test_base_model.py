#!/usr/bin/python3
"""Unittest module for the BaseModel class."""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json 
import re
import os
import time
import unittest
import uuid


import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Sets up an instance of BaseModel for testing."""
        self.model = BaseModel()

    def test_id_is_unique(self):
        """Test that id is a unique string in UUID format."""
        self.assertIsInstance(self.model.id, str)
        # Verify if the id is a valid UUID string
        try:
            uuid.UUID(self.model.id)
        except ValueError:
            self.fail(f"{self.model.id} is not a valid UUID")

    def test_created_at_is_datetime(self):
        """Test that created_at is of type datetime."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is of type datetime and equal to created_at at initialization."""
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_save_method(self):
        """Test the save method updates the updated_at attribute."""
        old_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertGreater(new_updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method returns the correct dictionary."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertIsInstance(model_dict, dict)

if __name__ == "__main__":
    unittest.main()
    