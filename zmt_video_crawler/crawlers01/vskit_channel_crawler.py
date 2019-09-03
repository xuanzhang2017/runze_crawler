# 接口https://video.vskit.tv/vskit/video/v3/activity/videolist?activity_id=616d47150f914b0ea2213b0bb1657b6dacid&page_id=4&order_type=1

import sys

sys.path.append('../')
sys.path.append('../utils')

import requests
import json
from utils.bloom_util import MyBloomUtil


def get_video_infos(url):
    video_infos = []
    resp = requests.get(url)
    metadata = json.loads(resp.text)
    # print(metadata)
    # print(type(metadata))
    # print(len(metadata.get('posts')))
    videos = metadata.get('data')
    for video in videos:
        video_info = {
            'video_url': video.get('rawl_video_url'),
            'title': 'short #prank video:' + video.get('title')
        }
        video_infos.append(video_info)
    return video_infos


def download_video(video_info):
    video_path = '/Users/xuan.zhang/Documents/videos/vskit/prank/%s.mp4' % video_info.get('title')
    bfu = MyBloomUtil('vskit')
    processed_url = bfu.process_item(video_info.get('video_url'))
    if processed_url:
        print('will start to download [%s]' % processed_url)
        resp = requests.get(processed_url)
        with open(video_path, 'wb') as f:
            f.write(resp.content)
    else:
        print('The video_url [%s] has already been downloaded.' % video_info.get('video_url'))


def crawl():
    for i in range(1, 12):
        url = 'https://video.vskit.tv/vskit/video/v3/activity/videolist?activity_id=616d47150f914b0ea2213b0bb1657b6dacid&page_id=%d&order_type=1' % i
        print('start to parse [%s]' % url)
        video_infos = get_video_infos(url)
        for video_info in video_infos:
            download_video(video_info)


if __name__ == '__main__':
    crawl()
