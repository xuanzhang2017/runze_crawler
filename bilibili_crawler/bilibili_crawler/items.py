# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    detail_url = scrapy.Field()

