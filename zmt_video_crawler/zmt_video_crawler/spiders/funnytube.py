# -*- coding: utf-8 -*-
import scrapy
from zmt_video_crawler.items import ZmtVideoCrawlerItem
from utils.bloom_util import MyBloomUtil

class MirchistatusSpider(scrapy.Spider):
    name = 'funnytube'
    allowed_domains = ['funnytube.in']

    start_urls = ['https://funnytube.in/videos/amazing-videos/']

    def parse(self, response):
        detail_urls = response.xpath("//div[@class='col-xl-3 col-sm-6 mb-3']/div/div/a[1]/@href").extract()
        for detail_url in detail_urls:
            print('detail_url = %s' % detail_url)
            yield scrapy.Request(detail_url, callback=self.parse_detail)

        next_url = response.xpath("//a[@class='btn btn-primary btn-lg btn-block border-none']/@href").extract_first()
        if next_url:
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        video_url = response.xpath("//div[@class='box mb-1 adblock']/a/@href").extract_first()
        bfu = MyBloomUtil(self.name)
        # if not bfu.is_exists(video_url):
        video_url = bfu.process_item(video_url)
        if video_url:
            video_title = response.xpath("//h1/a/text()").extract_first()
            video_path = '/Users/xuan.zhang/Documents/videos/funnytube/amazing_video/Amazing Video-%s.mp4' % video_title

            item = ZmtVideoCrawlerItem()
            item['video_url'] = video_url
            item['video_title'] = video_title
            item['video_local_path'] = video_path

            yield item
