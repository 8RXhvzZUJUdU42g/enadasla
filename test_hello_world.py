#!/usr/bin/env python3
"""
Test for the hello_world.py module
"""
import unittest
from io import StringIO
import sys
from contextlib import redirect_stdout
import hello_world

class TestHelloWorld(unittest.TestCase):
    """Test cases for hello_world.py"""
    
    def test_main_output(self):
        """Test that the main function prints 'Hello, World!'"""
        f = StringIO()
        with redirect_stdout(f):
            hello_world.main()
        self.assertEqual(f.getvalue().strip(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()