# -*- coding: utf-8 -*-
import pymongo
import logging
import sys
from scrapy.conf import settings

# See: Scrapy MongoDB reference http://doc.scrapy.org/en/latest/topics/item-pipeline.html?highlight=mongodb

class finder(object):
    
    def __init__(self):
        # connect MongoDB (local or server)
        # id/passwd for (Compose)access was defined at setting.py
        # MONGODB_SERVER is composed of userID/password and serviceURL at setting.py
        logging.info("MONGODB_SERVER info : %s ",settings['MONGODB_SERVER'])
        connection = pymongo.MongoClient(
                                         #define MONGODB ENV (MONGODB_SERVER,MONGODB_PORT,MONGODB_DB,MONGODB_COLLECTION)  at setting.py
                                         #Currntly Local MongoDB set for basic test
                                         settings['MONGODB_SERVER'],
                                         settings['MONGODB_PORT']
                                         )
            
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def search(self, keyword):
        print(keyword)
        keywordResult = self.collection.find({"keyword" : keyword})
        return keywordResult
    
if __name__ == "__main__":
    findermoudle = finder()
    result = findermoudle.search(sys.argv[1:])
    
    for item in result:
       print(item)