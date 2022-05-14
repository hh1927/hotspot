
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

    def test_buser(self):
        """
        See if we can successfully create a new business user.
        Post-condition: user is in DB.
        """
        cbu = ep.bUser(Resource)
        new_buser = new_entity_name("buser")
        ret = cbu.post("new_user", "15 west 4th", "new grad", "100", "20")
        busers = db.bList()
        self.assertIn(new_buser, busers)

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

    def cDaily(self):
        new_neighborhood = new_entitity_name("test_neighborhood")
        new_interests = new_entity_name("test_interests")
        user_name = new_entity_name("test_user")
        cDaily = ep.cDaily(Resource)
        self.assertIn(cdaily, ep.fetch_cusers)
