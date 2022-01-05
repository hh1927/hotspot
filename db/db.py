
"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""
import os

# This file will manage interactions with our data store.
# At first, it will just contain stubs that return fake data.
# Gradually, we will fill in actual calls to our datastore.

# import db.db_connect as dbc

DEMO_HOME = os.environ["DEMO_HOME"]
TEST_MODE = os.environ.get("TEST_MODE", 0)

if TEST_MODE:
    # this one should be changed!
    DB_NAME = "cuser_DB"
else:
    DB_NAME = "cloudDB"

# fields in db
NAME = "name"
AGE = "age"
CITY = "city"

OK = 0
NOT_FOUND = 1
DUPLICATE = 2
# client = dbc.get_client()
# if client is None:
#    print("Failed to connect to MongoDB.")
#    exit(1)

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


def fetch_cusers():
    '''
    A function to return all cusers in the data store.
    '''
    return {"Sara": ["woman", 25, ("clubbing", "brunch"), "NYC"],
            "John": ["man", 21, ("bars", "sports"), "NYC"],
            "Jane": ["woman", 32, ("art", "sports"), "NYC"]}

def get_busers():
    '''
    A function to return all cusers in the data store.
    '''
    return {"Catch": [("clubbing", "brunch"), "NYC"],
            "Penny Farthing": [("bars", "sports"), "NYC"],
            "Fleur Room": [("art", "clubbing"), "NYC"]}

def fetch_clientList():
    '''
    A function to returns list of clients,
    their sex, age, and size of additional party
    '''
    return {"Sara": ["woman", 25, 3],
            "John": ["man", 21, 1],
            "Jane": ["woman", 32, 5]}
