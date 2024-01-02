# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 10:59
# @Author  : XuLei
# @FileName: test_control.py
# @Software: PyCharm
import _thread
import random
import string
import time

from Common.Flow import Flow
from Common.Tools import Tools
import pytest
from openpyxl import Workbook
from Common.mqtt_check import app_check
from Common.set import Set
from PageEle.page.HomePage import HomePage
from PageEle.page.DeviceSelectPage import DeviceSelectPage
from PageEle.page.Navi_Bar import NaviBar
from PageEle.page.DeviceDnPage import DevicePage
from Common.data_deal import DataDeal
import allure


@allure.story('设备控制')
@pytest.mark.run(order=1)
#@pytest.mark.parametrize("test_data", DataDeal.get_test_data("test_mss425e_control"))
def test_mss425e_control():

    page = NaviBar()
    page = HomePage()
    page.click_search();
    page.yigedahua();
    workbook = Workbook()
    sheet = workbook.active

    sheet['A1'] = '序号'
    sheet['B1'] = '产品名称'
    sheet['C1'] = '页面显示价格'
    sheet['D1'] = '到手价'
    sheet['E1'] = '销量'
    sheet['F1'] = '发货地区'
    sheet['G1'] = '店铺名称'
    sheet['H1'] = '店铺小红书号'
    sheet['I1'] = '卖家口碑分'
    sheet['J1'] = '图片'
    sheet['K1'] = '商品链接'
    sheet['L1'] = '店铺链接'

    ran = ''.join(random.sample(string.ascii_letters + string.digits, 5))
    excel_path = f'demo{ran}.xlsx'

    page.continuetodo()
    for i in range(1,76):
        Tools.step_log(f"当前是第{i}条")
        data=[None]*12
        data[0]=i
        try:
            page.collect_info(sheet, data, i)
            # 每执行一条记录后保存到 Excel 表格
            workbook.save(excel_path)
        except Exception as e:
            print(f"记录第{i}条数据时出错: {str(e)}")

    try:
        workbook.save(excel_path)
        print(f"Excel 文件保存成功: {excel_path}")
    except Exception as e:
        print(f"保存 Excel 文件时出错: {str(e)}")
  
    # Tools.start_deal(test_data["title"], test_data)
    # Flow.login(test_data["user"], test_data["pwd"])
    # device_nickname=test_data["device_nickname"]
    
    # page.device_detail(device_nickname)
    # page.protector_control(test_data["sub_switch_on"],test_data['uuid'])
    # # Tools.step_log("单个排插开关已开启")
    # page.protector_control(test_data["master_switch_off"],test_data['uuid'],device_nickname)
    # Tools.step_log("排插总开关已关闭")
    # page.protector_control(test_data["master_switch_on"],test_data['uuid'],device_nickname)
    # Tools.step_log("排插总开关已开启")
    # page.protector_control(test_data["sub_switch_off"],test_data['uuid'])
    # # Tools.step_log("单个排插开关已关闭")
    # assert Set.check_result


@allure.story('设备控制')
@pytest.mark.run(order=2)
@pytest.mark.parametrize("test_data", DataDeal.get_test_data("test_mss110_control"))
def test_mss310_control(test_data):
    Tools.start_deal(test_data["title"], test_data)
    Flow.login(test_data["user"], test_data["pwd"])
    page = NaviBar()
    page.go_home_module()
    page = HomePage()
    page.plug_control(test_data['device_nickname'],test_data['on_rule'],test_data['uuid'])
    Tools.step_log("开关已打开")
    page.plug_control(test_data['device_nickname'], test_data['off_rule'],test_data['uuid'])
    Tools.step_log("开关已关闭")
    assert Set.check_result


@allure.story('设备控制')
@pytest.mark.run(order=3)
@pytest.mark.parametrize("test_data", DataDeal.get_test_data("test_map100_control"))
def test_map100_control(test_data):
    Tools.start_deal(test_data["title"], test_data)
    Flow.login(test_data["user"], test_data["pwd"])
    import threading
    t1 = threading.Thread(target=app_check,daemon=True)
    t1.start()
    page = NaviBar()
    page.go_home_module()
    page = HomePage()
    page.device_detail(test_data['device_nickname'])
    # page.air_speed_middle(test_data['speed_mid_mode'],test_data['uuid'])
    # assert Set.check_result
    page.map100_control(test_data['rule'],test_data['uuid'])
    from TestCase.conftest import stop_thread
    stop_thread(t1)
    assert Set.check_result


