"""
This file contains some common MongoDB code.
"""
import os
import json
import pymongo as pm
import bson.json_util as bsutil
from   pymongo.server_api import ServerApi

# all of these will eventually be put in the env:
user_nm = "ab8541@nyu.edu"
cloud_db = "serverlessinstance0.irvgp.mongodb.net"
#cloud_svc = "serverlessinstance0.mvrqy.mongodb.net"
passwd = os.environ.get("MONGO_PASSWD", 'test1234$')
cloud_mdb = "mongodb+srv"
db_params = "retryWrites=true&w=majority"
db_nm = "hotspot-mongo"

client = None


def get_client():
    """
    This provides a uniform way to get the client across all uses.
    Returns a mongo client object... maybe we shouldn't?
    Also set global client variable.
    """
    global client
    if os.environ.get("LOCAL_MONGO", False):
        client = pm.MongoClient()
    else:
        server_api=ServerApi('1')
        client = pm.MongoClient \
        (   \
            f"mongodb+srv://{user_nm}:{passwd}@"    \
            + f"{cloud_db}/{db_nm}?"    \
            + "retryWrites=true&w=majority",    \
            server_api=server_api, tls=True,    \
            tlsAllowInvalidCertificates=True
        )
    return client


def fetch_all(collect_nm, key_nm):
    all_docs = []
    for doc in client[db_nm][collect_nm].find():
        # print(doc)
        all_docs.append(json.loads(bsutil.dumps(doc)))
    return all_docs


def insert_doc(collect_nm, doc):
    client[db_nm][collect_nm].insert_one(doc)

def fetch_one(collect_nm, filters={}):
    """
    Fetch one record that meets filters.
    """
    return client[db_nm][collect_nm].find_one(filters)


def del_one(collect_nm, filters={}):
    """
    Fetch one record that meets filters.
    """
    return client[db_nm][collect_nm].delete_one(filters)
