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

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

    """Test attributes"""
    def test_id_given(self):
        """Test ids match when given"""
        self.assertTrue(Base(999), self.id == 999)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(-80), self.id == -80)

    def test_id_not_given(self):
