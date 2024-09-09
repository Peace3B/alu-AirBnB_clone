#!/usr/bin/python3
"""Unittest module for FileStorage class."""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
from models import storage
import json
import re
import os
import time
import unittest


class TestFileStorage(unittest.TestCase):
"""Test Cases for the fileStorage class."""

def setUp(self):
"""Sets up test methods."""
pass
