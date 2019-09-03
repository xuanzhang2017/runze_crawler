# coding=utf8

# 下载一个up主上传的所有视频
import requests
import json
import os

channel_id = '386753444'
get_videoids_url = 'https://space.bilibili.com/ajax/member/getSubmitVideos?mid=%s&pagesize=30&tid=0&page=1&keyword' \
                   '=&order=pubdate' % channel_id

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0',
}
ret = requests.get(get_videoids_url, headers=headers)
print(ret.text)
ret_json = json.loads(ret.text)
video_infos = ret_json.get('data').get('vlist')
for info in video_infos:
    vid = info.get('aid')
    print('vid = %s' % vid)
    detail_url = 'https://www.bilibili.com/video/av' + str(vid)
    cmd = 'source activate py3;you-get %s -o /Users/xuan.zhang/Documents/python_project_3/runze_crawler/bilibili_crawler/videos/' % detail_url
    print(cmd)
    try:
        os.system(cmd)
    except:
        os.system(cmd)