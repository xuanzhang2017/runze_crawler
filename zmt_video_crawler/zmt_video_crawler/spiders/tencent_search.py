# -*- coding: utf-8 -*-
import scrapy
import os
from zmt_video_crawler.items import ZmtVideoCrawlerItem


class TencentSearchSpider(scrapy.Spider):
    name = 'tecent_search'
    allowed_domains = ['qq.com']
    search_words = ['华为 美国']
    # search_words = ['燕双鹰']
    # search_words = ['牛人']
    # search_words = ['合集']
    # start_urls = ['https://v.qq.com/x/search/?ses=qid%3DM63UuDWnTBqs79djuwpf5qbaoBQkSKCo8NP3fXcyywwkQaq8KDLUkg%26last_query%3D%E9%BB%91%E8%80%81%E5%A4%A7%26tabid_list%3D0%7C1%7C2%7C7%7C3%7C4%7C6%7C5%7C17%7C8%7C15%26tabname_list%3D%E5%85%A8%E9%83%A8%7C%E7%94%B5%E5%BD%B1%7C%E7%94%B5%E8%A7%86%E5%89%A7%7C%E5%85%B6%E4%BB%96%7C%E7%BB%BC%E8%89%BA%7C%E5%8A%A8%E6%BC%AB%7C%E7%BA%AA%E5%BD%95%E7%89%87%7C%E9%9F%B3%E4%B9%90%7C%E6%B8%B8%E6%88%8F%7C%E5%8E%9F%E5%88%9B%7C%E6%95%99%E8%82%B2%26resolution_tabid_list%3D0%7C1%7C2%7C3%7C4%7C5%26resolution_tabname_list%3D%E5%85%A8%E9%83%A8%7C%E6%A0%87%E6%B8%85%7C%E9%AB%98%E6%B8%85%7C%E8%B6%85%E6%B8%85%7C%E8%93%9D%E5%85%89%7CVR&q=%E9%BB%91%E8%80%81%E5%A4%A7&needCorrect=%E9%BB%91%E8%80%81%E5%A4%A7&stag=4&filter=sort%3D0%26pubfilter%3D1%26duration%3D0%26tabid%3D0%26resolution%3D0#!filtering=1']
    def start_requests(self):
        for i in range(1, 3):
            for search_word in self.search_words:
                list_url = 'https://v.qq.com/x/search/?q=' + search_word + '&cur=' + str(
                    i) + '&cxt=tabid%3D0%26sort%3D0%26pubfilter%3D1%26duration%3D0'
                yield scrapy.Request(url=list_url, callback=self.parse)

    def parse(self, response):
        print('response.url = %s' % response.url)
        detail_urls = response.xpath("//h2[@class='result_title']/a/@href").extract()
        for detail_url in detail_urls:
            print(detail_url)
            you_get_cmd = 'you-get %s -o /Users/xuan.zhang/Documents/videos/tencent/05/' % detail_url
            print(you_get_cmd)
            os.system(you_get_cmd)
