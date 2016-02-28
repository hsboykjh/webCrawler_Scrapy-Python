# -*- coding: utf-8 -*-
import pymongo
import sys
from scrapy.conf import settings

# See: Scrapy MongoDB reference http://doc.scrapy.org/en/latest/topics/item-pipeline.html?highlight=mongodb

class finder(object):
    
    def __init__(self):
        # connect MongoDB (local or server)
        # id/passwd for (Compose)access was defined at setting.py
        # MONGODB_SERVER is composed of userID/password and serviceURL at setting.py
        connection = pymongo.MongoClient(
                                         #define MONGODB ENV (MONGODB_SERVER,MONGODB_PORT,MONGODB_DB,MONGODB_COLLECTION)  at setting.py
                                         #Currntly Local MongoDB set for basic test
                                         settings['MONGODB_SERVER'],
                                         settings['MONGODB_PORT']
                                         )
            
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
    # search keyword on mongoDB
    def search(self, keyword):
        print(keyword)
        keywordResult = self.collection.find({"keyword" : keyword})
        return keywordResult
    
if __name__ == "__main__":
    
    # check the user's input parameter on CMD
    if len(sys.argv) == 2:
        # instance of finder class
        findermoudle = finder()
        # search Keyword on MongoDB 
        result = findermoudle.search(sys.argv[1:])
    
        # result print
        for item in result:
           print(item)
        
        # TO-DO if the ohter search on the URL or content's text
        # ADD HERE THE CODE
           
    else:
        print("#########################################################")
        print("USAGE OF FINDER APPLICATION : >> python finder.py KEYWORD")
        print("#########################################################")