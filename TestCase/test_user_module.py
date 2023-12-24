# -*- coding: utf-8 -*-
# @Time    : 2022/7/8 1:45 PM
# @Author  : XuLei
# @FileName: test_user_module.py
# @Software: PyCharm
import time
from PageEle.page.Navi_Bar import NaviBar
from PageEle.page.UserPage import UserPage
import allure
import pytest
from Common.Flow import Flow, Tools
from PageEle.BasePage import Page
from Common.data_deal import DataDeal
from Common.set import Set
from Common.log import logger


@allure.story('User模块')
@pytest.mark.parametrize("test_data", DataDeal.get_test_data('test_signup_normal'))
def test_signup_normal(test_data):
    Tools.start_deal(test_data["title"], test_data)
    Flow.sign_up(test_data["user"], test_data["pwd"], test_data["judge"])
    Flow().real_log_out()
    Flow.login(test_data["user"], test_data["pwd"])


@allure.story('User模块')
@pytest.mark.parametrize("test_data", DataDeal.get_test_data('test_signup_exceptions'))
def test_signup_exceptions(test_data):
    Tools.start_deal(test_data["title"], test_data)
    Flow.sign_up(test_data["user"], test_data["pwd"], test_data["judge"])


@allure.story('User模块')
@pytest.mark.parametrize("test_data", DataDeal().get_test_data('test_login'))
def test_login(test_data):
    Tools.start_deal(test_data["title"], test_data)
    Flow.login(test_data["user"], test_data["pwd"], test_data["judge"])


@allure.story('User模块')
@pytest.mark.parametrize("test_data", DataDeal().get_test_data('test_forgot_change_pwd'))
def test_forgot_change_pwd(test_data):
    Tools.start_deal(test_data["title"], test_data)
    page = NaviBar()
    page.go_user_module()
    page = UserPage()
    page.start_login()
    page.login_in()
    pwd = page.forget_pwd(Set.email, Set.changed_pwd, test_data["judge"])
    page.login_in()
    page.login(Set.email, pwd)
    page = NaviBar()
    page.go_user_module()
    page = UserPage()
    page.user_detail()
    Tools.step_log('忘记密码后修改密码 清洗密码数据')
    page.change_pwd(Set.origin_pwd)
    page.login_in()
    page.login(Set.email, Set.origin_pwd)
    Tools.step_log('忘记密码后修改密码正确登录')


@allure.story('User模块')
@pytest.mark.parametrize("test_data", DataDeal().get_test_data('test_change_email_delete_account'))
def change_email_delete_account(test_data):
    Tools.start_deal(test_data["title"], test_data)
    pwd = test_data['pwd']
    Flow.sign_up(test_data["signup_email"], pwd)
    page = NaviBar()
    page.go_user_module()
    page = UserPage()
    page.user_detail()
    page.change_email(Set.del_email, pwd)
    page.login_in()
    page.login(Set.del_email, pwd)
    logger.info('开始删除账号，完成用例闭环运行')
    page = NaviBar()
    page.go_user_module()
    page = UserPage()
    page.user_detail()
    page.delete_account(pwd)


@allure.story('User模块')
@pytest.mark.parametrize("test_data", DataDeal().get_test_data('test_change_pwd_no_sms'))
def test_change_pwd_no_sms(test_data):
    Tools.start_deal(test_data["title"], test_data)
    Flow.sign_up(test_data['signup_user'], test_data['pwd'])
    page = UserPage()
    page.user_detail()
    page.change_pwd_no_sms(test_data['new_pwd'])
    page.log_out()
    page.reset()
    Flow.login(test_data["signup_user"], test_data['new_pwd'])

@allure.story('User模块')
@pytest.mark.parametrize("test_data", DataDeal().get_test_data('test_integration_meross'))
def test_integration_meross(test_data):
    Tools.start_deal(test_data["title"], test_data)
    Flow.login(test_data["user"], test_data["pwd"])
    page = NaviBar()
    page.go_user_module()
    page = UserPage()
    page.integration_alexa()
    page.integration_google()
