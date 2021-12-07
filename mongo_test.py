import sys
import json
import pymongo as pm
#from pymongo.server_api import ServerApi

#import mongo_connect as mc

client = pm.MongoClient()
print(client)
db = client["DesignDB"]
print(db)
