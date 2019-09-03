# coding=utf8
import os
import sys

sys.path.append('../')
sys.path.append('../vid_status')
# 平台
PLATFORM = 'Android'

# 设备名称 通过 adb devices -l 获取
DEVICE_NAME = 'MI_NOTE_Pro'

# APP路径
APP = os.path.abspath('.') + '/weixin.apk'

# APP包名
APP_PACKAGE = 'com.tencent.mm'

# 入口类名
APP_ACTIVITY = '.ui.LauncherUI'

# Appium地址
DRIVER_SERVER = 'http://localhost:4723/wd/hub'
# 等待元素加载时间
TIMEOUT = 300

# 微信手机号密码
USERNAME = ''
PASSWORD = ''

# 滑动点
FLICK_START_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700

# # MongoDB配置
# MONGO_URL = 'localhost'
# MONGO_DB = 'moments'
# MONGO_COLLECTION = 'moments'

# 滑动间隔
SCROLL_SLEEP_TIME = 2
SCROLL_TIMES = 300

log_dir = './log'
record_dir = './record'
data_dir = './data'
bucket_name = 'mx-you-crawler'
is_online = False
if not is_online:
    queue_name = 'app_crawler_tiktok_dev'
else:
    queue_name = 'app_crawler_tiktok_prod'


class TiktokInstruction(object):

    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    DIGG = 'digg'
