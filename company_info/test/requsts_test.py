# coding=utf8

import sys
import json

sys.path.append('../')
sys.path.append('../utils')
import time
import requests
import random
from utils.user_agents import USER_AGENTS
from lxml import etree
from utils import proxy_util


# def get_proxies():
#     proxy = "paygo.crawlera.com:8010"
#     proxy_auth = ""
#
#     proxies = {
#         "http": "http://{0}@{1}/".format(proxy_auth, proxy)
#     }
#     return proxies


def get_headers():
    ua = random.choice(USER_AGENTS)
    headers = {
        # 'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        # 'Cache-Control': 'max-age=0',
        # 'Connection': 'keep-alive',
        # # 'Cookie': '',
        # 'Host': 'www.dianping.com',
        # 'Referer': 'http://www.dianping.com/beijing/ch10/g110',
        "User-Agent": ua
    }
    return headers


urls = ['http://www.dianping.com/beijing/ch10/g110p%d' % i for i in range(1, 51)]

cookie_str = ''


def get_cookie(cookie_str):
    cookies = {}
    cookie_list = cookie_str.split(';')
    for coo in cookie_list:
        key = coo.split('=')[0]
        value = coo.split('=')[1]
        cookies[key] = value
    return cookies


def get_etree_html(src_url, key):
    # proxies = get_proxies()
    proxies = proxy_util.get_proxies(src_url)
    print(proxies)
    headers = get_headers()
    # cookies = get_cookie(cookie_str)
    # r = requests.get(src_url, proxies=proxies, headers=headers, cookies=cookies)
    try:
        r = requests.get(src_url, proxies=proxies, headers=headers, timeout=5)
    except Exception as e:
        print(e)
        return None
    # r = requests.get(src_url, headers=headers, cookies=cookies)
    # print(r.url)
    ret_txt = r.text
    print('ret_txt = %s' % ret_txt)
    print('len(ret_txt) = %d' % len(ret_txt))
    if len(ret_txt) < 3500:
        return None
    html = etree.HTML(ret_txt.encode("utf-8", 'ignore'))
    return html


def get_etree_by_retry(src_url, key):
    etree_html = get_etree_html(src_url, key)
    for i in range(20):
        if etree_html is None:
            etree_html = get_etree_html(src_url, key)

    return etree_html


def get_json(src_url):
    # proxies = get_proxies()
    proxies = proxy_util.get_proxies(src_url)
    headers = get_headers()
    # cookies = get_cookie(cookie_str)
    # r = requests.get(src_url, proxies=proxies, headers=headers, cookies=cookies)
    try:
        r = requests.get(src_url, proxies=proxies, headers=headers)
    except Exception as e:
        return None
    # r = requests.get(src_url, headers=headers)
    # r = requests.get(src_url, headers=headers, cookies=cookies)
    # print(r.url)
    ret_txt = r.text
    return json.loads(ret_txt)


def get_json_by_retry(src_url):
    json_ret = get_json(src_url)
    for i in range(10):
        if json_ret is None:
            json_ret = get_json(src_url)
    return json_ret


def parse(list_url, key):
    try:
        html = get_etree_by_retry(src_url=list_url, key=key)
    except:
        return None
    if html is None:
        return None
    first_company_url = html.xpath("//section[@id='searchlist']/table/tbody/tr/td[2]/a/@href")[0]
    print(first_company_url)
    first_company_num = first_company_url.split('_')[1].split('.')[0]
    first_company_phone_json_url = 'https://www.qichacha.com/tax_view?keyno=%s&ajaxflag=1' % first_company_num
    print('first_company_phone_json_url = %s' % first_company_phone_json_url)
    parse_detail_page(first_company_phone_json_url)
    # for i in range(500):
    #     url01 = 'https://www.qichacha.com/firm_cd1bc1e241c81094c2d4f87718cfe7c1.html'
    #     url02 = 'https://www.qichacha.com/tax_view?keyno=cd1bc1e241c81094c2d4f87718cfe7c1&ajaxflag=1'
    #     try:
    #         print('crawl for the [%d] time.' % i)
    #         parse_detail_page(url02, {})
    #     except:
    #         print('failed for the [%d] time.' % i)
    #         continue


def parse_detail_page(detail_link):
    json_info = get_json_by_retry(src_url=detail_link)
    # phone_num = html.xpath("//div[@id='fapiaoQrcode']/div/p[4]/span/text()")

    # metadata['shop_name_in_detail_page'] = phone_num
    # print(json.dumps(metadata))
    print(json_info)


def main():
    start = int(time.time())
    key = '航天恒星科技有限公司'
    list_url = 'https://www.qichacha.com/search?key=' + key
    parse(list_url, key)
    end = int(time.time())
    duration = end - start
    print('duration = %d' % duration)


if __name__ == '__main__':
    main()
