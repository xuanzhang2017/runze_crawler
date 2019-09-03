# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from zmt_video_crawler.items import ZmtVideoCrawlerItem
from utils.bloom_util import MyBloomUtil
from utils.user_agents import headers


class ZmkBaiduSpider(scrapy.Spider):
    name = 'zmk_baidu'
    allowed_domains = ['zimeika.com']

    # start_urls = ['https://www.zimeika.com/video/lists/haokan.html?cate_id=12&time_type=&read_order=&type=&author_id=&author_name=&title=%E6%89%8B%E6%9C%BA&p=11']

    def start_requests(self):
        for i in range(1, 101):
            url = 'https://www.zimeika.com/video/lists/haokan.html?cate_id=12&time_type=&read_order=&type=&author_id=&author_name=&title=华为手机&p=%d' % i
            yield scrapy.Request(url=url)

    def parse(self, response):
        print(response.url)
        driver = webdriver.PhantomJS()
        driver.get(response.url)
        details = driver.find_elements_by_xpath("//ul[@class='video-list']/li/a")
        # driver.close()
        for detail in details:
            detail_url = detail.get_attribute('href')
            yield scrapy.Request(detail_url, callback=self.parse_detail, headers=headers)

    def parse_detail(self, response):
        source_detail_url = response.url
        print('-----------source_detail_url=%s-------------' % source_detail_url)
        print('-----source_code--------:%s' % response.text)
        bfu = MyBloomUtil(self.name)
        if not bfu.process_item(source_detail_url):
            yield None
        title = response.xpath("//h1[@class='article-title']/a/text()").extract_first()
        video_url = response.xpath("//article/div[@class='content-text']/div[@class='thumbnail']/a/@href").extract_first()

        item = ZmtVideoCrawlerItem()
        item['source_detail_url'] = source_detail_url
        item['title'] = title
        item['video_url'] = video_url
        print('item = %s' % item)
        yield item
