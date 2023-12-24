# -*- coding: utf-8 -*-
# @Time    : 2022/6/23 13:40
# @Author  : XuLei
# @FileName: Navi_Bar.py
# @Software: PyCharm
import allure
from PageEle.BasePage import Page
from PageEle.selector.NaviSelector import *


class NaviBar(Page):

    @allure.step("进入用户模块")
    def go_user_module(self):
        self.find_element(NaviSelector.USER_MODEL).click()
        self.assert_ele(NaviSelector.USER_TITLE, '进入用户模块')

    def go_home_module(self):
        self.find_element(NaviSelector.HOME_MODEL).click()
        self.assert_ele(NaviSelector.HOME_TITLE, "进入home模块")

    def go_smart_module(self):
        self.find_element(NaviSelector.SMART_MODEL).click()
        self.assert_ele(NaviSelector.SMART_TITLE, "进入smart模块")

    def go_forum_module(self):
        self.find_element(NaviSelector.FORUM_MODEL).click()
        self.assert_ele(NaviSelector.FORUM_TITLE, '进入forum模块')

    def go_hot_deal(self):
        self.find_element(NaviSelector.HOT_DEAL_MODEL).click()
        self.assert_ele(NaviSelector.HOT_DEAL_TITLE, '进入hot deal模块')
