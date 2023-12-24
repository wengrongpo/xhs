# -*- coding: utf-8 -*-
# @Time    : 2022/9/7 16:41
# @Author  : XuLei
# @FileName: SmartPage.py
# @Software: PyCharm
import time

import allure

from Common.Tools import Tools
from PageEle.BasePage import Page
from PageEle.selector.SmartSelector import *


class SmartPage(Page):
    def routine_tab(self):
        self.hide_keyboard()
        self.slip('slow_up')
        self.find_element(SmartSelector.ROUTINE_TAB, 60).click()
        Tools.step_log('进入routine tab')

    def scene_tab(self):
        self.find_element(SmartSelector.SCENE_TAB).click()
        Tools.step_log('进入scene tab')

    def click_plus(self):
        self.find_element(SmartSelector.PLUS_BT).click()
        Tools.step_log('点击+号，创建scene or routine')

    def add_routine(self, model, ds_name, routine_name, action=None):
        self.assert_ele(SmartSelector.ROUTINE_SETUP, '进入添加routine页面')
        if model == 'auto_off':
            self.find_element(SmartSelector.AUTO_OFF).click()
            self.add_auto_off_routine(ds_name, routine_name)
        elif model == 'schedule':
            self.find_element(SmartSelector.ON_OFF_SCHEDULE).click()
            self.add_schedule(ds_name, routine_name, action)
        else:
            logger.error(f'model error:{model}')

    def routine_detail(self, routine_name):
        routine_name = Tools.re_ele(SmartSelector.ROUTINE_DETAIL, routine_name)
        time.sleep(3)
        self.find_element(routine_name, 30).click()
        self.assert_ele(SmartSelector.ROUTINE_DETAIL_TITLE, '进入编辑routine页面')

    def routine_switch(self, routine_name: str):
        routine_switch_ele = Tools.re_ele(SmartSelector.ROUTINE_SWITCH, routine_name)
        time.sleep(3)
        self.find_element(routine_switch_ele).click()
        Tools.step_log(f'启禁用{routine_name}routine')

    def edit_routine(self, model, new_name, new_device=None, new_action_scene=None):
        if model == 'auto_off':
            self.edit_name(new_name)
            self.edit_device(new_device)
        elif model == 'schedule':
            if new_device is None:
                self.edit_name(new_name)
                self.routine_edit_scene(new_action_scene)
            else:
                self.edit_name(new_name)
                self.edit_device(new_device)
                self.edit_device_status(new_action_scene)
        else:
            logger.error('error')

    def back_routine(self):
        time.sleep(2)
        self.find_element(SmartSelector.BACK, timeout=20).click()
        Tools.step_log("回到routine tab页面")

    def routine_edit_scene(self, new_scene):
        Tools.step_log("编辑routine中scene")
        self.find_element(SmartSelector.ROUTINE_EDIT_SCENE).click()
        scene = Tools.re_ele(SmartSelector.SELECT_DEVICE_OR_SCENE, new_scene)
        self.find_element(scene).click()
        self.find_element(SmartSelector.SAVE).click()

    def edit_device_status(self, action):
        Tools.step_log("编辑设备执行动作")
        self.find_element(SmartSelector.EDIT_STATUS).click()
        action = Tools.re_ele(SmartSelector.SELECT_STATUS, action)
        self.find_element(action).click()
        self.find_element(SmartSelector.SAVE).click()

    def edit_name(self, new_name):
        Tools.step_log("编辑routine名称")
        self.find_element(SmartSelector.EDIT_NAME).click()
        self.find_element(SmartSelector.NEW_NAME).clear()
        self.find_element(SmartSelector.NEW_NAME).send_keys(new_name)
        self.find_element(SmartSelector.SAVE).click()

    def edit_device(self, device_name):
        Tools.step_log("编辑设备名称")
        self.find_element(SmartSelector.EDIT_DEVICE).click()
        select_device = Tools.re_ele(SmartSelector.SELECT_DEVICE_OR_SCENE, device_name)
        self.find_element(select_device).click()
        self.find_element(SmartSelector.SAVE).click()

    def delete_routine(self, routine_name):
        self.routine_detail(routine_name)
        self.find_element(SmartSelector.DELETE_ROUTINE).click()
        self.find_element(SmartSelector.CONFIRM_DELETE).click()
        routine_selector = Tools.re_ele(SmartSelector.ROUTINE_DETAIL, routine_name)
        time.sleep(1)
        if self.find_element(routine_selector, timeout=3, model='assert') is None:
            Tools.step_log(f"成功删除{routine_name}", model='info')

    def add_auto_off_routine(self, device_name, routine_name):
        device_name = Tools.re_ele(SmartSelector.SELECT_DEVICE, device_name)
        self.assert_ele(SmartSelector.SELECT_DEVICE_TITLE, '进入选择设备页面')
        self.find_element(device_name).click()
        self.select_time()
        self.name_routine(routine_name)

    def name_routine(self, routine_name):
        self.assert_ele(SmartSelector.NAME_ROUTINE_TITLE, '进入命名routine页面')
        self.find_element(SmartSelector.NAME_ROUTINE).send_keys(routine_name)
        self.find_element(SmartSelector.SAVE_ROUTINE).click()
        if self.find_element(SmartSelector.ROUTINE_SUCCESS, timeout=5, model='assert'):
            self.find_element(SmartSelector.ROUTINE_SUCCESS).click()

    def add_schedule(self, name, routine_name, action=None):
        self.assert_ele(SmartSelector.SELECT_DEVICE_OR_SCENE_TITLE, '进入选择设备、场景页面')
        name = Tools.re_ele(SmartSelector.SELECT_DEVICE_OR_SCENE, name)
        self.slip_find_click(name)
        if action is not None:
            self.select_status(action)
            self.select_time()
            self.name_routine(routine_name)
        else:
            self.select_time()
            self.name_routine(routine_name)

    def select_status(self, action):
        self.assert_ele(SmartSelector.SELECT_STATUS_TITLE, '进入选择设备状态')
        action = Tools.re_ele(SmartSelector.SELECT_STATUS, action)
        self.find_element(action).click()

    def select_time(self):
        self.assert_ele(SmartSelector.SELECT_TIME_TITLE, '进入选择时间页面')
        self.find_element(SmartSelector.SELECT_TIME_NEXT).click()

    def create_scene(self, scene_name, scene_icon='away'):
        self.assert_ele(SmartSelector.CREATE_SCENE_TITLE, '进入创建scene页面')
        if scene_icon == 'home':
            self.find_element(SmartSelector.HOME_SCENE).click()
            logger.debug('选择home 场景')
        elif scene_icon == 'away':
            pass
        else:
            logger.error('error')
        self.find_element(SmartSelector.CREATE_SCENE_NAME).clear()
        self.find_element(SmartSelector.CREATE_SCENE_NAME).send_keys(scene_name)
        self.hide_keyboard()
        self.click_next()

    def select_device(self, device_list):
        for device_name in device_list:
            device_ele = Tools.re_ele(SmartSelector.SCENE_SELECT_DEVICE, device_name)
            self.find_element(device_ele).click()
        self.click_next()

    def scene_created(self):
        self.assert_ele(SmartSelector.SCENE_SETTINGS, '进入scene setting页面')
        if Set.client == 'android':
            if self.find_element(SmartSelector.LIGHT_SPRAY, model='assert') and self.find_element(
                    SmartSelector.SCENE_MODIFY, model='assert'):
                self.find_element(SmartSelector.LIGHT_SPRAY).click()
        self.find_element(SmartSelector.SCENE_DONE).click()

    def scene_detail(self, scene_name):
        scene_ele = Tools.re_ele(SmartSelector.SCENE_DETAIL, scene_name)
        self.find_element(scene_ele, 60).click()
        self.assert_ele(SmartSelector.SCENE_SETTINGS, '进入scene setting页面')

    def run_scene(self, scene_name):
        run_scene = Tools.re_ele(SmartSelector.RUN_SCENE, scene_name)
        time.sleep(10)
        self.find_element(run_scene).click()

    def delete_scene(self, scene_name):
        self.slip('slow_up')
        time.sleep(5)
        self.scene_detail(scene_name)
        self.find_element(SmartSelector.DELETE_SCENE).click()
        self.find_element(SmartSelector.CONFIRM_DELETE_SCENE).click()
        self.assert_ele(SmartSelector.SCENE_TAB, '回到smart页面')
        self.slip('slow_up')
        time.sleep(10)
        scene_ele = Tools.re_ele(SmartSelector.SCENE_DETAIL, scene_name)
        if self.find_element(scene_ele, timeout=15, model='assert') is None:
            Tools.step_log(f'✅成功删除scene:{scene_name}')
            assert True
        else:
            Tools.step_log(f'❎未成功删除scene:{scene_name}')

    @allure.step('删除所有场景')
    def delete_all_scene(self):
        while self.find_element(SmartSelector.DELETE_ALL_SCENE, timeout=15, model='assert') is not None:
            self.find_element(SmartSelector.DELETE_ALL_SCENE).click()
            self.find_element(SmartSelector.DELETE_SCENE).click()
            self.find_element(SmartSelector.CONFIRM_DELETE_SCENE).click()
            self.assert_ele(SmartSelector.SCENE_TAB, '回到smart页面')
        Tools.step_log('✅已删除所有scene')

    @allure.step('删除所有routine')
    def delete_all_routine(self):
        while self.find_element(SmartSelector.DELETE_ALL_ROUTINE, timeout=15, model='assert') is not None:
            self.find_element(SmartSelector.DELETE_ALL_ROUTINE).click()
            self.find_element(SmartSelector.DELETE_ROUTINE).click()
            self.find_element(SmartSelector.CONFIRM_DELETE).click()
            self.assert_ele(SmartSelector.ROUTINE_TAB, '回到smart页面')
        Tools.step_log('✅已删除所有routine')
