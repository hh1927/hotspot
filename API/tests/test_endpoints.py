from unittest import TestCase, skip 
from flask_restx import Resource, Api
import random
import API.endpoints as ep
import db.db as db

HUGE_NUM = 10000000000000  # any big number will do!

def new_entity_name(entity_type):
    int_name = random.randint(0, HUGE_NUM)
    return f"new {entity_type}" + str(int_name)

class EndpointTestCase(TestCase):
    def setUp(self):
         pass

    def tearDown(self):
         pass

    def test_hello(self):
        self.assertTrue(True)


    @skip("In the middle of making this work.")
    def test_cuser(self):
        """
        See if we can successfully create a new consumer user.
        Post-condition: user is in DB.
        """
        ccu = ep.Cuser(Resource)
        new_cuser = new_entity_name("user")
        ret = ccu.post(new_cuser)
        cusers = db.get_cusers()
        self.assertIn(new_cuser, cusers)
          
    def test_buser(self):
        """
        See if we can successfully create a new business user.
        Post-condition: user is in DB.
        """
        cbu = ep.Buser(Resource)
        new_buser = new_entity_name("buser")
        # ret = cbu.post(new_user)
        busers = db.get_busers()
        self.assertIn(new_buser, busers)
     
    def test_inv_response(self): 
        """
        See if we can successfully create a new invite.
        Post-condition: user is in DB.
        """
        inv_response = ep.Inv_Response(Resource)
        new_inv_response = new_entity_name("invite response")
        # ret = inv_response.post(new_inv_response)
        invite_responses = db.get_inv_response()
        self.assertIn(new_inv_response, invite_responses)
          
    def test_inv1(self): 
        """
        Post-condition 1: return is a dictionary.
        """
        invs = ep.Inv(Resource)
        ret = invs.get()
        self.assertIsInstance(ret, dict)
          
    def test_inv2(self):
        """
        Post-condition 2: keys to the dict are strings
        """
        invs = ep.Inv(Resource)
        ret = invs.get()
        for key in ret:
            self.assertIsInstance(key, str)

    def test_inv3(self):
        """
        Post-condition 3: the values in the dict are themselves dicts
        """
        invs = ep.Inv(Resource)
        ret = invs.get()
        for val in ret.values():
            self.assertIsInstance(val, dict)
    
    def test_ClientList1(self): 
        """
        Post-condition 1: return is a dictionary.
        """
        cl = ep.ClientList(Resource)
        ret = cl.get()
        self.assertIsInstance(ret, dict)
          
    def test_ClientList2(self):
        """
        Post-condition 2: keys to the dict are strings
        """
        cl = ep.ClientList(Resource)
        ret = cl.get()
        for key in ret:
            self.assertIsInstance(key, str)

    def test_ClientList3(self):
        """
        Post-condition 3: the values in the dict are themselves dicts
        """
        cl = ep.ClientList(Resource)
        ret = cl.get()
        for val in ret.values():
            self.assertIsInstance(val, list)
     
    def test_recList1(self):
        """
        Post-condition 1: return is a dictionary.
        """
        rl = ep.recList(Resource)
        ret = rl.get()
        self.assertIsInstance(ret, list)
          
    def test_recList2(self):
        """
        Post-condition 2: keys to the dict are strings
        """
        rl = ep.recList(Resource)
        ret = rl.get()
        for key in ret:
            self.assertIsInstance(key, str)

    def test_recList3(self):
        """
        Post-condition 3: the values in the dict are themselves dicts
        """
        rl = ep.recList(Resource)
        ret = rl.get()
        for val in ret.values():
            self.assertIsInstance(val, list)
     
     
