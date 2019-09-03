# coding=utf8
from __future__ import print_function  # Python 2/3 compatibility

import json

import boto3
import logging
import time
import datetime
import config
from boto3.dynamodb.conditions import Key


class ImportCrawledData(object):

    def __init__(self, endpoint, region_name, queue_name):
        self._sqs = boto3.resource('sqs', region_name=region_name, endpoint_url=endpoint)
        self._queue = self._sqs.get_queue_by_name(QueueName=queue_name)

    def import_one_item(self, detail_info):
        try:
            self._queue.send_message(MessageBody=json.dumps(detail_info))
            logging.info("SQS:import successful.")
            return True
        except Exception as e:
            logging.error("SQS:import failed.")
            return False

    def get_item(self):
        return self._queue.receive_messages(MaxNumberOfMessages=10)

    # 从消息队列中接收消息
    def receive(self):
        results = []
        # , VisibilityTimeout = 3 * 3600
        messages = self._queue.receive_messages(MaxNumberOfMessages=int(config.SQS_RECEIVE_COUNT),
                                                VisibilityTimeout=60 * 3)
        for message in messages:
            # results.append(message.body)
            results.append(message)
            # message.delete()

        # time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # logging.info(time_str + " receive " + str(len(results)) + " messages")
        return results


if __name__ == '__main__':
    SQS_QUEUE = "app_crawled_metadata"
    REGION = "ap-south-1"
    ENDPOINT = "https://%s.ap-south-1.amazonaws.com/715749150787"
    icd = ImportCrawledData(endpoint=ENDPOINT, region_name=REGION, queue_name=SQS_QUEUE)
    detail_info = {
        'url': 'http://www.baidu.com',
        'id': 1
    }
    icd.import_one_item(detail_info)

    time.sleep(3)
    msg_list = icd.receive()
    # print(ret)
    msg_body = msg_list[0].body
    print(msg_body)
