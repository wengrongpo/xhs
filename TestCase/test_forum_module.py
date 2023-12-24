# -*- coding: utf-8 -*-
# @Time    : 2023/6/20 10:51
# @Author  : XuLei
# @FileName: test_forum_module.py
# @Software: PyCharm
import threading
import time

from PageEle.page.HomePage import HomePage
from PageEle.page.ForumPage import ForumPage
from PageEle.page.UserPage import UserPage
from Common.Flow import Flow
from Common.Tools import Tools
import allure
import pytest

from Common.set import Set

from PageEle.page.Navi_Bar import NaviBar
from Common.data_deal import DataDeal
from Common.Tools import Tools


@allure.story('Forum模块')
@pytest.mark.parametrize("test_data", DataDeal().get_test_data('test_verify_forum_tag_with_login'))
def test_verify_forum_tag_with_login(test_data):
    Tools.start_deal(test_data["title"], test_data)
    Flow.login(test_data["user"], test_data["pwd"])
    page = NaviBar()
    page.go_forum_module()
    page = ForumPage()
    page.click_gotcha()
    page.modify_search_function()
    page.modify_site_to_japan()
    page.modify_forum_tag_with_login_in()


@allure.story('Forum模块')
@pytest.mark.parametrize("test_data", DataDeal().get_test_data('test_verify_forum_tag_with_logout'))
def test_verify_forum_tag_with_logout(test_data):
    Tools.start_deal(test_data["title"], test_data)
    Flow.login(test_data["user"], test_data["pwd"])
    Flow.log_out()
    page = UserPage()
    page.close_start_login()
    page = NaviBar()
    page.go_forum_module()
    page = ForumPage()
    page.click_gotcha()
    page.modify_forum_tag_with_logout()