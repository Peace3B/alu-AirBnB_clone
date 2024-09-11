#!/usr/bin/python3
"""Unittest module for the User class."""

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime
import unittest
import time
import re
import os
import json


class TestUser(unittest.TestCase):

    def setUp(self):
        """Sets up a User object to be used in tests."""
        self.user = User("john_doe", "john@example.com")

    def test_username(self):
        """Test that the username is correctly set."""
        self.assertEqual(self.user.username, "john_doe")

    def test_email(self):
        """Test that the email is correctly set."""
        self.assertEqual(self.user.email, "john@example.com")

    def test_display(self):
        """Test that display method works correctly."""
        self.assertEqual(self.user.display(), "john_doe (john@example.com)")

if __name__ == "__main__":
    unittest.main()
