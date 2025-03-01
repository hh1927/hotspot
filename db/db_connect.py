"""
This file contains some common MongoDB code.
"""
import os
import json
import pymongo as pm
from pymongo.server_api import ServerApi
import bson.json_util as bsutil


# all of these will eventually be put in the env:
user_nm = "hotspot"
cloud_svc = "cluster0.q05tp.mongodb.net"
# hide later
passwd = "GdfqZFngsJV47rtk"
cloud_mdb = "mongodb+srv"
db_params = "retryWrites=true&w=majority"

db_nm = "hotspot"
#if int(os.environ.get("TEST_MODE", "")) == 1:
    #dn_nm = "hotspot"


REMOTE = "0"
LOCAL = "1"

client = None


def get_client():
    """
    This provides a uniform way to get the client across all uses.
    Returns a mongo client object... maybe we shouldn't?
    Also set global client variable.
    """
    global client
    if os.environ.get("LOCAL_MONGO", REMOTE) == LOCAL:
        print("Connecting to Mongo locally.")
        client = pm.MongoClient()
    else:
        print("Connecting to Mongo remotely.")
        print("HELLO " + f"mongodb+srv://{user_nm}:{passwd}@" + f"{cloud_svc}/{db_nm}?"
             + "retryWrites=true&w=majority")
        client = pm.MongoClient(f"mongodb+srv://{user_nm}:{passwd}@" + f"{cloud_svc}/{db_nm}?"
             + "retryWrites=true&w=majority"
         )
            
    '''if os.environ.get("LOCAL_MONGO", REMOTE) == LOCAL:
        print("Connecting to Mongo locally.")
    else:
        try:
            client = MongoClient('mongodb+srv://hotspot:{passwd}@cluster0.q05tp.mongodb.net/hotspot?retryWrites=true&w=majority')
        except:
            print("failed to connect to mongo")'''
    return client


def fetch_one(collect_nm, filters={}):
    """
    Fetch one record that meets filters.
    """
    return client[db_nm][collect_nm].find_one(filters)


def del_one(collect_nm, filters={}):
    """
    Delete one record that meets filters.
    """
    return client[db_nm][collect_nm].delete_one(filters)


def fetch_all(collect_nm, key_nm):
    all_docs = []
    for doc in client[db_nm][collect_nm].find():
        all_docs.append(json.loads(bsutil.dumps(doc)))
    return all_docs


def insert_doc(collect_nm, doc):
    return client[db_nm][collect_nm].insert_one(doc)


def update_fld(db_nm, collect_nm, filters, fld_nm, fld_val):
    return client[db_nm][collect_nm].update_one(filters, {'$set': {fld_nm: fld_val}},
                                                upsert=False)
