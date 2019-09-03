# -*- coding: utf-8 -*-
import scrapy
import os
from utils.download_video import download
from utils.bloom_util import MyBloomUtil


class MirchistatusSpider(scrapy.Spider):
    name = 'mirchistatus'
    allowed_domains = ['mirchistatus.com']

    start_urls = ['https://mirchistatus.com/video/46/love_-_romantic_status_videos/new2old/1.html']

    def parse(self, response):
        detail_urls = [response.urljoin(x) for x in response.xpath("//div[@class='fl odd' or @class='fl even']/a/@href").extract()]
        for detail_url in detail_urls:
            print('detail_url = %s' % detail_url)
            yield scrapy.Request(detail_url, callback=self.parse_detail)

        page_urls = response.xpath("//div[@class='pgn']/a/@href").extract()
        if page_urls:
            next_url = response.urljoin(page_urls[-1])
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        video_url = response.urljoin(response.xpath("//div[@class='downLink']/a/@href").extract_first())
        bfu = MyBloomUtil(self.name)
        if not bfu.is_exists(video_url):
            video_title = response.xpath("//div[@class='fInfo']/descendant-or-self::div[@class='fi']/text()").extract_first()
            video_path = '/Users/xuan.zhang/Documents/videos/mirchistatus/%s.mp4' % video_title
            ret = download(video_url, video_path)
            if ret:
                bfu.add_in_bf(video_url)
