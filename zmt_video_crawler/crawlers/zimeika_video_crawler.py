# coding=utf8

import sys

sys.path.append('../')
sys.path.append('../utils')

from selenium import webdriver
from utils.bloom_util import MyBloomUtil
from utils.log_util import logger
from utils.user_agents import headers
from lxml import etree
import requests
import datetime
import os
import time
import json

# 抓取页数
page_num = 81


def crawl(search_word, page_num):
    for i in range(1, page_num + 1):
        try:
            list_url = 'http://zimeika.com/video/lists/haokan.html?cate_id=&time_type=&read_order=2&type=&author_id=&author_name=&title=%s&p=%d' % (
                search_word, i)
            print('list_url = %s' % list_url)
            parse_list(list_url, search_word)
        except Exception as e:
            logger.info(e)
            continue


def parse_list_with_selenium(list_url, search_word):
    driver = webdriver.PhantomJS()
    driver.get(list_url)
    details = driver.find_elements_by_xpath("//ul[@class='video-list']/li/a")
    # driver.close()
    for detail in details:
        try:
            detail_url = detail.get_attribute('href')
            parse_detail(detail_url, search_word)
        except Exception as e:
            logger.info(e)
            continue


def parse_list(list_url, search_word):
    html = requests.get(list_url, headers=headers).text
    text = etree.HTML(html)
    detail_urls = text.xpath("//ul[@class='video-list']/li/a/@href")
    for url in detail_urls:
        try:
            detail_url = 'https://www.zimeika.com' + url
            parse_detail(detail_url, search_word)
        except Exception as e:
            logger.info(e)
            continue


def parse_detail(detail_url, search_word):
    bfu = MyBloomUtil(search_word)
    processed_detail_url = bfu.process_item(detail_url)
    if not processed_detail_url:
        logger.info('%s has already been crawled.' % detail_url)
        return
    html = requests.get(processed_detail_url, headers=headers).text
    text = etree.HTML(html)
    title = text.xpath("//h1[@class='article-title']/a/text()")[0]
    video_url = text.xpath("//article/div[@class='content-text']/div[@class='thumbnail']/a/@href")[0]
    print('title = %s' % title)
    print('video_url = %s' % video_url)
    download_video(title, video_url, search_word)
    save_info(title, video_url, search_word)
    time.sleep(1)


def save_info(title, video_url, search_word):
    videos_csv = search_word + '.json'
    item = {
        'title': title,
        'video_url': video_url
    }
    with open(videos_csv, 'a', encoding='utf-8-sig') as f:
        f.write(json.dumps(item) + '\n')


def download_video(title, video_url, search_word):
    min = datetime.datetime.now().minute
    min_in_dir = min % 12
    cur_time = datetime.datetime.now().strftime("%Y%m%d%H")
    # video_dir = '/Users/xuan.zhang/Documents/videos/baiduhaokan/' + search_word + '/' + cur_time + str(min_in_dir)
    video_dir = '/Users/xuan.zhang/Documents/videos/baiduhaokan/' + search_word + '/' + cur_time + str(min_in_dir)

    if not os.path.exists(video_dir):
        os.makedirs(video_dir)
    video_path = video_dir + '/' + title + '.mp4'
    content = requests.get(video_url, timeout=30).content
    with open(video_path, 'wb') as f:
        f.write(content)


def main():
    search_words = ['抖音']
    for search_word in search_words:
        crawl(search_word, page_num)


if __name__ == '__main__':
    main()
