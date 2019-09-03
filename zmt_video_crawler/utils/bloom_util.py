# coding=utf8
import sys

sys.path.append('../')
sys.path.append('../maimai')
sys.path.append('../utils')
import os
from pybloom_live import BloomFilter
from utils.log_util import logger


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

    def is_exists(self, item):
        return item in self.bf

    def add_in_bf(self, item):
        print('add %s' % item)
        self.bf.add(item)
        self.bf.tofile(open(self.bloom_path, 'wb'))

    def process_item(self, item):
        if item in self.bf:
            logger.info('[%s] is already in bloom.' % item)
            return None
        else:
            logger.info('add [%s]' % item)
            self.bf.add(item)
            self.bf.tofile(open(self.bloom_path, 'wb'))
            return item
