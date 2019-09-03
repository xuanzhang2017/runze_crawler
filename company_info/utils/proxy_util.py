# coding=utf8

import requests
import random


def get_proxy_daxiang(protocol):
    # 从大象代理获取IP 得到IP形如185.15.0.187:43693
    s = requests.session()
    s.keep_alive = False
    if protocol == 'http':
        proxies = s.get('http://vip33.daxiangdaili.com/ip/?tid=559985817064399&num=5').text
    elif protocol == 'https':
        proxies = s.get(
            'http://vip33.daxiangdaili.com/ip/?tid=559985817064399&num=5&protocol=https').text
    # proxies = s.get('http://vip33.daxiangdaili.com/ip/?tid=559985817064399&num=8&foreign=only&filter=on').text
    proxy = random.choice(proxies.split('\r\n'))
    # proxy = s.get('http://vip22.daxiangdaili.com/ip/?tid=559985817064399&num=1&foreign=only').text
    return proxy


def get_proxy(protocol):
    # time.sleep(1.1)
    proxy = get_proxy_daxiang(protocol)
    if not proxy:
        # time.sleep(2)
        proxy = get_proxy_daxiang(protocol)
    if not proxy:
        # time.sleep(2)
        proxy = get_proxy_daxiang(protocol)
    if not proxy:
        # time.sleep(2)
        proxy = get_proxy_daxiang(protocol)
    if not proxy:
        # time.sleep(2)
        proxy = get_proxy_daxiang(protocol)
    if not proxy:
        # time.sleep(2)
        proxy = get_proxy_daxiang(protocol)
    return proxy


# 根据src_url是否以https开头来决定获取什么样的代理
def get_proxies(src_url):
    protocol = 'http'
    if src_url.startswith('https'):
        protocol = 'https'
    proxy = get_proxy(protocol)
    # logger.debug('The proxy is %s' % proxy)
    # print('The proxy is %s' % proxy)
    if not proxy.strip():
        # logger.debug('download %s/%s failed by requests, the proxy is empty.')
        return False

    proxies = {
        'http': 'http://%s' % proxy,
        'https': 'https://%s' % proxy
    }
    return proxies


if __name__ == '__main__':
    proxy = get_proxy('http')
    print(proxy)
