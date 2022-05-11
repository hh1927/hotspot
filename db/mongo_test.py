# import sys
# import json
import pymongo as pm
client = pm.MongoClient()
print(client)

DB_NAME = 'hotspot'
BUSINESS = 'business'
CONSUMER = 'consumer'
EVENTS = 'events'

client = dbs.get_client()
print(f"{client=}")

business_collect = client[DB_NAME][BUSINESS]

insert_ret = business_collect.insert_many([{'filter_nm': 'bar1'},
                                      {'filter_nm': 'bar2'},
                                      {'filter_nm': 'bar3'},
                                      {'filter_nm': 'bar4'},
                                      {'filter_nm': 'bar5'}])
insert_ret = business_collect.insert_one({'trees': 'yellow leaves'})
print(f"{insert_ret=}")

docs = business_collect.find()
print(f"{docs=}")
for doc in docs:
    print(f"{doc=}")

doc = business_collect.find_one({'trees': 'yellow leaves'})
print(f"find one = {doc=}")

doc = business_collect.delete_many({'foo': 'bar'})
print(f"find one = {doc=}")

docs = business_collect.find()
for doc in docs:
    print(f"{doc=}")

consumer_collect = client[DB_NAME][CONSUMER]

insert_ret = consumer_collect.insert_many([{'filter_nm': 'bar1'},
                                      {'filter_nm': 'bar2'},
                                      {'filter_nm': 'bar3'},
                                      {'filter_nm': 'bar4'},
                                      {'filter_nm': 'bar5'}])
insert_ret = consumer_collect.insert_one({'trees': 'yellow leaves'})
print(f"{insert_ret=}")

docs = consumer_collect.find()
print(f"{docs=}")
for doc in docs:
    print(f"{doc=}")

doc = consumer_collect.find_one({'trees': 'yellow leaves'})
print(f"find one = {doc=}")

doc = consumer_collect.delete_many({'foo': 'bar'})
print(f"find one = {doc=}")

docs = consumer_collect.find()
for doc in docs:
    print(f"{doc=}")

events_collect = client[DB_NAME][EVENTS]

insert_ret = events_collect.insert_many([{'filter_nm': 'bar1'},
                                      {'filter_nm': 'bar2'},
                                      {'filter_nm': 'bar3'},
                                      {'filter_nm': 'bar4'},
                                      {'filter_nm': 'bar5'}])
insert_ret = events_collect.insert_one({'trees': 'yellow leaves'})
print(f"{insert_ret=}")

docs = events_collect.find()
print(f"{docs=}")
for doc in docs:
    print(f"{doc=}")

doc = events_collect.find_one({'trees': 'yellow leaves'})
print(f"find one = {doc=}")

doc = events_collect.delete_many({'foo': 'bar'})
print(f"find one = {doc=}")

docs = events_collect.find()
for doc in docs:
    print(f"{doc=}")
