# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''
class WebcrawlerPipeline(object):
    def process_item(self, item, spider):
        return item
'''

import pymongo
import logging
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

# See: Scrapy MongoDB reference http://doc.scrapy.org/en/latest/topics/item-pipeline.html?highlight=mongodb

class MongoDBPipeline(object):
    
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

    def process_item(self, item, spider):
        
        # insert item into MongoDB
        # use update ( upsert option ) in order to prevent storing duplicated items
        self.collection.update({'keyword' : item['keyword'] , 'headline' : item['headline'] , 'article_url' : item['article_url'] , 'article_text' : item['article_text']}, dict(item) , upsert = True)

        #logging.info("PIPELINES ITEM info : %s || %s || %s || %s" , item['article_url'],item['article_text'],item['keyword'],item['headline'])
        
        return item