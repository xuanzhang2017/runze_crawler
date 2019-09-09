from utils.bloom_util import MyBloomUtil
import os

mbf = MyBloomUtil('bilibili')
for i in range(1,70):
    link = 'https://www.bilibili.com/video/av35463978/?p=%s' % i
    print(link)

    is_exist = mbf.is_exists(link)
    if not is_exist:
        # you_get_cmd = 'you-get %s -o /Users/xuanzhang/wengao/videos/tencent/01' % detail_url
        you_get_cmd = 'you-get %s -o ../videos/bilibili' % link
        print(you_get_cmd)
        os.system(you_get_cmd)
        mbf.add_in_bf(link)