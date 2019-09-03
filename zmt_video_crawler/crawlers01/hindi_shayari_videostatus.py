# coding=utf8
# app_url:

import requests
import json

with open('hindi_shayari_videostatus.json', 'r') as f:
    content = f.read()
    metadata = json.loads(content)
    print(metadata)
    records = metadata.get('Record')
    for record in records:
        video_title = '30 seconds hindi whatsapp video status ' + record.get('videoname')
        video_url = record.get('videourl')
        video_path = '/Users/xuan.zhang/Documents/videos/hindi_shayari/%s.mp4' % video_title
        print('video_path = %s' % video_path)
        resp = requests.get(video_url)
        with open(video_path, 'wb') as f:
            f.write(resp.content)
