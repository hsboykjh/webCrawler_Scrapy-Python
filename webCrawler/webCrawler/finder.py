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
    def search(self, field , keyword):
        # certain keyword search on "keyword" filed
        Result = self.collection.find({ field :{"$regex":keyword[0],"$options":""}})
        
        return Result
    
if __name__ == "__main__":
    
    # check the user's input parameter on CMD
    if len(sys.argv) == 2:
        # instance of finder class
        findermoudle = finder()
        # search Keyword on MongoDB 
        keywordresult = findermoudle.search("keyword", sys.argv[1:])    
        # result print
        print("############# KEYWORD SEARCH ############")
        for item in keywordresult:
           print(item)
        
        headlineresult = findermoudle.search("headline", sys.argv[1:])
        # result print
        print("############# HEADLINE SEARCH ############")
        for item in headlineresult:
           print(item)
        
        article_textresult = findermoudle.search("article_text", sys.argv[1:])
        print("############# ARTICLE TEXT SEARCH ############")
        for item in article_textresult:
           print(item)
        
           
    else:
        print("#########################################################")
        print("USAGE OF FINDER APPLICATION : >> python finder.py KEYWORD")
        print("#########################################################")