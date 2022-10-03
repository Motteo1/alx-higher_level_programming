#!/usr/bin/python3
"""
Unittest for Base Class
# run with python3 -m unittest discover tests
# run with python 3 -m unittest tests/test_models/test_base.py
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
        """Pep8"""
        style = pep8.StyleGuide(quiet=false)
        errors = 0
        files = ["models.base.py", "tests/test_models/test_base.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')


class TestBase(unittest.TestCase):
    """Tests for models/base.py"""
