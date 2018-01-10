# -*- coding: utf-8 -*-

import scrapy


class NewsCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link_title = scrapy.Field()
    url = scrapy.Field()
    sentiment = scrapy.Field()
    text = scrapy.Field()