# @allure.story('设备控制')
# @pytest.mark.run(order=4)
# @pytest.mark.parametrize("test_data", DataDeal.get_test_data("test_msg100_control"))
# def test_msg100_control(test_data):
#     Tools.start_deal(test_data["title"], test_data)
#     Flow.login(test_data["user"], test_data["pwd"])
#     page = NaviBar()
#     page.go_home_module()
#     page = HomePage()
#     model = page.get_door_status()
#     page.garage_door_control(test_data["device_nickname"], model)
#     model = page.get_door_status()
#     page.garage_door_control(test_data["device_nickname"], model)
#     assert Set.check_result

@allure.story('设备控制')
@pytest.mark.run(order=4)
@pytest.mark.parametrize("test_data", DataDeal.get_test_data("test_mss120_control"))
def test_mss120_control(test_data):
    Tools.start_deal(test_data["title"], test_data)
    Flow.login(test_data["user"], test_data["pwd"])
    page = NaviBar()
    page.go_home_module()
    page = HomePage()
    page.switch_control(test_data["switch_on"],test_data['uuid'],test_data['device_nickname'])
    Tools.step_log("插座双开关已开启")
    page.switch_control(test_data["switch_off"],test_data['uuid'],test_data['device_nickname'])
    Tools.step_log("插座双开关已关闭")
    assert Set.check_result


@allure.story('设备控制')
@pytest.mark.run(order=5)
@pytest.mark.parametrize("test_data", DataDeal.get_test_data("test_mdl110_control"))
def test_mdl110_control(test_data):
    Tools.start_deal(test_data["title"], test_data)
    Flow.login(test_data["user"], test_data["pwd"])
    device_nickname=test_data["device_nickname"]
    page = NaviBar()
    page.go_home_module()
    page = HomePage()
    page.device_detail(device_nickname)
    page.light_master_control(test_data["on_rule"],test_data['uuid'])
    Tools.step_log("总开关已开启")
    page.light_master_control(test_data["off_rule"],test_data['uuid'])
    Tools.step_log("总开关已关闭")
    assert Set.check_result

@allure.story('设备控制')
@pytest.mark.run(order=6)
@pytest.mark.parametrize("test_data", DataDeal.get_test_data("test_msl320_control"))
def test_msl320_control(test_data):
    Tools.start_deal(test_data["title"], test_data)
    Flow.login(test_data["user"], test_data["pwd"])
    device_nickname=test_data["device_nickname"]
    page = NaviBar()
    page.go_home_module()
    page = HomePage()
    page.device_detail(device_nickname)
    page.light_master_control(test_data["on_rule"],test_data['uuid'])
    Tools.step_log("开启总开关")
    page.go_effects()
    Tools.step_log("切换到effects页面")
    page.go_color()
    Tools.step_log("切换到color页面")
    page.light_master_control(test_data["off_rule"],test_data['uuid'])
    Tools.step_log("关闭总开关")
    assert Set.check_result

@allure.story('设备控制')
@pytest.mark.run(order=7)
@pytest.mark.parametrize("test_data", DataDeal.get_test_data("test_msl420_control"))
def test_msl420_control(test_data):
    Tools.start_deal(test_data["title"], test_data)
    Flow.login(test_data["user"], test_data["pwd"])
    device_nickname=test_data["device_nickname"]
    page = NaviBar()
    page.go_home_module()
    page = HomePage()
    page.device_detail(device_nickname)
    page.light_master_control(test_data["on_rule"],test_data['uuid'])
    Tools.step_log("开启总开关")
    page.go_color()
    Tools.step_log("切换到color页面")
    page.go_white()
    Tools.step_log("切换到white页面")
    page.light_master_control(test_data["off_rule"],test_data['uuid'])
    Tools.step_log("关闭总开关")
    assert Set.check_result

@allure.story('设备控制')
@pytest.mark.run(order=8)
@pytest.mark.parametrize("test_data", DataDeal.get_test_data("test_msl210_control"))
def test_msl210_control(test_data):
    Tools.start_deal(test_data["title"], test_data)
    Flow.login(test_data["user"], test_data["pwd"])
    device_nickname=test_data["device_nickname"]
    page = NaviBar()
    page.go_home_module()
    page = HomePage()
    page.device_detail(device_nickname)
    page.light_master_control(test_data["on_rule"], test_data['uuid'])
    Tools.step_log("开启总开关")
    page.full_light_on()
    Tools.step_log("进入全灯模式")
    page.full_light_off()
    Tools.step_log("退出全灯模式")
    page.night_light_on()
    Tools.step_log("进入夜灯模式")
    page.night_light_off()
    Tools.step_log("退出夜灯模式")
    page.light_favorite()
    Tools.step_log("点击favorite")
    page.light_master_control(test_data["off_rule"], test_data['uuid'])
    Tools.step_log("关闭总开关")
    assert Set.check_result