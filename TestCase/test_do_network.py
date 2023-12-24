from Common.Flow import Flow
from Common.Tools import Tools
import pytest
from PageEle.page.HomePage import HomePage
from PageEle.page.DeviceSelectPage import DeviceSelectPage
from PageEle.page.Navi_Bar import NaviBar
from PageEle.page.DeviceDnPage import DevicePage
from Common.data_deal import DataDeal
import allure


@allure.story('设备配网')
@pytest.mark.run(order=-1)
@pytest.mark.parametrize("test_data", DataDeal.get_test_data("test_do_network_normal"))
def test_do_network_normal(test_data):
    Tools.start_deal(test_data["title"], test_data)
    """登录并进入home模块"""
    Flow.login(test_data["user"], test_data["pwd"])
    """移除设备"""
    Flow.remove_devices(test_data['uuid'],test_data['device_nickname'])
    """搜索设备准备开始配网"""
    Flow.device_dn_ahead(test_data["device_name"], test_data["device_cate"])
    """开始配网流程"""
    Flow.get_dn_flow(test_data["device_name"])
    Flow.device_dn_later(test_data)
    page = DevicePage()
    page.wifi_bind(device_version=test_data['device_version'], device_nickname=test_data['device_nickname'],
                   device_cate=test_data['device_cate'])


@allure.story('设备配网')
@pytest.mark.run(order=-2)
@pytest.mark.parametrize("test_data", DataDeal.get_test_data("test_do_network_exception"))
def test_do_network_exception(test_data):
    Tools.start_deal(test_data["title"], test_data)
    """登录并进入home模块"""
    Flow.login(test_data["user"], test_data["pwd"])
    """移除设备"""
    Flow.remove_devices(test_data['uuid'], test_data['device_nickname'])
    """搜索设备准备开始配网"""
    Flow.device_dn_ahead(test_data["device_name"], test_data["device_cate"])
    """开始配网流程"""
    Flow.get_dn_flow(test_data["device_name"])
    Flow.device_dn_later(test_data)
    page = DevicePage()
    page.wifi_bind(test_data["bind_model"])
