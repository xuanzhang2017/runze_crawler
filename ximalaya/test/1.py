# coding=utf

import requests

url01 = 'http://audio.xmcdn.com/group48/M06/BA/AE/wKgKlVtK7d6BMqTmAJMERCIMA7E294.m4a'
ret = requests.get(url01)
with open('001.m4a', 'wb') as f:
    f.write(ret.content)

