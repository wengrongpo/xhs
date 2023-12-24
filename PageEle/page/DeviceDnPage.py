# -*- coding: utf-8 -*-
# @Time    : 2022/6/24 18:03
# @Author  : XuLei
# @FileName: DeviceDnPage.py
# @Software: PyCharm
import time
import allure
from PageEle.BasePage import Page
from PageEle.selector.DeviceNet import *
from Common.Tools import Tools
from func_timeout import func_set_timeout


class DevicePage(Page):
    def mss110_dn_flow(self):
        self.click_next("plug in smart plug mini")
        self.click_next("check the led light")
        # self.find_toast_next(DeviceNet.NO_DEVICE_TOAST)

    def mss310_dn_flow(self):
        self.click_next("plug in smart plug mini")
        self.click_next("check the led light")

    def mss425e_dn_flow(self):
        self.click_next("Power up Smart Surge Protector")
        # self.find_toast_next(DeviceNet.NO_DEVICE_TOAST)

    def smart_air_purifier_dn_flow(self):
        self.click_next("before we get started")
        self.click_next("power up device")
        # self.next_check(ps='未连接wifi再次')
        # self.find_toast_next(DeviceNet.NO_DEVICE_TOAST)

    def smart_bulb_msl120_dn_flow(self):
        self.click_next("install your smart bulb")
        self.click_next("power up your smart bulb")
        # self.find_toast_next(DeviceNet.NO_DEVICE_TOAST)

    def smart_humidifier_diffuser_dn_flow(self):
        self.click_next("before we get started")
        self.click_next("power up device")

    def smart_garage_door_opener_dn_flow(self):
        self.find_element(DeviceNet.GARAGE_DOOR_OPENER_SKIP).click()
        self.click_next("Connect Power Cable")
        self.click_next("Check the Status LED")

    @allure.step("打开定位")
    def turn_on_location(self):
        if self.find_element(DeviceNet.TURN_ON_LOCATION, 5, model='assert'):
            self.find_element(DeviceNet.SURE).click()
            # miui权限弹窗
        # if self.find_element(DeviceNet.MIUI_PERMISSION, 5, model='assert'):
        #     self.find_element(DeviceNet.MIUI_LOCATION_PERMISSION).click()

    @allure.step("ios选择设备版本")
    def select_version(self, version):
        if self.find_element(DeviceNet.SELECT_VERSION, model='assert'):
            self.assert_ele(DeviceNet.SELECT_VERSION, "ios选择设备版本")
            if version == 'hk':
                self.find_element(DeviceNet.HK).click()
            elif version == "no-hk":
                self.find_element(DeviceNet.NO_HK).click()
            else:
                logger.error(f"version error:{version}")

    @allure.step("进入wifi设置页面")
    def goto_wifi_setting(self, wifi_name):
        self.assert_ele(DeviceNet.CONNECT_TO_DEVICE, "进入连接设备页面")
        self.find_element(DeviceNet.GOTO_WIFI_SETTINGS).click()
        re=self.find_element(DeviceNet.SET_WIFI, model='assert')
        if re is False or re is None:
            self.terminate_app('com.apple.Preferences')
            self.activate_app('com.apple.Preferences')
        self.find_element(DeviceNet.SET_WIFI).click()
        wifi_name = Tools.re_ele(DeviceNet.WIFI_NAME, wifi_name)
        time.sleep(20)
        self.find_element(DeviceNet.WIFI_SWITCH,30).click()
        Tools.sleep(2)
        self.find_element(DeviceNet.WIFI_SWITCH,30).click()
        self.slip_find_click(wifi_name)
        # self.find_element(wifi_name).click()
        Tools.sleep(20)
        self.activate_app(Set.desired_caps["app"])
        time.sleep(15)

    @allure.step("添加hk设备")
    @func_set_timeout(600)
    def add_homekit_device(self, device_icon_name, setup_code, device_nickname):
        self.assert_ele(DeviceNet.ADD_HOMEKIT_DEVICE, "进入添加homekit设备")
        self.find_element(DeviceNet.ADD_HOMEKIT_NEXT).click()
        self.assert_ele(DeviceNet.ADD_ACCESSORY, "进入ADD_ACCESSORY弹窗")
        self.sp_tap(DeviceNet.CANT_SCAN)
        device_icon = Tools.re_ele(DeviceNet.DEVICE_ICON, device_icon_name)
        self.find_element(device_icon, 150).click()
        code_list = [a for a in setup_code]
        for num in code_list:
            setup_code_ele = Tools.re_ele(DeviceNet.SETUP_CODE, num)
            self.find_element(setup_code_ele).click()
        self.find_element(DeviceNet.CONTINUE_BT).click()
        time.sleep(20)
        if self.find_element(DeviceNet.HK_DEVICE_IDENTIFY, 300, model='assert'):
            self.find_element(DeviceNet.CONTINUE_BT, timeout=60).click()
            self.find_element(DeviceNet.HK_DEVICE_NAME).clear()
            self.find_element(DeviceNet.HK_DEVICE_NAME).clear()
            self.find_element(DeviceNet.HK_DEVICE_NAME).send_keys(device_nickname)
            self.find_element(DeviceNet.CONTINUE_BT).click()
            self.find_element(DeviceNet.CONTINUE_BT).click()
            if self.find_element(DeviceNet.CONTINUE_BT, model='assert'):
                self.find_element(DeviceNet.CONTINUE_BT).click()
            self.find_element(DeviceNet.BIND_DONE, 60).click()
        else:
            self.add_homekit_device(device_icon_name, setup_code, device_nickname)
        # else:
        #     if self.find_element(DeviceNet.HK_BIND_FAIL, model='assert'):
        #         self.find_element(DeviceNet.HK_BIND_FAIL).click()
        #         self.add_homekit_device(self, device_icon_name, setup_code, device_nickname)
        #     elif self.find_element(DeviceNet.HK_BIND_FAIL_FINE, model='assert'):
        #         self.find_element(DeviceNet.HK_BIND_FAIL).click()
        #         time.sleep(2)
        #         self.find_element(DeviceNet.HK_BIND_FAIL).click()

    @allure.step("安卓重新扫描wifi，未扫到重试")
    def rescan(self, wifi_name, retry=5):
        if self.find_element(DeviceNet.CONNECT_WIFI, 5, model='assert'):
            Tools.step_log("同类wifi唯一，直接连接wifi")
        else:
            self.assert_ele(DeviceNet.Multiple_Device_Found, "进入找到多个设备页面")
            wifi_select = Tools.re_ele(DeviceNet.ANDROID_WIFI_SELECT, wifi_name)
            n = 0
            while n <= retry:
                if self.find_element(wifi_select, 5, model="find"):
                    self.find_element(wifi_select).click()
                    break
                else:
                    time.sleep(3)
                    n+=1
                    self.find_element(DeviceNet.RESCAN).click()

    @allure.step("客户端连接设备wifi")
    def connect_wifi(self):
        self.find_element(DeviceNet.CONNECT_WIFI).click()
        # self.assert_ele(DeviceNet.BIND_SUCCESS, "客户端连接设备wifi", 40)

    @allure.step("连接成功后，编辑设备名称")
    def edit_device_name(self, name=None):
        self.assert_ele(DeviceNet.RENAME_DEVICE, "编辑设备名称", 60)
        if name is not None:
            self.find_element(DeviceNet.DEVICE_NAME).clear()
            self.find_element(DeviceNet.DEVICE_NAME).send_keys(name)
            self.hide_keyboard()
            self.click_next('编辑设备名称页面')

    @allure.step("进入选择icon页面,点击next")
    def customize_your_icon(self):
        if self.find_element(DeviceNet.JOIN_YOUR_HOME_WIFI, 10, "assert"):
            Tools.step_log("该设备配网未进入选择icon页面")
        else:
            self.assert_ele(DeviceNet.CUSTOMIZE_YOUR_ICON, "进入定义设备icon页面")
            time.sleep(2)
            self.click_next("进入选择icon页面")

    @allure.step("选择wifi后，连接wifi")
    def join_your_home_wifi(self, home_wifi_name, wifi_pwd):
        time.sleep(3)
        self.assert_ele(DeviceNet.JOIN_YOUR_HOME_WIFI, "进入wifi选择页面")
        self.find_element(DeviceNet.WIFI_BT).click()
        new_network = Tools.re_ele(DeviceNet.NEW_NETWORK, home_wifi_name)
        self.assert_ele(DeviceNet.REFRESH_WIFI, "进入选择wifi")
        n=0
        while self.slip_find_click(new_network, retry=5) is False:
            self.find_element(DeviceNet.REFRESH_WIFI).click()
            Tools.sleep(5,'等待固件返回wifi')
            if self.slip_find_click(new_network):
                break
            if n>5:
                Tools.step_log('已重试5次，无法连接wifi','warn')
                assert False
        self.find_element(DeviceNet.PWD).clear()
        self.find_element(DeviceNet.PWD).send_keys(wifi_pwd)
        self.hide_keyboard()
        self.click_next("选择wifi后，连接wifi")

    @allure.step("设备绑定家庭wifi")
    def wifi_bind(self, model='normal', device_version=None, device_nickname=None, device_cate=None):
        if model == 'bind_error':
            self.assert_ele(DeviceNet.DN_ERROR, '设备入网失败', timeout=300)
        elif model == 'normal':
            self.assert_ele(DeviceNet.WIFI_BIND_SUCCESS, "设备成功绑定家庭wifi", 180)
            if device_cate =='Smart Garage Door Opener':
                Tools.step_log("点击SKIP_HARDWARE_DEPLOYMENT")
                self.find_element(DeviceNet.SKIP_HARDWARE_DEPLOYMENT).click()
                self.find_element(DeviceNet.NOT_NOW).click()
                time.sleep(5)
                self.close_app()
                self.launch_app()
                self.change_hk_name(device_version, device_cate, device_nickname)
            else:
                self.find_element(DeviceNet.DONE).click()
                self.find_element(DeviceNet.NOT_NOW).click()
                self.change_hk_name(device_version, device_cate, device_nickname)
                self.close_device(device_nickname)
        else:
            Tools.step_log('model error')

    #  选择version'
    def bind_device(self, device_version: str, device_icon_name=None, setup_code=None, wifi_name=None,
                    device_nickname=None):
        if Set.client == 'ios' and device_version == "hk":
            self.select_version(device_version)
            self.add_homekit_device(device_icon_name, setup_code, device_nickname)
        elif Set.client == 'ios' and device_version == "no-hk":
            self.select_version(device_version)
            self.goto_wifi_setting(wifi_name)
        # 安卓 直接扫描wifi
        elif Set.client == 'android':
            self.rescan(wifi_name)
            self.connect_wifi()
        else:
            logger.error("Set.client or device_version error")

    @allure.step('判断是否更改hk设备名称')
    def change_hk_name(self, device_version, device_cate, device_nickname):
        if Set.client == 'ios' and device_version == 'hk':
            from PageEle.selector.HomeSelector import HomeSelector
            device_name = Tools.re_ele(HomeSelector.DEVICE_NAME, device_cate)
            if self.find_element(device_name, model="assert"):
                logger.info('设备名称未更改手动更改')
                from PageEle.page.HomePage import HomePage
                page = HomePage()
                page.device_detail(device_cate)
                page.device_more()
                page.change_device_name(device_nickname)

    def close_device(self, device_name):
        from PageEle.selector.HomeSelector import HomeSelector
        switch = Tools.re_ele(HomeSelector.DEVICE_SWITCH, device_name)
        if self.find_element(switch, 20, model='assert'):
            self.slip_find_click(switch)
            Tools.step_log(f'配网后，关闭设备{device_name}开关')
        else:
            Tools.step_log('配网后，该设备无一般开关按钮')
