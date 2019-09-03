# coding=utf8
import sys

sys.path.append('../')
sys.path.append('../utils')
import os
from pybloom_live import BloomFilter


class MyBloomUtil:
    def __init__(self, bloom_name):
        bloom_dir = './bf'
        if not os.path.exists(bloom_dir):
            os.makedirs(bloom_dir)
        self.bloom_path = '%s/%s.blm' % (bloom_dir, bloom_name)
        is_exist = os.path.exists(self.bloom_path)
        if is_exist:
            self.bf = BloomFilter.fromfile(open(self.bloom_path, 'rb'))
        else:
            self.bf = BloomFilter(20000, 0.001)

    def process_item(self, item):
        if item in self.bf:
            # logger.info('[%s] is already in bloom.' % item)
            return None
        else:
            print('add one')
            self.bf.add(item)
            self.bf.tofile(open(self.bloom_path, 'wb'))
            return item
