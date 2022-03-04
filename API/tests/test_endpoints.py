from unittest import TestCase, skip 
from flask_restx import Resource, Api
import random
import sys 
sys.path.insert(0,'/home/runner/work/hotspot/hotspot/API')
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
        ccu = ep.CreateCuser(Resource)
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
        ret = cbu.post(new_user)
        busers = db.get_busers()
        self.assertIn(new_buser, busers)
    
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

 
    def test_partySize(self):
        """
        See if we can successfully post party size
        """
        np = ep.add_Party(Resource)
        username = "tester"
        add_cuser(username)
        db.add_party(username, 4)
        ret = np.post(username)
        print(f'post {ret=}')
        psize = get_party(username)
        print(f'{psize=}')
        self.assertIn(4, psize)
        
     def deletecUser(self):
        """
        Deleting a cUser
        """
        newUser = new_entitity_name("newUser")
        db.add_cuser(newUser)
        cUser = ep.DeletecUser(Resource)
        cUser.post(newUser)
        self.assertNotIn(newUser, db.get_cusers)
        
     def deletebUser(self):
        """
        Deleting a bUser
        """
        newUser = new_entitity_name("newUser")
        db.add_buser(newUser)
        bUser = ep.DeletebUser(Resource)
        bUser.post(newUser)
        self.assertNotIn(newUser, db.get_busers)
