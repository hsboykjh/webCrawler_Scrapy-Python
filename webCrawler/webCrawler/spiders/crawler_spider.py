# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import logging
from scrapy import Spider
from scrapy.selector import Selector
from webCrawler.items import WebcrawlerItem

# Spider reference : http://doc.scrapy.org/en/latest/topics/spiders.html

class crawlerSpider(Spider):
    name = "crawler"
    
    # web-site URL for crawling
    allowed_domains = ["theguardian.com"]
    
    # start url for crawling
    start_urls = ["http://www.theguardian.com/au",]
    
    def parse(self, response):
        # set the delimeter to devide each news content.
        news = Selector(response).xpath('//div[@class="fc-item__content"]')
        
        # check the contents would be seperated by each topic in a page.
        #logging.info("NEWS info : %s", news.extract())
        
        
        # each contents should be idendified to item's categories.
        # the item's data structure is defined at items.py (WebcrawlerItem)
        for topic in news:
            
            #logging.info("TOPIC info : %s", topic.extract())
            item = WebcrawlerItem()
            
            # news_article URL information
            item['article_url'] = topic.xpath('div/h2/a[@class="fc-item__link"]/@href').extract()

            # major keyword of the news contents. it is defined as fc-item__kicker on the web
            item['keyword'] = topic.xpath('div/h2/a/span[@class="fc-item__kicker"]/text()').extract()
            
            # news headline
            item['headline'] = topic.xpath('div/h2/a/span/span[@class="js-headline-text"]/text()').extract()

            # news contents text
            item['article_text'] = topic.xpath('div[@class="fc-item__standfirst"]/text()').extract()
            
            #logging.info("ITEM info : %s , %s , %s , %s", item['article_url'] , item['keyword'] , item['headline'] , item['article_text'])
            yield item
