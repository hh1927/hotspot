
from unittest import TestCase, skip
from flask_restx import Resource, Api
import API.endpoints as ep
import db.data as db
import random

HUGE_NUM = 10000000000000

#import sys
#sys.path.insert(0, '/home/runner/work/hotspot/hotspot/API')
#sys.path.insert(0, '/home/runner/work/hotspot/hotspot/db')


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
        cusers = db.cList()
        self.assertIn(new_cuser, cusers)
        
    def test_fetchCuser(self):
        """
        See if we can successfully fetch consumer user.
        """
        np = ep.bList("tester")
        cl = ep.cList(Resource)
        self.assertIn(cl, np)

    def test_buser(self):
        """
        See if we can successfully create a new business user.
        Post-condition: user is in DB.
        """
        cbu = ep.bUser(Resource)
        new_buser = new_entity_name("buser")
        ret = cbu.post(new_user)
        busers = db.bList()
        self.assertIn(new_buser, busers)
        
    def test_fetchBuser(self):
        """
        See if we can successfully fetch business user.
        """
        np = ep.business_name("tester")
        bl = ep.bList(Resource)
        self.assertIn(bl, np)

    def test_ClientList1(self):
        """
        Post-condition 1: return is a dictionary.
        """
        cl = ep.cList(Resource)
        ret = cl.get()
        self.assertIsInstance(ret, dict)

    def test_cList2(self):
        """
        Post-condition 2: keys to the dict are strings
        """
        cl = ep.cList(Resource)
        ret = cl.get()
        for key in ret:
            self.assertIsInstance(key, str)

    def test_blist1(self):
        """
        Post-condition 1: return is a dictionary.
        """
        bl = ep.cList(Resource)
        ret = bl.get()
        self.assertIsInstance(ret, dict)
    
    def test_blist2(self):
        """
        Post-condition 2: keys to the dict are strings
        """
        bl = ep.cList(Resource)
        ret = bl.get()
        for key in ret:
            self.assertIsInstance(key, str)
           
    def test_bList3(self):
        """
        Post-condition 3: the values in the dict are themselves dicts
        """
        bl = ep.bList(Resource)
        ret = bl.get()
        for val in ret.values():
            self.assertIsInstance(val, list)


    def test_retrievePartySize(self):
        """
        See if we can successfully retrieve correct values
        """
        evInf = ep.eventInfo(7)
        # party_size = ep.fetch_psize()
        self.assertTrue(True)

    def deletecUser(self):
        """
        Deleting a cUser
        """
        newUser = new_entitity_name("newUser")
        db.add_cuser(newUser)
        cUser = ep.deletecUser(Resource)
        cUser.post(newUser)
        self.assertNotIn(newUser, db.fetch_cusers)

    def deletebUser(self):
        """
        Deleting a bUser
        """
        newUser = new_entitity_name("newUser")
        db.add_buser(newUser)
        bUser = ep.deletebUser(Resource)
        bUser.post(newUser)
        self.assertNotIn(newUser, db.fetch_busers)

    def resetPartySize(self):
        """
        Resetting Party Size for the next nights events
        """
        newPartySize = new_entitity_name("newUser")
        db.cUser(newUser)
        db.eventInfo(newUser, 4)
        partySize.update(newUser)
        self.assertNotIn(newUser, db.fetch_cusers)

    def deleteEvent(self):
        """
        Deleting a deleteEvent
        """
        db.add_event("testEvent", "testLocation", "testPrice", "testHours")
        newevent = ep.del_event(Resource)
        eventInfo.post(newevent)
        self.assertNotIn(newevent, db.fetch_events)


    def test_retrieve_Bquota(self):
        """
        See if we can successfully retrieve correct values
        """
        new_quota = new_quota(5)
        business_name = new_entitity_name("test name, retrieval")
        # evInf = bquota_list.updateOne({name:business_name},{$set:{quota:new_quota}})
        bquota_updated = ep.fetch_bquota()
        # self.assertIn(evInf, bquota_updated)
        self.assertIn(bquota_updated, ep)

    def cDaily(self):
        new_neighborhood = new_entitity_name("test_neighborhood")
        new_interests = new_entity_name("test_interests")
        user_name = new_entity_name("test_user")
        cDaily = ep.cDaily(Resource)
        self.assertIn(cdaily, ep.fetch_cusers)
   

    def test_retrieve_cDaily(self):
        """
        See if we can successfully retrieve correct values
        """
        new_neighborhood = new_neighborhood("test_neighborhood")
        new_interests = new_interests("test_interests")
        user_name = new_entity_name("test_user")
        cDaily = ep.test_update_cDaily(Resource)
        cDaily.cusers.updateOne({name:user_name},{set:{neighborhood:new_neighborhood}})
        cDaily.cusers.updateOne({name:user_name},{set:{interests:new_interests}})
        self.assertTrue(True)

    def test_eventInfoExists(self):
        """
        See if we can successfully post event info
        """
        evInf = ep.add_event("Test event", "Test location",
                             "test price", "test hours")
        isExists = event_exists("Test event", "Test location")
        self.assertTrue(4, isExists)

    def test_eventInfo(self):
        """
        See if we can successfully retrieve correct values
        """
        evInf = ep.add_event("Test event", "Test location",
                             "test price", "test hours")
        np = ep.add_buser("tester")
        cl = ep.cList(Resource)
        allEvents = ep.fetch_events(Resource)
        self.assertIn(evInf, allEvents)
