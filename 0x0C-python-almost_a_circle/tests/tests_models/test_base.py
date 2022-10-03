#!/usr/bin/python3
"""
Unittest for Base Class
# run with python3 -m unittest discover tests
# run with python 3 -m unittest tests/tests_models/test_base.py
"""

import unittest
import pep8
import json
import os
from models import base
from models import rectangle
Base = base.Base
Rectangle = rectangle.Rectangle


class TestPep8(unittest.TestCase):
    """Pep8 models.base.py & tests/tests_models/tests_base.py"""
    def test_pep8(self):
