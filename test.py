#!/usr/bin/python3

import unittest
from BASIC_api import *

class BASIC_api_test(unittest.TestCase):
    def test_code(self):
        self.assertTrue(output.status_code == 200)
    def test_login(self):
        self.assertTrue(output.json()["login"] == "dronmorse")

