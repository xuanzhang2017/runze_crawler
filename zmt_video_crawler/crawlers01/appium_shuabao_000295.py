# coding=utf8

# 参考：https://github.com/Python3WebSpider/Moments/blob/master/moments.py
# zenjoy-000354

import sys
import traceback

sys.path.append('../')
sys.path.append('../tiktok')
sys.path.append('../utils')
import random
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from crawlers01.tiktok_config import *


class Tiktok():
    # lang_to_crawl需要抓取的语言
    def __init__(self):
        """
        初始化
        """
        # 驱动配置
        # fortunaltezh
        # devicename-dev: treltektt
        # devicename-online: ja3g
        # le_turbo 乐视
        # udid-online 4d0061fe4874a0eb
        # udid-dev 4100a5dbf2e6b191
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': 'ja3g',
            'appPackage': 'com.jm.video',
            'appActivity': '.ui.main.MainActivity',
            'udid': '4d0061fe4874a0eb',
            "noReset": "true",
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        # self.wait = WebDriverWait(self.driver, TIMEOUT)

    def enter(self):
        print('Entered the app.')
        sleep(random.randint(18, 22))
        # TouchAction(self.driver).press(x=372, y=902).move_to(x=372, y=596).release().perform()
        print('entered.')

    def move(self):
        # while True:
        print('start to move...')
        # sleep(3)
        for i in range(SCROLL_TIMES):
            # print('move for the [%d] time.' % i)
            try:
                print('Swipe for the %d time.' % i)
                TouchAction(self.driver).press(x=538, y=1552).move_to(x=499, y=414).release().perform()
                sleep(random.randint(18, 23))
                # sleep(35)
                # # 点击一下
                # TouchAction(self.driver).tap(x=707, y=898).perform()
                # sleep(0.5)
                # TouchAction(self.driver).tap(x=707, y=898).perform()
                # sleep(random.randint(1, 5))
            except Exception as e:
                traceback.print_exc()
                break

    def close(self):
        self.driver.close_app()
        print('closed')

    def main(self):
        # 进入app
        self.enter()
        # 滑动
        self.move()
        # 关闭app
        self.close()


def main():
    while True:
        try:
            tiktok_slider = Tiktok()
            tiktok_slider.main()
        except:
            traceback.print_stack()
            continue


if __name__ == '__main__':
    main()
