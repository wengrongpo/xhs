# -*- coding: utf-8 -*-
# @Time    : 2022/6/23 11:38
# @Author  : XuLei
# @FileName: common.py
# @Software: PyCharm
import time

from PageEle.page.DeviceDnPage import DevicePage
from PageEle.page.DeviceSelectPage import DeviceSelectPage
from PageEle.page.HomePage import HomePage
from PageEle.page.SmartPage import SmartPage
from PageEle.page.UserPage import UserPage
from PageEle.page.Navi_Bar import NaviBar
from PageEle.selector.UserSelector import UserSelector
from PageEle.BasePage import Page
import allure
from Common.log import logger
from Common.Tools import Tools


# 维护公共的ui自动化流程
class Flow:
    @staticmethod
    def login(user, pwd, judge='normal'):
        from Common.set import Set
        if Set.re_login != 0:
            page = NaviBar()
            page.go_user_module()
            page = UserPage()
            """进入注册登录页面"""
            page.start_login()
            page.login_in()
            page.login(user, pwd, judge)
            #  校验
            page.login_judge(judge, user)

    @staticmethod
    def sign_up(email, pwd, judge="normal"):
        page = NaviBar()
        page.go_user_module()
        page = UserPage()
        page.start_login()
        page.sign_up(email, pwd, judge)
        page.signup_judge(judge, email, pwd)

    @staticmethod
    def log_out():
        page = NaviBar()
        page.go_user_module()
        page = UserPage()
        page.log_out()

    def real_log_out(self):
        Page().close_app()
        Page().launch_app()
        self.log_out()
        Page().close_app()
        Page().launch_app()

    @staticmethod
    def assert_log_out():
        page = Page()
        page.close_app()
        page.launch_app()
        page = NaviBar()
        page.go_user_module()
        if page.find_element(UserSelector.START_LOGIN, 7, "assert"):
            Tools.step_log("未登录状态无需清除登录态")
        else:
            page = UserPage()
            page.log_out()
            page.close_start_login()
            Tools.step_log("账号之前为登录状态，已清除登录态")

    @staticmethod
    def device_dn_ahead(device_name, device_cate):
        page = NaviBar()
        page.go_home_module()
        page = HomePage()
        page.plus_device()
        page = DeviceSelectPage()
        page.search_device(device_name)
        page.enter_device_cate(device_cate)
        page.device_dn(device_name)

    @staticmethod
    def remove_device():
        page = NaviBar()
        page.go_home_module()

    @staticmethod
    def device_dn_later(test_data):
        page = DevicePage()
        page.turn_on_location()
        from Common.set import Set
        if test_data["device_version"] == "hk" and Set.client == 'ios':
            page.bind_device(test_data["device_version"], test_data["device_icon_name"], test_data["setup_code"],
                             test_data["wifi_name"], test_data['device_nickname'])
        else:
            page.bind_device(test_data["device_version"],
                             wifi_name=test_data["wifi_name"])
            page.edit_device_name(test_data["device_nickname"])
            page.customize_your_icon()
            page.join_your_home_wifi(test_data["home_wifi_name"], test_data["home_wifi_pwd"])

    @staticmethod
    def remove_devices(uuid, device_name):
        page = NaviBar()
        page.go_home_module()
        page = HomePage()
        if page.select_device(device_name):
            Tools.check_online(uuid,device_name)
            page.remove_device(device_name)
            Tools.sleep(30, 'WAIT')

    @staticmethod
    def get_dn_flow(device_name):
        Tools.step_log(f"{device_name}选择配网流程")
        page = DevicePage()
        if device_name == "MSS110":
            page.mss110_dn_flow()
        elif device_name == "MSS425E":
            page.mss425e_dn_flow()
        elif device_name == "MSS310":
            page.mss310_dn_flow()
        elif device_name == "MSL120":
            page.smart_bulb_msl120_dn_flow()
        elif device_name == "MAP100":
            page.smart_air_purifier_dn_flow()
        elif device_name == "MOD100":
            page.smart_humidifier_diffuser_dn_flow()
        elif device_name == "MSG100":
            page.smart_garage_door_opener_dn_flow()
        else:
            Tools.step_log(f"device_name:{device_name}暂不支持", model='error')

    @staticmethod
    def create_routine(model, ds_name, routine_name, action=None):
        page = SmartPage()
        page.routine_tab()
        page.click_plus()
        page.add_routine(model, ds_name, routine_name, action)

    @staticmethod
    def create_scene(scene_name, device_list, scene_icon='away'):
        page = SmartPage()
        page.scene_tab()
        page.click_plus()
        page.create_scene(scene_name, scene_icon)
        page.select_device(device_list)
        page.scene_created()

    @staticmethod
    def switch_wifi_ios():
        from PageEle.selector.DeviceNet import DeviceNet
        page = Page()
        page.terminate_app('com.apple.Preferences')
        page.activate_app('com.apple.Preferences')
        page.find_element(DeviceNet.SET_WIFI).click()
        wifi_name = Tools.re_ele(DeviceNet.WIFI_NAME, 'TEST_UI')
        time.sleep(10)
        page.slip_find_click(wifi_name)
        time.sleep(5)
        from Common.set import Set
        page.activate_app(Set.Apk)
        Tools.step_log('成功切换wifi')
