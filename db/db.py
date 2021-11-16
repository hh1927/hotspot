"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""


def fetch_pets():
    """
    A function to return all pets in the data store.
    """
    return {"tigers": 2, "lions": 3, "zebras": 1}


def fetch_cusers():
    '''
    A function to return all cusers in the data store.
    '''
    return {"Sara": ["woman", 25, ("clubbing", "brunch"), "NYC"] , "John":["man",21, ("bars", "sports"), "NYC"], "Jane":["woman", 32, ("art", "sports"), "NYC"]}

