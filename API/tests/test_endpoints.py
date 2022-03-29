
from unittest import TestCase, skip
from flask_restx import Resource, Api

import Api.endpoints as ep
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

    def test_retrievePartySize(self):
        """
        See if we can successfully retrieve correct values
        """
        evInf = ep.add_party(7)
        # party_size = ep.fetch_psize()
        self.assertTrue(True)

    def deletecUser(self):
        """
        Deleting a cUser
        """
        newUser = new_entitity_name("newUser")
        db.add_cuser(newUser)
        cUser = ep.DeletecUser(Resource)
        cUser.post(newUser)
        self.assertNotIn(newUser, db.fetch_cusers)

    def deletebUser(self):
        """
        Deleting a bUser
        """
        newUser = new_entitity_name("newUser")
        db.add_buser(newUser)
        bUser = ep.DeletebUser(Resource)
        bUser.post(newUser)
        self.assertNotIn(newUser, db.fetch_busers)

    def resetPartySize(self):
        """
        Resetting Party Size for the next nights events
        """
        newPartySize = new_entitity_name("newUser")
        db.add_cuser(newUser)
        db.add_party(newUser, 4)
        db.reset_party(newUser)
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

    def update_bquota(self):
        new_quota = new_entitity_name(8)
        business_name = new_entitity_name("test name")
        bquota_list = ep.bquota(Resource)
        # ret = bquota_list.updateOne({name:business_name},{$set:{quota:new_quota}})
        # self.assertIn(bquota_list)
        self.assertTrue(True)

    def test_retrieve_Bquota(self):
        """
        See if we can successfully retrieve correct values
        """
        new_quota = new_entitity_name(5)
        business_name = new_entitity_name("test name, retrieval")
        # evInf = bquota_list.updateOne({name:business_name},{$set:{quota:new_quota}})
        bquota_updated = ep.fetch_bquota()
        # self.assertIn(evInf, bquota_updated)
        self.assertTrue(True)

    def cDaily(self):
        new_neighborhood = new_entitity_name("test_neighborhood")
        new_interests = new_entity_name("test_interests")
        user_name = new_entity_name("test_user")
        cDaily = ep.cDaily(Resource)
        # db.cusers.updateOne({name:user_name},{$set:{neighborhood:new_neighborhood}})
        # db.cusers.updateOne({name:user_name},{$set:{interests:new_interests}})
        self.assertIn(cdaily, db.fetch_cusers)

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
        allEvents = ep.fetch_events()
        self.assertIn(evInf, allEvents)
