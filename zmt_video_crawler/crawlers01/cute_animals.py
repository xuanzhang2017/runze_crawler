# coding=utf8

# https://www.reddit.com/r/aww/hot.json?after=t3_c3axd6

import requests
import json
from utils.user_agents import headers

start_url = 'https://www.reddit.com/r/aww/hot.json?after=t3_c3axd6'


def get_metadata(url):
    cookies = 'loid=00000000003zl7iqee.2.1561186945715.Z0FBQUFBQmREZEtCRHdsYmlLSWgxVTdTY1ZRUmJ5Ymx0U1MzT1NLWnhBbG92c2JLRWI4UW1ZakpkNThyQUVnSWkxUDVwcDVlSU1mOWdVbC1MNWw0QUwwWjVPZGUyTnhUbGFfT01lZWgxdGs0M1ptdUY0TzlmSGdMZXhnRzd5bW1GU0JtLTM0SlR1cG0; edgebucket=UNrzqu52CeECzdc69k; session_tracker=uVFP9JohgmkWxuqgHz.0.1561189198373.Z0FBQUFBQmREZHRPa245N3FIcHRYZEJLVXdVeGZBVmYwejlMQ3VmY1V0QWxxZkdjbUcyZVJUNDBTTzF5bS1MVWFUVjVfRjRCbTJoYmRqRUNabW9fbU1lcXFKaWw2OU1sTDNDMTFKRTdrYkp6QXhndFQ5T3RBc2dzaHVRSFR6XzQ3NXNlLWthRGFOR3c'
    # headers['cookie'] = cookies
    resp = requests.get(url, headers=headers)
    return json.loads(resp.text)


def parse_metadata(metadata):
    video_info_list = []
    video_datas = metadata.get('data').get('children')
    after = metadata.get('after', '')
    if after:
        next_url = 'https://www.reddit.com/r/aww/hot.json?after=%s' % after
    else:
        next_url = None

    for video_data in video_datas:
        video_info = {
            'video_url': video_data.get('data', {}).get('secure_media', {}).get('reddit_video', '').get('fallback_url',
                                                                                                        ''),
            'video_title': video_data.get('title', '')
        }
        video_info_list.append(video_info)
    return video_info_list, next_url


def download_video(video_info):
    print('video_info = %s' % json.dumps(video_info))


def crawl(url):
    metadata = get_metadata(url)
    video_info_list, next_url = parse_metadata(metadata)
    for video_info in video_info_list:
        download_video(video_info)
    if next_url:
        crawl(next_url)


def main():
    crawl(start_url)


if __name__ == '__main__':
    # main()
    print(get_metadata(start_url))
