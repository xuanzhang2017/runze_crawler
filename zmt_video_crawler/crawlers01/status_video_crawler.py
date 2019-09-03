# 接口http://www.statusvideos2019.com/?json=get_posts&exclude=content,categories,tags,comments,custom_fields&page=6&count=5

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
    videos = metadata.get('posts')
    for video in videos:
        video_info = {
            'video_url': video.get('attachments')[0].get('url'),
            'title': '#status #videos ' + video.get('title')
        }
        video_infos.append(video_info)
    return video_infos


def download_video(video_info):
    video_path = '/Users/xuan.zhang/Documents/videos/status_video/%s.mp4' % video_info.get('title')
    bfu = MyBloomUtil('status_video')
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
        url = 'http://www.statusvideos2019.com/?json=get_posts&exclude=content,categories,tags,comments,custom_fields&page=%d&count=5' % i
        print('start to parse [%s]' % url)
        video_infos = get_video_infos(url)
        for video_info in video_infos:
            download_video(video_info)


if __name__ == '__main__':
    crawl()
