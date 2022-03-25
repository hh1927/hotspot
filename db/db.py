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

CUSERS = "cusers"
BUSERS = "busers"
EVENTS = "events"

# fields in db
CUSER_NM = "cuserName"
BUSER_NM = "buserName"
EVENT_NM = "eventName"
LOCATION = "location"
PRICE = "price"
HOURS = "hours"
NAME = "name"
GENDER = "gender"
AGE = "age"
INTERESTS = "clubInterestType"
CITY = "city"
LOCATIONTYPE = "locationType"
PARTY = "sizeOfParty"
QUOTA = "quota"

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
    See if a buser with username is in the db.
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
    # return dbc.fetch_all(BUSERS, BUSER_NM)
    return {
        "Catch": [("clubbing", "brunch"), "NYC"],
        "Penny Farthing": [("bars", "sports"), "NYC"],
        "Fleur Room": [("art", "clubbing"), "NYC"],
    }

def fetch_events():
    """
    A function to return all events in the data store.
    """
    return dbc.fetch_all(EVENTS, EVENT_NM, LOCATION, PRICE, HOURS)

def add_buser(busername):
    """
    Add a buser to business db
    """
    if buser_exists(busername):
        return DUPLICATE
    else:
        dbc.insert_doc(
            BUSERS,
            {
                BUSER_NM: busername,
                "LocationType": ["bars, arts"],
                "City": "NYC",
            },
        )
        return OK


def add_cuser(cusername):
    """
    Add a cuser to business db
    """
    if cuser_exists(cusername):
        return DUPLICATE
    else:
        dbc.insert_doc(
            CUSERS,
            {
                CUSER_NM: cusername,
                "Gender": "xxxx",
                "Age": "00",
                "Interests": ["xxxx", "xxxx"],
                "Location": "NYC",
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
        dbc.insert_doc(CUSERS, {CUSER_NM: username}, {PARTY: 0}
        return ok
    else:
        return ok
        

def add_party(username, party):
    """
    Add party sizes to the user database.
    """
    if cuser_exists(username):
        dbc.insert_doc(CUSERS, {CUSER_NM: username}, {PARTY: party})
        return OK
    else:
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

def event_exists(eventName,location):
    """
    See if a event already exists in the db.
    Returns True or False.
    """
    rec = dbc.fetch_one(EVENTS, filters={LOCATION: location}, {EVENT_NM: eventName})
    print(f"{rec=}")
    return rec is not None

def add_event(eventName, location, price, hours):
     """
    Add events to the event database.
    """
     if event_exists(eventName, location):
        return DUPLICATE
    else:
        dbc.insert_doc(
            EVENTS,
            {
                EVENT_NM: eventName,
                LOCATION: location,
                PRICE: price,
                HOURS: hours,
            },
        )
        return OK
    
def del_event(eventName, location):
    """
    Delete event from the db.
    """
    if not event_exists(eventName, location):
        return NOT_FOUND
    else:
        dbc.del_one(EVENTS, filters={LOCATION: location}, {EVENT_NM: eventName})
        return OK

def update_bquota(bUser, new_quota):
    """
    Update old bquota in db.
    """
    if not buser_exists(bUser):
        return NOT_FOUND
    else:
        dbc.update_one(USERS, filters={USER_NM: bUser},
                       updates={"$set": {QUOTA: new_quota}})
    return OK
                       
