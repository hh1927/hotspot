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

    def test_get_cusers(self):
        """
        Can we fetch user db?
        """
        users = db.get_cusers()
        self.assertIsInstance(users, dict)
        
    def test_get_busers(self):
        """
        Can we fetch user db?
        """
        users = db.get_busers()
        self.assertIsInstance(users, dict)
        
      def test_get_event_info(self):
        """
        Can we fetch event_info db?
        """
        users = db.get_event_info()
        self.assertIsInstance(users, dict)
        
     def test_buser_exists(self): 
        """
        testing that buser_exists works
        """
        new_buser = ep.add_buser("tester")
        busers = db.get_busers()
        self.asserIn(new_buser, busers)
    
