#!/usr/bin/python3
"""Unittest module for Place class."""

from models.base_model import BaseModel
from model.engine.file_storage import FileStorage
from datetime import datetime
from models import storage
from models.place import place
import unittest
import re
import os
import json
import time 
