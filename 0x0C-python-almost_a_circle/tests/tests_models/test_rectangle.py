#!/usr/bin/python3
"""
Unittest for Rectangle Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_rectangle.py
"""


import os
import pycodestyle
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models import rectangle
Rectangle = rectangle.Rectangle


class TestPep8(unittest.TestCase):
    """Pep8 models/rectangle.py & tests/test_models/test_rectangle.py"""
    def test_pep8(self):
        """Pep8"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pycodestyle')


class TestBase(unittest.TestCase):
    """Tests for models/rectangle.py"""

    """Test attributes"""
    def test_all_attr_given(self):
        """Test all attributes match what's given"""
        r1 = Rectangle(10, 20, 1, 2, 99)
        self.assertTrue(r1.width == 10)
        self.assertTrue(r1.height == 20)
        self.assertTrue(r1.x == 1)
        self.assertTrue(r1.y == 2)
        self.assertTrue(r1.id == 99)

    def test_default_attr(self):
        """Test default attributes are set when not given"""
        r2 = Rectangle(3, 4)
        self.assertTrue(r2.width == 3)
        self.assertTrue(r2.height == 4)
        self.assertTrue(r2.x == 0)
        self.assertTrue(r2.y == 0)
        self.assertTrue(r2.id is not None)
