"""
This file holds the tests for data.py.
"""

from unittest import TestCase, skip
import API.endpoints as ep
# import random

import db.data as db

FAKE_USER = "Fake user"


class DBTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_write_collection(self):
        """
        Can we write the user db?
        """
        fake_data = {FAKE_USER: {}}
        return True

    def test_fetch_buser(self):
        """
        Can we fetch buser db?
        """
        busers = db.fetch_busers()
        self.assertIsInstance(busers, list)

    def test_fetch_cuser(self):
        """
        Can we fetch cuser db?
        """
        cusers = db.fetch_cusers()
        self.assertIsInstance(cusers, list)
