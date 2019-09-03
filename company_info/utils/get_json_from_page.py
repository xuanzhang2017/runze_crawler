# coding=utf8
import sys
sys.path.append('../')
sys.path.append('../utils')
import requests
import json
from utils.proxy_util import get_proxies
from utils import user_agents


def get_json(url, headers):
    proxies = get_proxies(url)
    try:
        ret = requests.get(url, headers=headers, proxies=proxies)
        ret_json = json.loads(ret.text)
        return ret_json
    except:
        return None


def get_json_by_retry(url, headers=None):
    if not headers:
        headers = user_agents.headers
    return get_json(url, headers) \
           or get_json(url, headers) \
           or get_json(url, headers) \
           or get_json(url, headers) \
           or get_json(url, headers)


if __name__ == '__main__':
    url = 'https://api.giphy.com/v1/gifs/search?api_key=3eFQvabDx69SMoOemSPiYfh9FY0nzO9x&q=' + 'song' + '&offset=0&limit=100'
    ret = get_json_by_retry(url)
    print(ret)
