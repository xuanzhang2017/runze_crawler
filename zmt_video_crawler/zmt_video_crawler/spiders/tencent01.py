# -*- coding: utf-8 -*-
import scrapy
import os
from multiprocessing import Pool
from zmt_video_crawler.items import ZmtVideoCrawlerItem


class TencentSpider(scrapy.Spider):
    name = 'tecent01'
    allowed_domains = ['qq.com']
    start_urls = [
        'https://v.qq.com/vplus/37052c929ab8ac20ced49e3d6d74a98f#uin=37052c929ab8ac20ced49e3d6d74a98f?page=video']

    def parse(self, response):
        detail_urls = [response.urljoin(url) for url in response.xpath(
            "//div[@id='_videolist_latest']/div[@class='list_item ']/a/@href | //div[@class='mod_feed_item']/div/a/@href").extract()]
        # for detail_url in detail_urls:
        #     print(detail_url)
        #     you_get_cmd = 'you-get %s -o /Users/xuan.zhang/Documents/videos/tencent/07/' % detail_url
        #     print(you_get_cmd)
        #     os.system(you_get_cmd)
        #
        #     # item = ZmtVideoCrawlerItem()
        #     # item['detail_url'] = detail_url
        #     # yield item

        pool = Pool(10)
        pool.map(self.download_detail, detail_urls)

    def download_detail(self, detail_url):
        you_get_cmd = 'you-get %s -o /Users/xuan.zhang/Documents/videos/tencent/07/' % detail_url
        print(you_get_cmd)
        os.system(you_get_cmd)
