#!/usr/bin/python3
"""
Unittest for Square Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_square.py
"""


import unittest
import pycodestyle
from io import StringIO
from contextlib import redirect_stdout
from models import square
Square = square.Square


class TestPep8(unittest.TestCase):
    """Pep8 models/square.py & tests/test_models/test_square.py"""
    def test_pycodestyle(self):
        """Pep8"""
        style = pycodestyle.StyleGuide(quiet=False)
        errors = 0
        files = ["models/square.py", "tests/test_models/test_square.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pycodestyle')


class TestBase(unittest.TestCase):
    """Tests for models/square.py"""

    """Test attributes"""
    def test_all_attr_given(self):
