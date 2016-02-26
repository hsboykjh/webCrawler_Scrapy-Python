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

# See: MongoDB reference http://doc.scrapy.org/en/latest/topics/item-pipeline.html?highlight=mongodb

class MongoDBPipeline(object):
    
    collection_name = 'scrapy_items'
    
    def __init__(self):
        connection = pymongo.MongoClient(
                                         #define MONGODB ENV (MONGODB_SERVER,MONGODB_PORT,MONGODB_DB,MONGODB_COLLECTION)  at setting.py
                                         #Currntly Local MongoDB set for basic test
                                         #settings['MONGODB_SERVER'],
                                         #settings['MONGODB_PORT']
                                         "mongodb://hsboykjh:kjh3131@aws-us-east-1-portal.14.dblayer.com", 10095
                                         #/admin -u hsboykjh -p kjh3131"
        )
            
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        
        # insert item into MongoDB
        self.collection.insert({'keyword' : item['keyword'] , 'headline' : item['headline'] , 'article_url' : item['article_url'] , 'article_text' : item['article_text']})

        #logging.info("PIPELINES ITEM info : %s || %s || %s || %s" , item['article_url'],item['article_text'],item['keyword'],item['headline'])
        
        #self.collection.insert({'keyword' : "field2" , 'headline' : "field12" , 'article_url' : "field3" , 'article_text' : "field4"})
        return item
