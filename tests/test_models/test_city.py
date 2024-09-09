#!/usr/bin/python3
"""Unittest module for City class."""

from models.city import City
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
from models import storage
import json
import re
import os
import time
import unittest
