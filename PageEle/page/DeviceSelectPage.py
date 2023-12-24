# -*- coding: utf-8 -*-
# @Time    : 2022/6/24 16:05
# @Author  : XuLei
# @FileName: DeviceSelectPage.py
# @Software: PyCharm
import time
from PageEle.BasePage import Page
from PageEle.selector.DeviceSelect import *
from Common.Tools import Tools
import allure


class DeviceSelectPage(Page):

    @allure.step("开始搜索设备")
    def search_device(self, device_name):
        self.find_element(DeviceSelector.SEARCH).send_keys(device_name)

    @allure.step("点击设备分类")
    def enter_device_cate(self, cate_name):
        ele = Tools.re_ele(DeviceSelector.CATE_REPLACE, cate_name)
        self.find_element(ele).click()

    @allure.step("more设备")
    def more_device(self):
        if self.find_element(DeviceSelector.MORE,model='assert'):
            self.find_element(DeviceSelector.MORE).click()

    @allure.step("进入设备配网")
    def device_dn(self, device_name):
        if self.find_element(DeviceSelector.CHOOSE_THE_MODEL,5,model='assert'):
            ele = Tools.re_ele(DeviceSelector.DEVICE_REPLACE, device_name)
            self.slip_find_click(ele)
            Tools.step_log('选择具体设备名称后，进行配网')
        else:
            Tools.step_log('直接进行配网')
