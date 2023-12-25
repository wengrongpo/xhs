# -*- coding: utf-8 -*-
# @Time    : 2022/6/23 13:38
# @Author  : XuLei
# @FileName: HomePage.py
# @Software: PyCharm
import re
import time
import allure
from openpyxl.drawing.image import Image
from Common.Tools import Tools
from PageEle.BasePage import Page
from PageEle.selector.HomeSelector import *
from PageEle.selector.DeviceSelect import *

class HomePage(Page):
    @allure.step("+ 进入添加设备页面")
    def plus_device(self):
        self.find_element(HomeSelector.PLUS_BN).click()
        if self.find_element(DeviceSelector.ENABLE_BLUETOOTH, 10, 'assert'):
            self.find_element(DeviceSelector.ENABLE_BLUETOOTH_OK).click()
        self.assert_ele(DeviceSelector.SEARCH, "+ 进入添加设备页面")

    def device_detail(self, device_name):
        device_name = Tools.re_ele(HomeSelector.DEVICE_NAME, device_name)
        self.find_element(device_name).click()
        time.sleep(3)
        Tools.step_log('进入设备详情')

    def device_more(self):
        Tools.step_log("进入设备更多属性")
        if self.find_element(HomeSelector.DEVICE_DETAIL, model="assert", timeout=5):
            self.find_element(HomeSelector.DEVICE_DETAIL).click()

    def remove_device(self, device_name):
        self.device_more()
        self.assert_ele(HomeSelector.DEVICE_SETTING, "进入设备详情")
        self.slip_find_click(HomeSelector.REMOVE_DEVICE)
        self.find_element(HomeSelector.CONFIRM_REMOVE).click()
        Tools.step_log(f"已移除设备{device_name}", model="info")

    def select_device(self, device_name):
        device_name = HomeSelector.DEVICE_NAME.replace("$replace", device_name)
        Tools.sleep(10,'等待首页刷新')
        if self.find_element(device_name, model='assert', timeout=20):
            self.slip_find_click(device_name)
            Tools.step_log(f"选择设备，进入详情")
            return True
        elif self.slip_find(device_name):
            if self.find_element(device_name, model='assert', timeout=20):
                self.slip_find_click(device_name)
            return True
        else:
            Tools.step_log("未找到相应设备解绑，直接尝试配网")
            return False

    def control_device(self, device_cate, action=None):
        if device_cate == 'Smart Surge Protector':
            self.protector_control(action)
        elif device_cate == 'Smart Plug':
            self.plug_control(action)
        else:
            logger.warning(f'暂不支持该设备类型:{device_cate}')
        time.sleep(1)

    def notif(self, model):
        if Set.client == "android":
            self.slip('notif-open')
        if model == 'open':
            self.assert_ele(HomeSelector.GARAGE_DOOR_CLOSED, '车库门打开', 40)
        elif model == 'close':
            self.assert_ele(HomeSelector.GARAGE_DOOR_OPENED, '车库门打开', 40)
        if Set.client == "android":
            self.find_element(HomeSelector.CLEAR_NOTIF).click()

    def garage_door_control(self, name, model):
        Tools.step_log('控制车库门')
        garage_door = Tools.re_ele(HomeSelector.GARAGE_DOOR, name)
        self.find_element(garage_door).click()
        self.notif(model)

    def get_door_status(self):
        Tools.step_log('获取车库门状态')
        if Set.client == 'ios':
            if self.find_element(HomeSelector.GARAGE_DOOR_OPEN_STATUS, 10, model='assert'):
                return 'open'
            elif self.find_element(HomeSelector.GARAGE_DOOR_CLOSED_STATUS, 10, model='assert'):
                return 'close'
            else:
                logger.error('error')
        elif Set.client == 'android':
            if self.find_element(HomeSelector.GARAGE_DOOR_OPEN_DOT, model='assert'):
                return 'open'
            else:
                return 'close'

    def protector_control(self, action, uuid,device_nickname=None,):
        if type(action) is dict:
            for switch, rule in action.items():
                switch_btn = Tools.re_ele(HomeSelector.PROTECTOR_SWITCH, switch)
                self.find_element(switch_btn).click()
                Tools.uuid_rule_deal({'uuid': uuid, 'rule': rule}, msg=f'校验：开关{switch}正确')
                time.sleep(10)
                Tools.step_log(f'已点击排插按钮{switch}')
        elif type(action) is str:
            switch_btn = Tools.re_ele(HomeSelector.MASTER_PROTECTOR_SWITCH, device_nickname)
            self.find_element(switch_btn).click()
            Tools.uuid_rule_deal({'uuid': uuid, 'rule': action}, msg=f'校验：开关总开关正确')
            # Tools.step_log(f'已点击排插总开关{action}')
            time.sleep(15)

        else:
            Tools.step_log('暂不支持', "error")

    def plug_control(self, device_name, rule,uuid):
        plug_switch = Tools.re_ele(HomeSelector.DEVICE_SWITCH, device_name)
        self.find_element(plug_switch).click()
        Tools.step_log("home页找设备")
        Tools.uuid_rule_deal({'uuid': uuid, 'rule': rule}, msg='校验：开关插座')
        time.sleep(30)

    def switch_control(self, action, uuid,device_nickname=None):
        switch_btn_one = Tools.re_ele(HomeSelector.HOME_SWITCH_ONE, device_nickname)
        self.find_element(switch_btn_one).click()
        switch_btn_two = Tools.re_ele(HomeSelector.HOME_SWITCH_TWO, device_nickname)
        self.find_element(switch_btn_two).click()
        for switch, rule in action.items():
            Tools.uuid_rule_deal({'uuid': uuid, 'rule': rule}, msg=f'校验：开关{switch}正确')
            time.sleep(15)

    def light_master_control(self, rule, uuid):
        self.find_element(HomeSelector.LIGHT_MASTER_ONOFF).click()
        Tools.uuid_rule_deal({'uuid': uuid, 'rule': rule}, msg='校验：总开关')
        time.sleep(15)

    def go_effects(self):
        self.find_element(HomeSelector.LIGHT_TYPE_EFFECTS).click()
        self.assert_ele(HomeSelector.EFFECTS_CONTENT, "切换到effects页")
        time.sleep(3)

    def go_color(self):
        self.find_element(HomeSelector.LIGHT_TYPE_COLOR).click()
        self.assert_ele(HomeSelector.COLOR_SELECTOR, "切换到color页")
        time.sleep(3)

    def go_white(self):
        self.find_element(HomeSelector.LIGHT_TYPE_WHITE).click()
        self.assert_ele(HomeSelector.WHITE_SELECTOR, "切换到white页")
        time.sleep(3)

    def full_light_on(self):
        self.find_element(HomeSelector.FULL_LIGHT_ON).click()
        self.assert_ele(HomeSelector.LIGHT_EXIT, "进入全灯模式")
        time.sleep(3)

    def full_light_off(self):
        self.find_element(HomeSelector.LIGHT_EXIT).click()
        self.assert_ele(HomeSelector.FULL_LIGHT_ON, "退出全灯模式")
        time.sleep(3)

    def night_light_on(self):
        self.find_element(HomeSelector.NIGHT_LIGHT_ON).click()
        self.assert_ele(HomeSelector.LIGHT_EXIT, "进入夜灯模式")
        time.sleep(3)

    def night_light_off(self):
        self.find_element(HomeSelector.LIGHT_EXIT).click()
        self.assert_ele(HomeSelector.NIGHT_LIGHT_ON, "退出夜灯模式")
        time.sleep(3)

    def light_favorite(self):
        self.find_element(HomeSelector.LIGHT_FAVORITE).click()
        time.sleep(3)

    @allure.step('更改设备名称')
    def change_device_name(self, name):
        self.assert_ele(HomeSelector.DEVICE_SETTING, '进入设备设置页面')
        self.find_element(HomeSelector.DEVICE_DETAIL_NAME).click()
        self.find_element(HomeSelector.CHANGE_NAME).clear()
        self.find_element(HomeSelector.CHANGE_NAME).send_keys(name)
        self.find_element(HomeSelector.SAVE_NAME).click()
        self.find_element(HomeSelector.RETURN_BT).click()
        if self.find_element(HomeSelector.HOME_TITLE, model='assert') is False:
            if self.find_element(HomeSelector.RETURN_BT, 5, model='assert'):
                self.find_element(HomeSelector.RETURN_BT).click()
            elif self.find_element(HomeSelector.CLOSE_BT, 5, model='assert'):
                self.find_element(HomeSelector.CLOSE_BT).click()
        Tools.step_log(f'成功修改设备名称为{name}')

    def overtime_reminder(self):
        Tools.step_log('设置超时提醒时间')
        self.slip_find_click(HomeSelector.OVERTIME_REMINDER)
        overtime_reminder_time = Tools.re_ele(HomeSelector.OVERTIME_REMINDER_TIME, '10 min')
        self.find_element(overtime_reminder_time).click()
        self.find_element(HomeSelector.SAVE_OVERTIME_REMINDER).click()
        time.sleep(5)
        self.find_element(HomeSelector.RETURN_BT).click()

    def overtime_warning(self):
        logger.info('等待完毕，查看超时警告')
        self.assert_ele(HomeSelector.OVERTIME_WARNING, '超时警告', 300)

    # def air_speed_middle(self, rule,uuid):
    #     self.find_element(HomeSelector.AIR_SPEED).click()
    #     self.find_element(HomeSelector.AIR_MID_SPEED).click()
    #     Tools.uuid_rule_deal({'uuid': uuid, 'rule': rule}, msg='校验：风速')
    #     time.sleep(5)
    #     Tools.step_log('风速已切换')

    def map100_control(self, rule,uuid):
        Tools.set_uuid_rule(rule['speed_middle_mode'],uuid,check_msg='校验：空净风速切换为中')
        self.find_element(HomeSelector.AIR_SPEED).click()
        self.find_element(HomeSelector.AIR_MID_SPEED).click()
        time.sleep(5)
        Tools.step_log('风速已切换')
        Tools.set_uuid_rule(rule['sleep_model'],uuid,check_msg=' 校验：空净进入睡眠模式')
        self.find_element(HomeSelector.AIR_SLEEP_MODEL).click()
        time.sleep(5)
        Tools.step_log('已进入睡眠模式')
        Tools.set_uuid_rule(rule['child_lock_on'],uuid,check_msg='校验：打开童锁')
        self.find_element(HomeSelector.AIR_CHILD_LOCK).click()
        time.sleep(5)
        Tools.step_log('已打开童锁')
        Tools.set_uuid_rule(rule['child_lock_off'],uuid,check_msg='校验：关闭童锁')
        self.find_element(HomeSelector.AIR_CHILD_LOCK).click()
        time.sleep(5)
        Tools.step_log('已关闭童锁')
        Tools.set_uuid_rule(rule['master_switch_off'],uuid,check_msg='校验：关闭空净开关')
        self.find_element(HomeSelector.AIR_ON_OFF).click()
        time.sleep(5)
        Tools.step_log('已关闭开关')
        Tools.set_uuid_rule(rule['master_switch_on'],uuid,check_msg='校验：打开空净开关')
        self.find_element(HomeSelector.AIR_ON_OFF).click()
        time.sleep(5)
        Tools.step_log('已打开开关')
        time.sleep(10)
        self.find_element(HomeSelector.AIR_ON_OFF).click()

    def get_air_status(self):
        if self.find_element(HomeSelector.AIR_STATUS_OFF, model='assert', timeout=7):
            return 'off'
        elif self.find_element(HomeSelector.AIR_STATUS_ON, model='assert', timeout=7):
            return 'on'
        else:
            logger.warning('warn')

    def click_search(self):
        self.find_element(HomeSelector.SEARCH).click();
        self.find_element(HomeSelector.TEXT_BOX).send_keys("娇韵诗");
        self.find_element(HomeSelector.SEARCH_AGAIN).click();
        self.find_element(HomeSelector.PRODUCT).click();
        time.sleep(5)
        self.find_element(HomeSelector.WAYS).click();
        
    def yigedahua(self):
        time.sleep(5)
        self.slip('xhs_slow_down')

    def collect_info(self,sheet,data,i):
        time.sleep(5)
        self.tap(675,240)
        #进入商品详情页
        #获取原价
        # original_price_1 = self.find_element(HomeSelector.ORINGINAL_PRICE_1)
        # if original_price_1.text.isdigit():
        #     original_price=original_price_1.text
        # else:
        #     original_price = self.find_element(HomeSelector.ORINGINAL_PRICE).text
        # Tools.step_log(f'原价是{original_price}')  
        # data[2]=original_price  
        #获取原价、获取到手价
        text_views =self.get_elem("by.classes_name","android.widget.TextView")
        originalFlag=False
        currentFlag=False
        count=0
        sum=0
        for text_view in text_views:
            #获取原价
            if originalFlag :
                Tools.step_log(f'原价是{text_view.text}')
                data[2]=text_view.text
                originalFlag=False
            #获取到手价    
            if currentFlag :
                Tools.step_log(f'到手价是{text_view.text}')
                data[3]=text_view.text
                break;
            #获取到手价
            if text_view.text=="¥" and count==1:
                currentFlag=True 
            #获取原价
            if text_view.text=="¥" and count==0:
                originalFlag=True
                count+=1
            
            sum+=1
            if sum==15:break
        if currentFlag==False:
            Tools.step_log('无到手价')
            data[3]='无到手价'
            
        
        #获取到手价
        # nowdays_price_1 = self.find_element(HomeSelector.NOWDAYS_PRICE_1)  
        # nowdays_price = self.find_element(HomeSelector.NOWDAYS_PRICE)  
        # nowdays_price_1plus1 = self.find_element(HomeSelector.NOWDAYS_PRICE_1plus1)  
        # nowdays_price_plus1 = self.find_element(HomeSelector.NOWDAYS_PRICE_plus1)  
        # decimal_point = self.find_element(HomeSelector.DECIMAL_PONIT)
        # decimal_point_1 = self.find_element(HomeSelector.DECIMAL_PONIT_1)
        # if nowdays_price_1.text.isdigit():
        #     nowdays_price=nowdays_price_1.text
        #     Tools.step_log(f'到手价是{nowdays_price}')
        #     data[3]=nowdays_price
        # elif nowdays_price.text.isdigit(): 
        #     Tools.step_log(f'到手价是{nowdays_price.text}')  
        #     data[3]=nowdays_price.text
        # elif "." in decimal_point_1.text:
        #     Tools.step_log(f'到手价是{nowdays_price_1plus1.text}') 
        #     data[3]=nowdays_price_1plus1.text
        # elif "." in decimal_point.text  :
        #     Tools.step_log(f'到手价是{nowdays_price_plus1.text}')         
        #     data[3]=nowdays_price_plus1.text
        # else:
        #     Tools.step_log(f'无到手价')  
        #     data[3]='无到手价'
        #获取商品名
        name =self.find_element(HomeSelector.NAME).text
        Tools.step_log(f'商品名是{name}')
        data[1]=name
        #获取图片
        self.tap(650,435)
        path=self.shot()
        img= Image(path)
        location=f'J{i+1}'
        img.anchor=location
        img.width=60
        img.height=20
        sheet.add_image(img)
        self.back()
        #获取商品链接
        self.get_elem("by.id","com.xingin.xhs:id/cll").click()
        self.swip()
        shop_url=self.get_elem("by.xpath",'//android.widget.Button[@content-desc="复制链接"]/android.view.ViewGroup/android.widget.ImageView[1]')
        shop_url.click()
        url=self.clipboard_content()
        Tools.step_log(f'商品链接是{url}')
        data[10]=url
        
        entry=self.find_element(HomeSelector.ENTRY)
        self.slip("xhs_slow_down_1")
        text_views =self.get_elem("by.classes_name","android.widget.TextView")
        locationFlag=False
        ratingFlag=False
        for text_view in text_views:
            #获取发货地
            if locationFlag :
                Tools.step_log(f'发货地是{text_view.text}')
                data[5]=text_view.text
                locationFlag=False
            #获取卖家口碑    
            if ratingFlag :
                Tools.step_log(f'评分是{text_view.text}')
                data[8]=text_view.text
                break;
            #获取销量
            if text_view.text.find("已售")!=-1:
                quantity=text_view.text
                matches =re.findall(r'\d+',quantity)
                number = matches[0]
                Tools.step_log(f'销量是{number}')
                data[4]=number
            #获取发货地
            if text_view.text=="发货":
                locationFlag=True
            #获取评分
            if text_view.text=="卖家口碑":
                ratingFlag=True 
        entry.click()
        shop_name=self.find_element(HomeSelector.SHOP_NAME)
        Tools.step_log(f'店铺名是{shop_name.text}')
        data[6]=shop_name.text
        number=self.find_element(HomeSelector.NUMBER)
        xhsh=number.text
        matches =re.findall(r'\d+',xhsh)
        Tools.step_log(f'小红书号是{matches[0]}')
        data[7]=matches[0]
        #获取店铺链接
        self.get_elem("by.id","com.xingin.xhs:id/gg4").click()
        shop_url=self.get_elem("by.xpath",'//android.widget.Button[@content-desc="复制链接"]/android.view.ViewGroup/android.widget.ImageView[1]')
        shop_url.click()
        url=self.clipboard_content()
        Tools.step_log(f'店铺链接是{url}')
        data[11]=url

        sheet.append(data)
        self.back()
        self.back()
        time.sleep(1)
        self.slip('xhs_slow_down')
    
                
