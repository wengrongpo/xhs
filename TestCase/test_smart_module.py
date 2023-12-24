# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 10:34
# @Author  : XuLei
# @FileName: test_smart_module.py
# @Software: PyCharm
import threading
import time

import allure

from Common.Flow import Flow
from Common.Tools import Tools
import pytest

from Common.set import Set
from PageEle.page.HomePage import HomePage
from PageEle.page.SmartPage import SmartPage
from PageEle.page.Navi_Bar import NaviBar
from Common.data_deal import DataDeal
from Common.Tools import Tools


def check_result():
    if Set.check_result is False:
        Tools.step_log('❎校验设备返回数据存在失败')
        assert Set.check_result
    elif Set.check_result is True:
        Tools.step_log('✅校验设备返回数据均正确')
        assert Set.check_result


@allure.story('Smart模块')
@pytest.mark.parametrize("test_data", DataDeal.get_test_data("test_modify_scene_schedule"))
def test_modify_scene_schedule(test_data):
    Tools.check_online_all()
    Tools.start_deal(test_data["title"], test_data)
    Flow.login(test_data["user"], test_data["pwd"])
    page = NaviBar()
    page.go_smart_module()
    page = SmartPage()
    page.delete_all_scene()
    Flow.create_scene(test_data['scene_one'], test_data['scene_one_device_list'], 'home')
    Flow.create_scene(test_data['scene_two'], test_data['scene_two_device_list'], 'home')
    Flow.create_scene('away', test_data['scene_two_device_list'], 'away')
    page.routine_tab()
    page.delete_all_routine()
    Flow.create_routine('schedule', test_data['scene_one'], test_data['scene_schedule_name'])
    Tools.uuid_rule_deal(uuid_rule=test_data['check_rule'], time_diff=300, msg='5分钟后打开灯泡、排插、香薰机/插座')
    page.routine_switch(test_data['scene_schedule_name'])
    page.routine_detail(test_data["scene_schedule_name"])
    page.edit_routine('schedule', test_data['new_scene_schedule_name'], new_action_scene=test_data["scene_two"])
    page.back_routine()
    page.scene_tab()
    Tools.end_deal()
    page.delete_scene(test_data['scene_one'])
    page.delete_scene(test_data['scene_two'])
    page.run_scene('away')
    page.delete_scene('away')
    check_result()

@allure.story('Smart模块')
@pytest.mark.parametrize("test_data", DataDeal.get_test_data("test_routine_check"))
def test_routine_check(test_data):
    Tools.check_online_all()
    Tools.start_deal(test_data["title"], test_data)
    Flow.login(test_data["user"], test_data["pwd"])
    page = NaviBar()
    page.go_smart_module()
    page = SmartPage()
    page.delete_all_scene()
    Flow.create_scene(test_data['init_scene'], test_data['device_list'], 'home')
    page.run_scene(test_data['init_scene'])
    Tools.uuid_rule_deal(test_data['init_check'], msg='校验：先打开灯和插座')
    page.delete_scene(test_data['init_scene'])
    page.routine_tab()
    page.delete_all_routine()
    page.click_plus()
    page.add_routine(test_data["model_one"], test_data["ds_name_one"], test_data["routine_name_one"],
                     test_data['action_one'])
    Tools.uuid_rule_deal(test_data['uuid_rule_one'], time_diff=300, msg='校验：灯5分钟后关闭')
    page.click_plus()
    page.add_routine(test_data["model_two"], test_data["ds_name_two"], test_data["routine_name_two"],
                     Tools.get_value(test_data, "action_two"))
    Tools.uuid_rule_deal(test_data['uuid_rule_two'], time_diff=300, msg='110 plug 在创建5分钟后关闭')
    page.routine_detail(test_data["routine_name_one"])
    page.edit_routine(test_data["model_two"], test_data["new_name"], Tools.get_value(test_data, "new_device"),
                      Tools.get_value(test_data, 'new_action_scene'))
    page.back_routine()
    Tools.end_deal()
    page.delete_routine(test_data["new_name"])
    page.delete_routine(test_data["routine_name_two"])
    check_result()


@allure.story('Smart模块')
@pytest.mark.parametrize("test_data", DataDeal.get_test_data("test_scene_check"))
def test_scene_check(test_data):
    Tools.check_online_all()
    Tools().start_deal(test_data["title"], test_data)
    Flow.login(test_data["user"], test_data["pwd"])
    page = NaviBar()
    page.go_smart_module()
    page = SmartPage()
    page.delete_all_scene()
    Flow.create_scene(test_data['all_on_scene_name'], test_data['device_list'], 'home')
    page.run_scene(test_data['all_on_scene_name'])
    Flow.create_scene(test_data['scene_name'], test_data['device_list'])
    page.run_scene(test_data['scene_name'])
    Tools.uuid_rule_deal(test_data['uuid_rule'], msg='校验：run scene设备关闭')
    page.run_scene(test_data['all_on_scene_name'])
    page.routine_tab()
    page.delete_all_routine()
    Flow.create_routine('schedule', test_data['scene_name'], 'Test off')
    Tools.uuid_rule_deal(test_data['uuid_rule'], time_diff=300, msg='校验：routine执行成功时，设备5分钟后全部关闭')
    time.sleep(60)
    # page.scene_tab()
    # page.run_scene(test_data['all_on_scene_name'])
    page.routine_tab()
    Flow.create_routine('schedule', test_data['all_on_scene_name'], test_data['disable_routine_name'])
    page.routine_switch(test_data['disable_routine_name'])
    Tools.uuid_rule_deal(uuid_rule=test_data['uuid_rule'], time_diff=300, msg='校验：已禁用routine不会执行')
    Tools.end_deal()
    page.routine_tab()
    page.routine_detail('Test off')
    page.edit_routine('schedule', 'New Test off', new_action_scene=test_data['all_on_scene_name'])
    page.back_routine()
    Tools.uuid_rule_deal(uuid_rule=test_data['uuid_rule'], time_diff=100, msg='routine过期不会生效')
    page.scene_tab()
    Tools.end_deal()
    time.sleep(10)
    page.delete_scene(test_data['scene_name'])
    page.delete_scene(test_data['all_on_scene_name'])
    Tools.step_log('删除已创建数据，保持环境干净')
    check_result()
