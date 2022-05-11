"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""
import os

# This file will manage interactions with our data store.
# At first, it will just contain stubs that return fake data.
# Gradually, we will fill in actual calls to our datastore.

import db.db_connect as dbc

HOTSPOT_HOME = os.environ["HOTSPOT_HOME"]
# TEST_MODE = os.environ.get("TEST_MODE", 0)

# if TEST_MODE:
# this one should be changed!
# DB_NAME = "cuser_DB"
# else:
# DB_NAME = "cloudDB"

CUSERS = "consumer"
BUSERS = "business"
EVENTS = "events"

# fields in db
CUSER_NM = "username"
AGE = "age"
INTERESTS = "interests"
NEIGHBORHOOD = "neighborhood"
PARTY_SIZE = "party_size"


BUSER_NM = "business_name"
AGE_RESTRICTIONS = "age_restrictions"
USERNAME = "username"
QUOTA = "quota"
BUSINESS_TYPE = "business_type"


EVENT_NM = "event_name"
ADDRESS = "address"
FEE = "fee"
HOURS = "hours"







OK = 0
NOT_FOUND = 1
DUPLICATE = 2

client = dbc.get_client()
if client is None:
    print("Failed to connect to MongoDB.")
    exit(1)

# def create_cuser(name, demographic, age, categories, location):
#    """
#    A function that will save a user to the data base
#    """
#    user = {"name": name,
#            "age": age,
#            "demographic": demographic,
#            "Interest Categories": categories,
#            "location": location}
#    create = json.dumps(user)
#    print(create)


def buser_exists(busername):
    """
    See if a buser with the business name is in the db.
    Returns True or False.
    """
    rec = dbc.fetch_one(BUSERS, filters={BUSER_NM: busername})
    print(f"{rec=}")
    return rec is not None


def cuser_exists(cusername):
    """
    See if a cuser with username is in the db.
    Returns True or False.
    """
    rec = dbc.fetch_one(CUSERS, filters={CUSER_NM: cusername})
    print(f"{rec=}")
    return rec is not None


def fetch_cusers():
    """
    A function to return all cusers in the data store.
    """
    return dbc.fetch_all(CUSERS, CUSER_NM)
    """return {"Sara": ["woman", 25, ("clubbing", "brunch"), "NYC"],
            "John": ["man", 21, ("bars", "sports"), "NYC"],
            "Jane": ["woman", 32, ("art", "sports"), "NYC"]}"""


def fetch_busers():
    """
    A function to return all busers in the data store.
    """
    return dbc.fetch_all(BUSERS, BUSER_NM)
    """
    return {
        "Catch": [("clubbing", "brunch"), "NYC"],
        "Penny Farthing": [("bars", "sports"), "NYC"],
        "Fleur Room": [("art", "clubbing"), "NYC"],
    }
    """

def fetch_events():
    """
    A function to return all events in the data store.
    """
    #return dbc.fetch_all(EVENTS, EVENT_NM, LOCATION, PRICE, HOURS)
    return dbc.fetch_all(EVENTS, EVENT_NM)

def add_buser(age_restrictions,buser_nm,business_type,business_name,quota):
    """
    Add a buser to business db
    """
    if buser_exists(buser_nm):
        return DUPLICATE
    else:
        dbc.insert_doc(
           BUSERS,
                {
                    AGE_RESTRICTIONS: age_restrictions,
                    BUSER_NM: buser_nm,
                    BUSINESS_TYPE: business_type,
                    QUOTA: quota,
                    USERNAME: business_name
                },
            )
        return OK


def add_cuser(cuser_nm,age,interests,neighborhood,party_size):
    """
    Add a cuser to business db
    """
    if cuser_exists(cuser_nm):
        return DUPLICATE
    else:
        dbc.insert_doc(
            CUSERS,
            {
                CUSER_NM: cuser_nm,
                AGE: age,
                INTERESTS: interests,
                NEIGHBORHOOD: neighborhood,
                PARTY_SIZE: party_size
            },
        )
        return OK

def fetch_clientList(busername):
    """
    A function to returns list of clients,
    their sex, age, and size of additional party
    """
    return dbc.fetch_all(CUSERS, CUSER_NM, AGE, PARTY, {"owner": busername})
    """return {"Sara": ["woman", 25, 3],
            "John": ["man", 21, 1],
            "Jane": ["woman", 32, 5]}"""
    
def reset_party(username):
    """
    reset party sizes at the end of the night - CHECK AGAIN
    """
    if cuser_exists(username):
        dbc.insert_doc(CUSERS, {CUSER_NM: username}, {PARTY: 0})
        return OK
    else:
        return OK
        

def add_party(username, party):
    """
    Add party sizes to the user database.
    """
    if cuser_exists(username):
        dbc.insert_doc(CUSERS, {CUSER_NM: username}, {PARTY: party})
        return OK


def get_party(username):
     """
     Function to return user's party size
     """
     # temporarily hard coded
     return 4
     """
     cusers = db.fetch_one(CUSERS, filters={USER_NM: username})
     psize = cusers[PARTY]
     return psize
     """

def event_exists(buser_nm):
    """
    See if a event already exists in the db.
    Returns True or False.
    """
    rec = dbc.fetch_one(EVENTS, filters={BUSER_NM: buser_nm})
    print(f"{rec=}")
    return rec is not None

def add_event(buser_nm, eventName, address, fee, hours):
     """
    Add events to the event database.
    """
     if event_exists(buser_nm):
        return DUPLICATE
     else:
        dbc.insert_doc(
            EVENTS,
            {
                BUSER_NM: buser_nm,
                EVENT_NM: eventName,
                ADDRESS: address,
                FEE: fee,
                HOURS: hours,
            },
        )
        return OK
    
def del_event(buser_nm):
    """
    Delete event from the db.
    """
    if not event_exists(buser_nm):
        return NOT_FOUND
    else:
        dbc.del_one(EVENTS, filters={BUSER_NM: buser_nm})
        return OK
    
def del_buser(buser_nm):
    """
    Delete event from the db.
    """
    if not buser_exists(buser_nm):
        return NOT_FOUND
    else:
        dbc.del_one(BUSERS, filters={BUSER_NM: buser_nm})
        return OK
    
def del_cuser(cuser_nm):
    """
    Delete event from the db.
    """
    if not cuser_exists(cuser_nm):
        return NOT_FOUND
    else:
        dbc.del_one(CUSERS, filters={CUSER_NM: cuser_nm})
        return OK


def update_bquota(bUser, new_quota):
    """
    Update old bquota in db.
    """
    if not buser_exists(bUser):
        return NOT_FOUND
    else:
        dbc.update_one(USERS, filters={BUSER_NM: bUser},
                       updates={"$set": {QUOTA: new_quota}})
    return OK
                       
def update_cdaily(cUser, new_interests, new_neighborhood):
    """
    Update consumers new interests and neighborhood
    """
    if not cuser_exists(cUser):
        return NOT_FOUND
    else:
        dbc.update_one(USERS, filters={USER_NM: cUser},
                       updates={"$set": {INTERESTS: new_interests}})
        dbc.update_one(USERS, filters={USER_NM: cUser},
                       updates={"$set": {LOCATION: new_neighborhood}})
    return OK  
                                
def fetch_psize(cUser, psize):
    """
    Finding the party size 
    """
    if not cuser_exists(cUser):
        return NOT_FOUND
    else:
        dbc.fetch_one(PARTY, filters={USER_NM: cUser})
    return OK
                                
                                
