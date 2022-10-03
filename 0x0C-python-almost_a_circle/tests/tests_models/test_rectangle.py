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



