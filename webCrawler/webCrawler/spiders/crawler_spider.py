# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import logging
from scrapy import Spider
from scrapy.selector import Selector
from webCrawler.items import WebcrawlerItem


class crawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["theguardian.com"]
    start_urls = ["http://www.theguardian.com",]
    
    def parse(self, response):
        news = Selector(response).xpath('//div[@class="fc-item__content"]')
        
        #logging.info("NEWS info : %s", news.extract())
        
        for topic in news:
            #logging.info("TOPIC info : %s", topic.extract())
            item = WebcrawlerItem()
            item['article_url'] = topic.xpath('div/h2/a[@class="fc-item__link"]/@href').extract()
            item['keyword'] = topic.xpath('div/h2/a/span[@class="fc-item__kicker"]/text()').extract()
            item['headline'] = topic.xpath('div/h2/a/span/span[@class="js-headline-text"]/text()').extract()
            item['article_text'] = topic.xpath('div[@class="fc-item__standfirst"]/text()').extract()
            #logging.info("ITEM info : %s , %s , %s , %s", item['article_url'] , item['keyword'] , item['headline'] , item['article_text'])
            yield item


