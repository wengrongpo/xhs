import logging
import time
from selenium.webdriver.common.by import By
from Common.log import logger
from appium.webdriver.common.appiumby import AppiumBy
import allure
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
import string
from selenium.webdriver.support.wait import WebDriverWait
from Common.Tools import Tools
from Common.set import Set
from retrying import retry


def retry_if_result_false(result):
    return result is False


class Page:
    def __init__(self):
        self.driver = Set.driver

    @retry(stop_max_attempt_number=3, wait_fixed=6, retry_on_result=retry_if_result_false)
    def find_element(self, ele_origin: str, timeout=5, model='found', sleep_time=0):
        #开始时间
        time_start = time.time()
        time.sleep(sleep_time)
        n = 0
        #处理原始数据，分为ele[0]定位方法和ele[1]表达式
        ele = Page.ele_deal(ele_origin)
        #替换表达式中含包名的部分
        ele_selector = self.re_app(ele[1])
        try:
            #检查当前页面是否有该元素，否则抛出异常进入except分支
            WebDriverWait(self.driver, timeout).until(lambda x: self.get_elem(ele[0], ele_selector))
            logger.debug(f"开始定位 {ele_selector} 元素,使用{ele[0]}方法")
            elem = self.get_elem(ele[0], ele_selector)
            while elem:
                if elem.is_displayed():
                    time_diff = time.time() - time_start
                    time_diff = round(time_diff, 2)
                    logger.debug(f'成功定位元素{ele_selector},耗时{time_diff}s')
                    return elem
                else:
                    if model not in ['find', 'assert']:
                        if self.pop_up_window():
                            self.find_element(ele_origin)
                        logger.warning(f"{ele_selector} 元素可能不展示")
                        return elem
                    else:
                        return None
        except BaseException as e:
            """普通寻找元素，和一直寻找元素"""
            logger.debug(f'寻找元素{ele_origin}可能发生异常')
            if model == "found":
                if self.pop_up_window() is True:
                    return self.find_element(ele_origin)
                elif self.slip_find(ele_origin) is True:
                    return self.find_element(ele_origin)
                else:
                    Tools.step_log(fr'未找到元素{ele_selector},使用{ele[0]}方法')
                    if Set.debug=='1':
                        Tools.step_log(self.get_page_source(),shot='')
                    return False
            elif model == 'assert':
                Tools.step_log(f"{timeout}s内判断元素: {ele_selector} 不存在",shot='')
            elif model == "find":
                logger.info(f"{ele_selector}元素持续寻找中")
            else:
                logger.error(f'error:{e}')

    def get_elem(self, by, value):
        if by == "by.id":
            elem = self.driver.find_element(By.ID, value)
        elif by == "by.class_name":
            elem = self.driver.find_element(By.CLASS_NAME, value)
        elif by == "by.classes_name":
            elem = self.driver.find_elements(By.CLASS_NAME, value)    
        elif by == "by.tag":
            elem = self.driver.find_element(By.TAG_NAME, value)
        elif by == "by.link_text":
            elem = self.driver.find_element(By.LINK_TEXT, value)
        elif by == "by.partial_link_text":
            elem = self.driver.find_element(By.PARTIAL_LINK_TEXT, value)
        elif by == "by.xpath":
            elem = self.driver.find_element(By.XPATH, value)
        elif by == "by.css":
            elem = self.driver.find_element(By.CSS_SELECTOR, value)
        elif by == "by.ios_uiautomation":
            elem = self.driver.find_element(AppiumBy.IOS_UIAUTOMATION, value)
        elif by == "by.ios_predicate":
            elem = self.driver.find_element(AppiumBy.IOS_PREDICATE, value)

        elif by == "by.ios_class_chain":
            elem = self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value)

        elif by == "by.android_uiautomator":
            elem = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value)

        elif by == "by.android_viewtag":
            elem = self.driver.find_element(AppiumBy.ANDROID_VIEWTAG, value)

        elif by == "by.android_data_matcher":
            elem = self.driver.find_element(AppiumBy.ANDROID_DATA_MATCHER, value)

        elif by == "by.accessibility_id":
            elem = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value)
        elif by == "by.android_view_matcher":
            elem = self.driver.find_element(AppiumBy.ANDROID_VIEW_MATCHER, value)
        elif by == "by.windows_uiautomation":
            elem = self.driver.find_element(AppiumBy.WINDOWS_UI_AUTOMATION, value)
        elif by == "by.image":
            elem = self.driver.find_element(AppiumBy.IMAGE, value)

        elif by == "by.custom":
            elem = self.driver.find_element(AppiumBy.CUSTOM, value)
        else:
            elem = ""
            logger.error(f"by方法不能识别,传值是{by}，系统识别是by.id格式，均小写")
        return elem

    @staticmethod
    def ele_deal(ele: str):
        ele = ele.split("|")
        return ele

    def launch_app(self):
        logger.debug("开始启动app")
        self.driver.launch_app()

    def close_app(self):
        logger.debug("开始关闭app")
        self.driver.close_app()

    def reset(self):
        logger.debug("开始重启app")
        self.driver.reset()

    def assert_ele(self, ele_origin, ps, timeout=10):
        ele = Page.ele_deal(ele_origin)
        ele_selector = self.re_app(ele[1])
        try:
            WebDriverWait(self.driver, timeout).until(lambda x: self.get_elem(ele[0], ele_selector))
            self.get_elem(ele[0], ele[1])
            Tools.step_log(f"✅校验：{ps}正确",'info', shot='1')
            result = True
        except BaseException as e:
            pop = self.pop_up_window()
            if pop is True:
                return self.assert_ele(ele_origin, ps)
            else:
                if Set.debug =='1':
                    logger.error(self.get_page_source())
                Tools.step_log(fr'❎{ps}校验失败，元素{ele_selector}不存在')
                if Set.debug == '1':
                    Tools.step_log(self.get_page_source(), shot='')
                    Tools.step_log(e,shot='')
                result = False
        assert result
        return result

    def back(self):
        self.driver.back()

    def start_record(self):
        self.driver.start_recording_screen()

    def stop_record(self):
        self.driver.stop_recording_screen()

    def shot(self):
        try:
            ran = ''.join(random.sample(string.ascii_letters + string.digits, 20))
            path = f"./Log/shot/{ran}.png"
            self.driver.get_screenshot_as_file(path)
            return path
        except Exception as e:
            logger.error(e)

    def slip(self, model):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        if model == "down":
            actions.w3c_actions.pointer_action.move_to_location(0.5 * width, 0.75 * height)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(0.5 * width, 0.25 * height)
        elif model == "slow_down":
            actions.w3c_actions.pointer_action.move_to_location(0.5 * width, 0.75 * height)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(0.5 * width, 0.5 * height)
        elif model == "xhs_slow_down_1":
            actions.w3c_actions.pointer_action.move_to_location(0.5 * width, 0.75 * height)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(0.5 * width, 0.7 * height)
        elif model == "xhs_slow_down":
            actions.w3c_actions.pointer_action.move_to_location(0.5 * width, 0.75 * height)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(0.5 * width, 0.625 * height)
        elif model == "up":
            actions.w3c_actions.pointer_action.move_to_location(0.5 * width, 0.25 * height)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(0.5 * width, 0.75 * height)
        elif model == "slow_up":
            actions.w3c_actions.pointer_action.move_to_location(0.5 * width, 0.25 * height)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(0.5 * width, 0.5 * height)
        elif model == "left":
            actions.w3c_actions.pointer_action.move_to_location(0.25 * width, 0.5 * height)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(0.75 * width, 0.5 * height)
        elif model == "right":
            actions.w3c_actions.pointer_action.move_to_location(0.75 * width, 0.75 * height)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(0.25 * width, 0.25 * height)
        elif model == "notif-open":
            actions.w3c_actions.pointer_action.move_to_location(0.2 * width, 0)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(0.2 * width, height)
        elif model == "notif-close":
            actions.w3c_actions.pointer_action.move_to_location(0.2 * width, height)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(0.2 * width, 0)
        else:
            logger.error(f"model:{model}不支持")
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    @allure.step("下滑寻找隐藏元素并点击")
    def slip_find_click(self, ele, retry=10):
        n = 0
        time.sleep(3)
        re=self.find_element(ele, 10, 'find')
        if re is not None:
            re.click()
            return True
        else:
            while True:
                ele_select = self.find_element(ele, 3, model="find")
                if ele_select is not None:
                    ele_select.click()
                    return True
                else:
                    if n <= 0.5 * retry:
                        self.slip('slow_down')
                    elif 0.5 * retry < n <= retry:
                        self.slip('slow_up')
                    else:
                        logger.debug(f'超过{n}次重试')
                        return False
                    n += 1
                    time.sleep(0.5)

    @allure.step("下滑寻找元素")
    def slip_find(self, ele, retry=10):
        n = 0
        time.sleep(3)
        re=self.find_element(ele, 10, 'find')
        if re is not None:
            return True
        else:
            while True:
                ele_select = self.find_element(ele, 3, model="find")
                if ele_select is not None:
                    return True
                else:
                    if n <= 0.5 * retry:
                        self.slip('slow_down')
                    elif 0.5 * retry < n <= retry:
                        self.slip('slow_up')
                    else:
                        logger.debug(f'超过{n}次重试')
                        return False
                    n += 1
                    time.sleep(0.5)

    @allure.step('隐藏键盘')
    def hide_keyboard(self):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(0.5 * width, 0.1 * height)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    @allure.step('触碰元素')
    def tap(self, x, y):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    @staticmethod
    # 替换元素中带app的
    def re_app(ele):
        if ele.find("${app}") != -1:
            if Set.app == 'eHome':
                ele = ele.replace("${app}", 'eHomeLife')
            elif Set.app == 'refoss' or Set.app == 'Refoss':
                ele = ele.replace("${app}",'Refoss')
            else:
                ele = ele.replace("${app}", Set.app)
        return ele

    # @staticmethod
    # @allure.step("touch元素、图片")
    # def touch(v, model='img', times=1, timeout=15, **kwargs):
    #     if model == 'img':
    #         wait(v, timeout)
    #         touch(v, times, **kwargs)
    #     else:
    #         touch(v, times, **kwargs)

    # @staticmethod
    # def exists(v, msg='test'):
    #     time.sleep(2)
    #     result = exists(v)
    #     if result:
    #         msg = msg + '成功'
    #         filepath = Page().shot(msg)
    #         allure.attach.file(filepath, msg, attachment_type=allure.attachment_type.PNG)
    #         Tools.step_log(f'{msg}，图片识别结果：{result}')
    #     else:
    #         msg = msg + '失败'
    #         filepath = Page().shot(msg)
    #         allure.attach.file(filepath, msg, attachment_type=allure.attachment_type.PNG)
    #         logger.error(f'{msg}图片：{v}')
    #     # assert result
    #     return result

    # @staticmethod
    # def template(filename, threshold=None, target_pos=TargetPos.MID, record_pos=None, resolution=(), rgb=True,
    # scale_max=800, scale_step=0.005):
    # path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # time.sleep(2)
    # return Template(path + '/PageEle/img/' + filename, threshold, target_pos, record_pos, resolution, rgb,
    # scale_max, scale_step)

    def get_window_size(self):
        return self.driver.get_window_size()

    def get_url(self):
        return self.driver.current_url()

    def pop_up_window(self):
        Tools.step_log('')
        if Set.client == "android":
            if self.close_pop_up_window() is True:
                return True
            else:
                pop_ele = 'by.id|android:id/button1'
                if self.find_element(pop_ele, model='assert', timeout=2):
                    self.find_element(pop_ele, 2).click()
                    Tools.step_log("弹窗阻塞ui自动化，已做异常处理")
                    return True
        else:
            if self.find_element("by.ios_predicate|label CONTAINS 'The Internet Connection error'", 10, model='assert'):
                Tools.step_log('没网')
                self.find_element('by.ios_predicate|label == "OK"').click()
                from Common.Flow import Flow
                Flow.switch_wifi_ios()
                return True
            else:
                return self.close_pop_up_window()

    def click_next(self, ps=''):
        if Set.client == 'android':
            next_btn = "by.xpath|//*[ contains(@text, 'Next')]"
        else:
            next_btn = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Next"`]'
        time.sleep(5)
        self.find_element(next_btn).click()
        Tools.step_log(f'{ps}点击next成功')

    def next_check(self, time_sleep=3, ps=''):
        time.sleep(time_sleep)
        if Set.client == 'android':
            next_btn = "by.xpath|//*[ contains(@text, 'Next')]"
        else:
            next_btn = "by.ios_predicate|value='Next'"
        while True:
            if self.find_element(next_btn, time_sleep, model="assert"):
                Tools.step_log(f'{ps}点击next')
            else:
                break

    def find_toast_next(self, toast, retry=5):
        n = 0
        while True:
            n += 1
            if self.find_element(toast, 5, model="assert"):
                Tools.step_log(f"识别到toast：{toast}")
                self.click_next("再次点击")
            else:
                break
            if n >= retry:
                break

    def get_page_source(self):
        return self.driver.page_source

    def close_pop_up_window(self):
        logger.debug('尝试关闭一般弹窗')
        from Common.data_deal import DataDeal
        pop_up_window = DataDeal.get_pop_up_window()
        try:
            source = self.get_page_source()
            for key in pop_up_window.keys():
                if key in source:
                    if Set.client == 'ios':
                        ele = f"by.ios_predicate|label =='{pop_up_window[key]}'"
                    else:
                        ele = f"by.xpath|//*[contains(@text,'{pop_up_window[key]}')]"
                    if self.find_element(ele, model='assert'):
                        self.find_element(ele).click()
                        Tools.step_log(f'成功点掉弹窗{key}')
                        return True
                    else:
                        return False
        except BaseException as e:
            logger.error(e)
            return False

    def terminate_app(self, app):
        self.driver.terminate_app(app)
        logger.debug(f'终止app{app}')

    def activate_app(self, app):
        self.driver.activate_app(app)
        logger.debug(f'激活app{app}')

    def restart_app(self, app):
        self.terminate_app(app)
        self.activate_app(app)

    def sp_tap(self, ele, model='mid_down'):
        size = self.find_element(ele).size
        location = self.find_element(ele).location
        if model == 'mid_down':
            x = 0.5 * size['width'] + location['x'] - 10
            y = location['y'] + size['height'] - 5
            self.tap(x, y)

    def clipboard_content(self):
        return self.driver.get_clipboard()        

    def swip(self):
        # 计算滑动起始点和结束点的坐标
        start_x = 850  # 起始点横坐标为屏幕宽度的80%
        start_y =  2103 # 起始点纵坐标为屏幕高度的50%
        end_x = 245 # 结束点横坐标为屏幕宽度的20%
        end_y = 2089

        # 执行向左滑动操作
        self.driver.swipe(start_x,start_y,end_x,end_y,duration=1000)

if __name__ == '__main__':
    pass
