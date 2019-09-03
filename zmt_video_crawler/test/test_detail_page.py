# coding=utf8

import requests

url = 'https://www.zimeika.com/video/detail/haokan.html?id=1223952'
for i in range(100):
    ret = requests.get(url)
    print(ret.text)
    print('-------------%d-------------' % i)