# -*- coding: utf-8 -*-
import scrapy
from bilibili_crawler.items import BilibiliCrawlerItem


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']

    # start_urls = ['http://bilibili.com/']

    def start_requests(self):
        url = 'https://search.bilibili.com/all?keyword=%E6%8A%96%E9%9F%B3&from_source=banner_search&order=pubdate&duration=1&tids_1=0&single_column=1'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        li_list = response.xpath("//ul[contains(@class,'video-contain')]/li")
        for li in li_list:
            detail_url = response.urljoin(li.xpath("a/@href").extract_first())
            title = li.xpath("div[@class='info']/div/a[@class='title']/@title").extract_first()

            print(detail_url)
            print(title)
            print('-------------------')

            biliItem = BilibiliCrawlerItem()
            biliItem['detail_url'] = detail_url
            biliItem['title'] = title
            yield biliItem
