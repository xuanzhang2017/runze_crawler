# coding=utf8
import sys
sys.path.append('../')
sys.path.append('../utils')
import requests
import json
from utils import user_agents


def get_json(url, headers):
    try:
        ret = requests.get(url, headers=headers)
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
    pass
