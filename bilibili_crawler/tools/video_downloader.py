# coding=utf8

from utils.SQSUtil import ImportCrawledData
import config
import json
import time
import os

receive_test_sqs = ImportCrawledData(
    region_name="ap-south-1",
    endpoint='https://sqs.ap-south-1.amazonaws.com/715749150787/joyshare_tiktok_local',
    queue_name='joyshare_tiktok_local'

)

while True:
    sqs_list = receive_test_sqs.receive()
    # 如果消息队列为空，则睡眠
    if len(sqs_list) == 0:
        # print('-----------4-----------')
        # time.sleep(settings.SLEEP_TIME)
        # logger.info('The sqs is empty，sleep for [%s] seconds' % settings.SLEEP_TIME)
        time.sleep(config.SLEEP_TIME)
        continue
    for msg in sqs_list:
        # logger.info('===============================================')

        # print('-----------5-----------')
        # 读消息队列
        # sqs_res = sqs_list[0]
        sqs_res = msg.body
        # logger.debug('msg.body=%s' % sqs_res)

        # print sqs_res
        # print type(sqs_res)
        if type(sqs_res) == dict:
            video_metadata = sqs_res
        else:
            video_metadata = json.loads(sqs_res)
        # 打平metadata
        # logger.debug('will start plat metadata.')

        detail_url = video_metadata.get('detail_url')
        title = video_metadata.get('title')

        you_get_cmd = 'you-get %s -O \'%s.mp4\' -o \'../videos\'' % (detail_url, title)
        print('you_get_cmd = %s' % you_get_cmd)
        os.system(you_get_cmd)
        msg.delete()
        continue
