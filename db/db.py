
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

# fields in db
CUSER_NM = "cuserName"
BUSER_NM = "buserName"
NAME = "name"
GENDER = "gender"
AGE = "age"
INTERESTS = "clubInterestType"
CITY = "city"
LOCATIONTYPE = "locationType"

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


def buser_exists(username):
    """
    See if a buser with username is in the db.
    Returns True of False.
    """
    rec = dbc.fetch_one(BUSERS, filters={BUSER_NM: username})
    print(f"{rec=}")
    return rec is not None


def cuser_exists(username):
    """
    See if a cuser with username is in the db.
    Returns True of False.
    """
    rec = dbc.fetch_one(CUSERS, filters={CUSER_NM: username})
    print(f"{rec=}")
    return rec is not None


def fetch_cusers():
    '''
    A function to return all cusers in the data store.
    '''
    return dbc.fetch_all(CUSERS, CUSER_NM)
    '''return {"Sara": ["woman", 25, ("clubbing", "brunch"), "NYC"],
            "John": ["man", 21, ("bars", "sports"), "NYC"],
            "Jane": ["woman", 32, ("art", "sports"), "NYC"]}'''


def fetch_busers():
    '''
    A function to return all busers in the data store.
    '''
    return dbc.fetch_all(BUSERS, BUSER_NM)
    '''return {"Catch": [("clubbing", "brunch"), "NYC"],
            "Penny Farthing": [("bars", "sports"), "NYC"],
            "Fleur Room": [("art", "clubbing"), "NYC"]}'''


def add_buser(username):
    """
    Add a buser to business db
    """
    if user_exists(username):
        return DUPLICATE
    else:
        dbc.insert_doc(BUSERS, {BUSER_NM: username})
        return OK


def add_inv_response(username):
    """
    Add a user to the inv response db.
    """
    if user_exists(username):
        return DUPLICATE
    else:
        dbc.insert_doc(USERS, {USER_NM: username})
        return OK


def fetch_clientList():
    '''
    A function to returns list of clients,
    their sex, age, and size of additional party
    '''
    return {"Sara": ["woman", 25, 3],
            "John": ["man", 21, 1],
            "Jane": ["woman", 32, 5]}


def fetch_clientHist():
    '''
    A function to returns list of ALL PAST clients,
    their sex and age to the business
    '''
    return {"Sara": ["woman", 25],
            "John": ["man", 21],
            "Jane": ["woman", 32]}


def fetch_recList():
    '''
    A function to returns list of recommendations
    '''
    return {"Catch": ["10/21/1999", "10:00 PM", 21],
            "Penny Farthing": ["10/21/2000", "8:00 PM", 21],
            "Fleur Room": ["10/21/2001", "4:00 PM", 18]}


def fetch_revHist():
    '''
    A function to returns list of ALL past places visted and
    reviews out of 5 and date
    '''
    return {"Catch": ["10/21/1999", 4],
            "Penny Farthing": ["10/21/2000", 1],
            "Fleur Room": ["10/21/2001", 5]}


def fetch_invs():
    '''
    shows users invites with information
    on the event including company, date,
    time, and age requirement.
    '''
    return {"Catch": ["10/21/1999", "10:00 PM", 21],
            "Penny Farthing": ["10/21/2000", "8:00 PM", 21],
            "Fleur Room": ["10/21/2001", "4:00 PM", 18]}


def get_inv_response():
    '''
    A function to returns a list of invite info,
    including name, age, party size
    '''
    return ["Sara", 25, 3]


def fetch_clientType():
    '''
    A function to return client categories of interest
    '''
    return ["Sports Bar", "Club", "Speakeasy"]


def fetch_promos():
    '''
    A function to return that week's promos
    '''
    return {"Lady's night": ["Catch", "Penny Farthing"],
            "Happy hour": ["Fleur Room"],
            "Half price apps": ["Penny Farthing", "Fleur Room"]}


def fetch_invResponse():
    '''
    A function to return invite responses
    '''
    return {"Catch": ["Sara", 4],
            "Penny Farthing": ["John", 3]}
