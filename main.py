# Requires pymongo 3.6.0+
from pymongo import MongoClient

client = MongoClient("mongodb://host:port/")
database = client["mongo_db_conn1"]
collection = database["city"]

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

query = {}

cursor = collection.find(query)
try:
    for doc in cursor:
        print(doc)
finally:
    client.close()
