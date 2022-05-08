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
    try:
        client = MongoClient(f"mongodb+srv://hotspot:{passwd}@cluster0.q05tp.mongodb.net/hotspot?retryWrites=true&w=majority")
    except:
        print("failed to connect to mongo")
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
    client[db_nm][collect_nm].insert_one(doc)
