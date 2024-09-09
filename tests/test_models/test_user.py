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
