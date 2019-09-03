# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZmtVideoCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # source_detail_url = scrapy.Field()
    # title = scrapy.Field()
    video_url = scrapy.Field()
    video_title = scrapy.Field()
    video_local_path = scrapy.Field()

