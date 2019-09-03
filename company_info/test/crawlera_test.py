# coding=utf8

import requests
import random
import json
from dianping.settings import USER_AGENTS

proxy = "paygo.crawlera.com:8010"
proxy_auth = ""

proxies = {
    "http": "http://{0}@{1}/".format(proxy_auth, proxy)
}


def get_headers():
    ua = random.choice(USER_AGENTS)
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': '',
        'Host': 'www.dianping.com',
        'Referer': 'http://www.dianping.com/beijing/ch10/g110',
        "User-Agent": ua
    }
    return headers


cookie_str = '_lxsdk_cuid=16497548b2ec8-0f2d8f3ffa117-4a5369-13c680-16497548b2ec8; _lxsdk=16497548b2ec8-0f2d8f3ffa117-4a5369-13c680-16497548b2ec8; _hc.v=1c9700ba-388a-ed72-d293-145e57e71287.1531547258; s_ViewType=10; __mta=244168250.1531547299659.1531547480000.1532850488124.3; aburl=1; cityid=2; default_ab=shop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A1; switchcityflashtoast=1; m_flash2=1; cy=2; cye=beijing; _lxsdk_s=1681c1ee086-fc-c80-929%7C%7C2'


def get_cookie(cookie_str):
    cookies = {}
    cookie_list = cookie_str.split(';')
    for coo in cookie_list:
        key = coo.split('=')[0].strip()
        value = coo.split('=')[1].strip()
        cookies[key] = value
    print('cookies = %s' % json.dumps(cookies))
    return cookies


cookies = {
    "_lxsdk_cuid": "16497548b2ec8-0f2d8f3ffa117-4a5369-13c680-16497548b2ec8",
    "_lxsdk": "16497548b2ec8-0f2d8f3ffa117-4a5369-13c680-16497548b2ec8",
    "_hc.v": "1c9700ba-388a-ed72-d293-145e57e71287.1531547258",
    "s_ViewType": 10,
    "__mta": "244168250.1531547299659.1531547480000.1532850488124.3",
    "aburl": 1,
    "cityid": 2,
    "default_ab": "shop:A:1|index:A:1|shopList:A:1",
    "switchcityflashtoast": 1,
    "m_flash2": 1,
    "cy": 2,
    "cye": "beijing",
    "_lxsdk_s": "1681d4ebace-1a4-b25-478||15"
}

for i in range(50):
    # url01 = 'http://www.dianping.com/shop/69089926'
    url02 = 'http://www.dianping.com/shop/18585748'
    # ret = requests.get(url01, headers=get_headers(), proxies=proxies, cookies=get_cookie(cookie_str))
    # ret = requests.get(url01, headers=get_headers(), proxies=proxies)
    ret = requests.get(url02, headers=get_headers())
    print(ret.status_code)
    print(ret.text)
