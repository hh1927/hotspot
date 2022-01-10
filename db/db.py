"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import os

import db.db_connect as dbc

#HOTSPOT_HOME = os.environ["HOTSPOT_HOME"]
#print("test", DEMO_HOME)
#print("TEST", os.environ["DEMO_HOME"])

CUSER = "clientUsers"
BUSER = "businessUsers"

# field names in our DB: 
CLIENT_TYPE = "clientType"
PROMOS = "promos" 

# mongoDB connection
client = dbc.get_client()
if client is None:
    print("Failed to connect to MongoDB.")
    exit(1)
    
def fetch_clientTypes():
    """
    A function to return all the types of clients
    a business.
    """
    return dbc.fetch_all(BUSER, CLIENT_TYPE)


def fetch_busers():
    """
    A function to return all business info
    """
    return dbc.fetch_all(BUSER)


def fetch_promos():
    """
    A function to return all active promos
    """
    return dbc.fetch_all(PROMOS)

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
