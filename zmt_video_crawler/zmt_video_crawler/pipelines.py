# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import json
import os
from utils.user_agents import headers
from zmt_video_crawler.items import ZmtVideoCrawlerItem


class ZmtVideoCrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class DownloadVideoPipeline(object):
    def process_item(self, item, spider):
        print('--------------------DownloadVideoPipeline-------------------------')
        # item = ZmtVideoCrawlerItem()
        print('item = %s' % json.dumps(dict(item)))
        video_local_path = item.get('video_local_path')
        resp = requests.get(item.get('video_url'), headers=headers)
        with open(video_local_path, 'wb') as f:
            f.write(resp.content)
        return item


class DownloadTecentVideoPipeline(object):
    def process_item(self, item, spider):
        detail_url = item.get('detail_url')
        you_get_cmd = 'you-get %s -o /Users/xuan.zhang/Documents/videos/tencent/07/' % detail_url
        print(you_get_cmd)
        os.system(you_get_cmd)
        return item
