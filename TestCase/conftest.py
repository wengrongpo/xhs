import os
import random
import string
import threading
import time
import allure
import pytest

import Common.set
from Common.log import logger
from appium import webdriver

from Common.mqtt_check import app_check
from Common.set import Set
import warnings
from Common.data_deal import DataDeal
import base64
from Common.Tools import Tools
from appium.options.android import UiAutomator2Options

DataDeal.setting()
DataDeal.get_email()


@pytest.fixture(scope="function", autouse=True)
def start():
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        driver = webdriver.Remote('http://localhost:4723/wd/hub', Set.desired_caps)
    logger.info(f"测试机配置：{Set.desired_caps}")
    Tools.thread_start(Tools().assert_rule)
    setting(driver)
    yield
    time.sleep(10)
    end_deal(driver)
    driver.quit()


def record(driver):
    """保存用例执行录像"""
    if Set.record == "1":
        video = driver.stop_recording_screen()
        video_data = base64.b64decode(video)
        ran = ''.join(random.sample(string.ascii_letters + string.digits, 9))
        mp4 = f'./TestReport/videos/{ran}.mp4'
        file = open(mp4, 'wb')
        file.write(video_data)
        file.close()
        logger.info(f'当前用例录像地址：{mp4}')


def setting(driver):
    logger.info(f"已连接{Set.client}手机开始测试,隐式等待{Set.wait_time}秒")
    if Set.debug == '1':
        logger.info("打开调试模式")
    elif Set.debug == '0':
        driver.close_app()
        driver.launch_app()
        logger.info("关闭调试模式")
    else:
        logger.warning("debug 模式异常")
    setattr(Set, "driver", driver)
    if Set.record == "1":
        logger.info("打开录像功能")
        driver.start_recording_screen()
    else:
        logger.info('已关闭录像功能')
    driver.implicitly_wait(Set.wait_time)


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    import ctypes
    tid = ctypes.c_long(tid)
    import inspect
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def end_deal(driver):
    setattr(Set, 'check_result', True)
    if Set.time_diff is not None:
        time.sleep(Set.time_diff)
    record(driver)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    import time
    """统计次数结果"""
    case_dict = {"case_pass": len(terminalreporter.stats.get('passed', [])),
                 "case_fail": len(terminalreporter.stats.get('failed', [])),
                 "case_error": len(terminalreporter.stats.get('error', [])),
                 "case_skip": len(terminalreporter.stats.get('skipped', [])),
                 "case_xfail": len(terminalreporter.stats.get('xfailed', [])),
                 "case_xpass": len(terminalreporter.stats.get('xpassed', [])),
                 "case_rerun": len(terminalreporter.stats.get('rerun', [])),
                 "case_time": round(time.time() - terminalreporter._sessionstarttime, 2),
                 'case_start_time': Tools.date_time(terminalreporter._sessionstarttime),
                 'case_end_time': Tools.date_time(time.time())}
    from Common.msg import push_test_report
    if Set.report_switch == 1 or Set.report_switch == '1':
        push_test_report(case_dict)
