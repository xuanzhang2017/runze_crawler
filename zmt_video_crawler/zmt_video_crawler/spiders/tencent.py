# -*- coding: utf-8 -*-
import scrapy
import os
from zmt_video_crawler.items import ZmtVideoCrawlerItem
from utils.bloom_util import MyBloomUtil


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['qq.com']
    start_urls = [
        ######## 国际新闻
        # 燃新闻
        # 'https://v.qq.com/vplus/b7804c699e970d4567d5bd9617482a49#uin=b7804c699e970d4567d5bd9617482a49?page=video',
        # 'https://v.qq.com/vplus/7bd332aeddfaa689bafef9e42a504593#uin=7bd332aeddfaa689bafef9e42a504593?page=video',
        # 'https://v.qq.com/vplus/8fba149e0af4019e3d9d36e561cdbe5c#uin=8fba149e0af4019e3d9d36e561cdbe5c?page=video',
        # 'https://v.qq.com/vplus/90b9efe8fe80aa1e6f356522325b0902#uin=90b9efe8fe80aa1e6f356522325b0902?page=video',
        # 'https://v.qq.com/vplus/3b3f74ac90c97d436790f8db904e73a1#uin=3b3f74ac90c97d436790f8db904e73a1?page=video',
        # 'https://v.qq.com/vplus/392b4bf379df35ac1f15c9a406347560#uin=392b4bf379df35ac1f15c9a406347560?page=video',
        # 'https://v.qq.com/vplus/5ba4bd48d599ccfc7d8c1a9c4a92e49d#uin=5ba4bd48d599ccfc7d8c1a9c4a92e49d?page=video',
        # 'https://v.qq.com/vplus/e23a3fc044e64378b188a15948ea99e1#uin=e23a3fc044e64378b188a15948ea99e1?page=video',
        # 中宏网新闻
        # 'https://v.qq.com/vplus/431cd173e260b928a7f358a3c1cdb434#uin=431cd173e260b928a7f358a3c1cdb434',
        # 'https://v.qq.com/vplus/99e1f7f0bcf809a40905ea2aaa949e12#uin=99e1f7f0bcf809a40905ea2aaa949e12?page=video',
        # 'https://v.qq.com/vplus/b7cb0785b9776c80d96face787e921b3#uin=b7cb0785b9776c80d96face787e921b3?page=video',
        # 'https://v.qq.com/vplus/ec886881a40c7f510f8cf579b9d6066f#uin=ec886881a40c7f510f8cf579b9d6066f?page=video',

        'https://v.qq.com/vplus/0858c04ba0c6616f9d05fe0ddce931ef#uin=0858c04ba0c6616f9d05fe0ddce931ef?page=video',
        'https://v.qq.com/vplus/38cfec596ea37ff7ced49e3d6d74a98f#uin=38cfec596ea37ff7ced49e3d6d74a98f?page=video',

        ###### 科技
        #科技杂谈家
        # 'https://v.qq.com/vplus/8b33fa3f95fe49217afa2888d66bd01c#uin=8b33fa3f95fe49217afa2888d66bd01c?page=video',
        # 'https://v.qq.com/vplus/69c6a8582bede0357afa2888d66bd01c#uin=69c6a8582bede0357afa2888d66bd01c?page=video',
        #鲁大师官方
        # 'https://v.qq.com/vplus/024fd313917ced20374b388a03b2358f#uin=024fd313917ced20374b388a03b2358f?page=video',

        #####电影
        # 'https://v.qq.com/vplus/35d92cd65c46b581a0b6c87bb849e22c#uin=35d92cd65c46b581a0b6c87bb849e22c?page=video',

        # 体育
        # 'https://v.qq.com/vplus/204302bc80b27194d96face787e921b3#uin=204302bc80b27194d96face787e921b3?page=video',

        ####美食做法，吃播
        # 版权主张比较多
        # 'https://v.qq.com/vplus/e9b0660f06a4eece374b388a03b2358f#uin=e9b0660f06a4eece374b388a03b2358f?page=video',
        # 'https://v.qq.com/vplus/77a68d128fdc679ea25e9827b38c171e#uin=77a68d128fdc679ea25e9827b38c171e?page=video',

        #####有氧运动，减肥，健康
        # 'https://v.qq.com/vplus/94adaad2c2f6d1a0b1f4158faf187d3f#uin=94adaad2c2f6d1a0b1f4158faf187d3f?page=video',

        ######影视
        # 'https://v.qq.com/vplus/25850010d1306d0d7ca329be3aecc704#uin=25850010d1306d0d7ca329be3aecc704?page=video',
        # 'https://v.qq.com/vplus/311b5a4f9f924136f9a10ae0a7d3f9b1#uin=311b5a4f9f924136f9a10ae0a7d3f9b1?page=video',
        # 'https://v.qq.com/vplus/3bc2c272c99c88debafef9e42a504593#uin=3bc2c272c99c88debafef9e42a504593?page=video',
        # 'https://v.qq.com/vplus/8465eff38e40dfaba01b0ec44fc77ae4#uin=8465eff38e40dfaba01b0ec44fc77ae4?page=video',

        ######搞笑
        # 'http://v.qq.com/vplus/3f836cea1aa502a4bac790ee1028a77e?page=video',

        #####娱乐
        'https://v.qq.com/vplus/4bb16a9899bea450ee34a4e73a803f62#uin=4bb16a9899bea450ee34a4e73a803f62?page=video',
        'https://v.qq.com/vplus/05556727b25584586f356522325b0902#uin=05556727b25584586f356522325b0902?page=video',
        'https://v.qq.com/vplus/141f5e664b343f9567d5bd9617482a49#uin=141f5e664b343f9567d5bd9617482a49?page=video',
        'https://v.qq.com/vplus/8aa7832813445ba3083dce956f48556c#uin=8aa7832813445ba3083dce956f48556c?page=video',
        'https://v.qq.com/vplus/0c866f036c7dcc6b478b8fdb08d871fa#uin=0c866f036c7dcc6b478b8fdb08d871fa?page=video',
        'https://v.qq.com/vplus/0943cdbde9e89c16e59d64df08a6d68f#uin=0943cdbde9e89c16e59d64df08a6d68f?page=video',
        'https://v.qq.com/vplus/9b18d7d518431ae8f893016a79843b0d#uin=9b18d7d518431ae8f893016a79843b0d?page=video',
        'https://v.qq.com/vplus/97e5558e80a0d58bdef1e7c7ee68744c#uin=97e5558e80a0d58bdef1e7c7ee68744c?page=video',
        'https://v.qq.com/vplus/ee8581446297af1d85fc9e995a19b595#uin=ee8581446297af1d85fc9e995a19b595?page=video',
        'https://v.qq.com/vplus/d5122d5360271d7373641ebb97994585#uin=d5122d5360271d7373641ebb97994585?page=video',

        # 其他
        'https://v.qq.com/vplus/a74b9725b739299fd6e00555d6a4fbaa#uin=a74b9725b739299fd6e00555d6a4fbaa?page=video',
    ]

    def start_requests(self):
        with open('./video_src_list/xianfeng_shortvideos.csv', 'r') as f:
            lines = f.readlines()
            for link in lines:
                yield scrapy.Request(link, callback=self.parse)

    def parse(self, response):
        detail_urls = [response.urljoin(url) for url in response.xpath(
            "//div[@id='_videolist_latest']/div[@class='list_item ']/a/@href | //div[@class='mod_feed_item']/div/a/@href").extract()]
        mbf = MyBloomUtil(self.name)

        for detail_url in detail_urls:
            print('detail_url = %s' % detail_url)
            is_exist = mbf.is_exists(detail_url)
            if not is_exist:
                # you_get_cmd = 'you-get %s -o /Users/xuanzhang/wengao/videos/tencent/01' % detail_url
                you_get_cmd = 'you-get %s -o ./videos/tencent' % detail_url
                print(you_get_cmd)
                os.system(you_get_cmd)
                mbf.add_in_bf(detail_url)
            # item = ZmtVideoCrawlerItem()
            # item['detail_url'] = detail_url
            # yield item
