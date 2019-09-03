# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import boto3
import json
from utils.bloom_util import MyBloomUtil


class BilibiliCrawlerPipeline(object):
    def process_item(self, item, spider):
        # detail_url = item.get('detail_url')
        # title = item.get('title')
        # you_get_cmd = 'you-get %s -O \'%s.mp4\' -o \'./videos\'' % (detail_url, title)
        # print('you_get_cmd = %s' % you_get_cmd)
        # os.system(you_get_cmd)

        item = dict(item)

        bloom = MyBloomUtil(spider.name)
        item = bloom.process_item(item)

        SQS_QUEUE = 'joyshare_tiktok_local'
        REGION = "ap-south-1"
        ENDPOINT = 'https://sqs.ap-south-1.amazonaws.com/715749150787/joyshare_tiktok_local'
        sqs = boto3.resource('sqs', region_name=REGION, endpoint_url=ENDPOINT)
        queue = sqs.get_queue_by_name(QueueName=SQS_QUEUE)
        queue.send_message(MessageBody=json.dumps(item))
        return item
