# -*- coding: utf-8 -*-

# initial application
import pymongo

# MongoDB init
# connect MongoDB (local or server)
# id/passwd for (Compose)access was defined at setting.py
# MONGODB_SERVER is composed of userID/password and serviceURL at setting.py
#logging.info("MONGODB_SERVER info : %s ",settings['MONGODB_SERVER'])

connection = pymongo.MongoClient("mongodb://hsboykjh:kjh3131@aws-us-east-1-portal.14.dblayer.com", 10095)

db = connection["test3"]
collection = db["news"]


# MongoDB find, Search function
# see Index function on MongoDB: https://docs.mongodb.org/v3.0/core/index-text/
# see Text Search no MongoDB: https://docs.mongodb.org/v3.0/tutorial/text-search-in-aggregation/

# Simple case : search item's keyword stored on MongoDB with the keyword.
keywordResult = collection.find({"keyword" : "NS"})

for item in keywordResult:
    print(item)

# Simple case : search item's headline stored on MongoDB with the keyword.
######### TO-DO ##############
# text search or find function certain data with partial string keyword
headlineResult = collection.find({"headline" : "NS"})


##############################
for item in headlineResult:
    print(item)
