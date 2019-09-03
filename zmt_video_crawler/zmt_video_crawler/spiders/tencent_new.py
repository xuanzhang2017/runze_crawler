# -*- coding: utf-8 -*-
import scrapy
import os
from selenium import webdriver
import time


class TencentSpider(scrapy.Spider):
    name = 'tecent_new'
    allowed_domains = ['qq.com']
    start_urls = ['https://v.qq.com/vplus/69af131791104afad5b0b89a1ce27006#uin=69af131791104afad5b0b89a1ce27006?page=video']

    def parse(self, response):
        driver = webdriver.PhantomJS()
        driver.get(response.url)
        for i in range(20):
            driver.execute_script("window.scrollTo(0,3000)")
            time.sleep(1)
        details = driver.find_elements_by_xpath("//div[@id='_videolist_latest']/div[@class='list_item ']/a/@href | //div[@class='mod_feed_item']/div/a")
        print('detail_lenth = %d' % len(details))