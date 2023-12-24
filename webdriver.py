# -*- coding: utf-8 -*-
# @Time    : 2022/10/20 2:55 PM
# @Author  : XuLei
# @FileName: webdriver.py
# @Software: PyCharm
import os
import subprocess
from Common.log import logger


udid=subprocess.Popen('idevice_id -l | head -n1',shell=True,stdout=subprocess.PIPE)

udid=udid.stdout.read()
udid=udid.decode('utf-8')
udid=udid.replace('\n', '')
udid=udid.replace('\r', '')
if udid !='':
    os.system(f'xcodebuild -project /Users/meross/Downloads/WebDriverAgent-4.10.2/WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id={udid}" USE_PORT=8100 test')
else:
    logger.error('未找到待测试的iphone手机,请检查')