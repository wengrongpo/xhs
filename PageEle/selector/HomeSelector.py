# -*- coding: utf-8 -*-
# @Time    : 2022/6/23 15:51
# @Author  : XuLei
# @FileName: HomeSelector.py
# @Software: PyCharm
from Common.set import Set
from Common.log import logger


class HomeSelector:
    if Set.client == "android":
        PLUS_BN=f"by.id|{Set.Apk}:id/iv_right"  #+进入添加设备页面
        HOME_MODEL = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/navigation_title') and contains(@text, 'Home')]"  #底部导航栏Home模块
        HOME_TITLE = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Home')]"  # HOME的title
        DEVICE_NAME=f"""by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, "$replace")]"""
        # 设备详情
        DEVICE_DETAIL=f'by.id|{Set.Apk}:id/icons_fake'
        DEVICE_SETTING=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Device Settings')]"
        REMOVE_DEVICE="by.xpath|//*[contains(@text, 'Remove device')]"
        CONFIRM_REMOVE=f"by.xpath|//*[contains(@resource-id,'android:id/button1') and contains(@text, 'Delete')]"
        DEVICE_DETAIL_NAME=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Device name')]"
        CHANGE_NAME=f'by.id|{Set.Apk}:id/et_name'
        SAVE_NAME=f'by.id|{Set.Apk}:id/bt_next'
        RETURN_BT=f'by.id|{Set.Apk}:id/iv_left_gone'
        CLOSE_BT=f'by.id|{Set.Apk}:id/iv_left_gone'
        """排插开关"""
        PROTECTOR_SWITCH = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')]/../preceding-sibling::android.widget.ImageView"
        MASTER_PROTECTOR_SWITCH=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')]/../preceding-sibling::android.widget.ImageView"
        """插座开关"""
        DEVICE_SWITCH= f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')]/preceding-sibling::android.view.ViewGroup/child::android.widget.ImageView"
        """车库门开关"""
        GARAGE_DOOR=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')]/preceding-sibling::*[@resource-id='{Set.Apk}:id/iv_head']"
        GARAGE_DOOR_OPENED=f"by.xpath|//*[contains(@text, 'Garage Door has been opened!')]"
        GARAGE_DOOR_CLOSED=f"by.xpath|//*[contains(@text, 'Garage Door has been closed!')]"
        CLEAR_NOTIF='by.id|com.android.systemui:id/clear_all'
        GARAGE_DOOR_OPEN_DOT=f'by.id|{Set.Apk}:id/garage_door_open_dot'
        OVERTIME_REMINDER=f"by.id|{Set.Apk}:id/rl_ot_remind"
        OVERTIME_WARNING = "by.xpath|//*[contains(@text,'Overtime Warning')"
        OVERTIME_REMINDER_TIME =f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_time') and contains(@text, '$replace')]"
        SAVE_OVERTIME_REMINDER =f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_right') and contains(@text, 'Save')]"
        """空净控制"""
        AIR_ON_OFF = f'by.id|{Set.Apk}:id/iv_on_off'
        AIR_SPEED = f'by.id|{Set.Apk}:id/iv_speed'
        AIR_HIGH_SPEED = f'by.id|{Set.Apk}:id/iv_high'
        AIR_MID_SPEED = f'by.id|{Set.Apk}:id/iv_middle'
        AIR_LOW_SPEED = f'by.id|{Set.Apk}:id/iv_low'
        AIR_SLEEP_MODEL = f'by.id|{Set.Apk}:id/iv_sleep'
        AIR_CHILD_LOCK = f'by.id|{Set.Apk}:id/iv_lock'
        AIR_STATUS_ON="by.xpath|//*[contains(@text,'On')]"
        AIR_STATUS_OFF="by.xpath|//*[contains(@text,'Off')]"
        """home双开关"""
        HOME_SWITCH_ONE = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')]/following-sibling::android.view.ViewGroup/child::android.widget.ImageView"
        HOME_SWITCH_TWO = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')]/following-sibling::android.view.ViewGroup[2]/child::android.widget.ImageView"
        """light控制"""
        LIGHT_MASTER_ONOFF = f"by.id|{Set.Apk}:id/bottom_light_iv"
        LIGHT_TYPE_EFFECTS = f"by.id|{Set.Apk}:id/type_effect_rb"
        EFFECTS_CONTENT = f"by.id|{Set.Apk}:id/effect_title_tv"
        LIGHT_TYPE_COLOR = f"by.id|{Set.Apk}:id/type_color_rb"
        COLOR_SELECTOR = f"by.id|{Set.Apk}:id/color_selector"
        LIGHT_TYPE_WHITE = f"by.id|{Set.Apk}:id/type_white_rb"
        WHITE_SELECTOR = f"by.id|{Set.Apk}:id/white_selector"
        FULL_LIGHT_ON = f"by.id|{Set.Apk}:id/lyt_all_light"
        LIGHT_EXIT = f"by.id|{Set.Apk}:id/cs_night_exit"
        NIGHT_LIGHT_ON = f"by.id|{Set.Apk}:id/lyt_night_light"
        LIGHT_FAVORITE = f"by.id|{Set.Apk}:id/lyt_favourite"
        #xhs
        SEARCH= f'by.accessibility_id|搜索'
        TEXT_BOX= f'by.class_name|android.widget.EditText'
        PRODUCT= f'by.xpath|(//androidx.appcompat.app.ActionBar.Tab)[3]'
        WAYS= f'by.id|com.xingin.xhs:id/ewl'
        NAME= f'by.id|com.xingin.xhs:id/ci_'
        SHOP_NAME= f'by.id|com.xingin.xhs:id/gh0'
        ENTRY= f'by.id|com.xingin.xhs:id/clj'
        NUMBER= f'by.id|com.xingin.xhs:id/gh2'
        SEARCH_AGAIN= f'by.id|com.xingin.xhs:id/ewz'
        #原价、小数点、到手价
        ORINGINAL_PRICE_1 = f'by.xpath|(//android.widget.TextView)[3]'
        DECIMAL_PONIT_1 = f'by.xpath|(//android.widget.TextView)[4]'
        NOWDAYS_PRICE_1 = f'by.xpath|(//android.widget.TextView)[6]'
        NOWDAYS_PRICE_1plus1 = f'by.xpath|(//android.widget.TextView)[7]'

        ORINGINAL_PRICE = f'by.xpath|(//android.widget.TextView)[5]'
        DECIMAL_PONIT = f'by.xpath|(//android.widget.TextView)[6]'       
        NOWDAYS_PRICE = f'by.xpath|(//android.widget.TextView)[8]'
        NOWDAYS_PRICE_plus1 = f'by.xpath|(//android.widget.TextView)[9]'

        TEXT_VIEW =f'by.classes_name|android.widget.TextView'
    elif Set.client == "ios":
        PLUS_BN = 'by.ios_class_chain|**/XCUIElementTypeNavigationBar[`name == "Home"`]/XCUIElementTypeButton'  # +进入添加设备页面
        HOME_MODEL = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "Home"`]'   # 底部导航栏Home模块
        HOME_TITLE = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Home"`]'
        DEVICE_NAME='by.ios_predicate|label == "$replace" and type=="XCUIElementTypeStaticText"'
        # 设备详情
        DEVICE_DETAIL = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "menu"`]'
        DEVICE_DETAIL_NAME='by.ios_predicate|label == "Device name"'
        CHANGE_NAME='by.ios_class_chain|**/XCUIElementTypeTextField[1]'
        SAVE_NAME='by.ios_predicate|label == "Save"'
        RETURN_BT='by.ios_class_chain|**/XCUIElementTypeButton[`label == "return"`]'
        CLOSE_BT='by.ios_predicate|label == "close"'
        DEVICE_SETTING='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Device Settings"`]'
        REMOVE_DEVICE='by.ios_predicate|name="Remove device"'
        CONFIRM_REMOVE = "by.ios_predicate|label == 'Delete' and type='XCUIElementTypeButton'"
        """排插开关"""
        PROTECTOR_SWITCH = "by.xpath|//XCUIElementTypeStaticText[@name='$replace']/preceding-sibling::XCUIElementTypeButton"
        MASTER_PROTECTOR_SWITCH="by.xpath|(//XCUIElementTypeStaticText[@name='$replace']/preceding-sibling::XCUIElementTypeButton)[2]"
        """一般开关"""
        DEVICE_SWITCH = 'by.xpath|//XCUIElementTypeButton[@name="$replace"]/preceding-sibling::XCUIElementTypeOther/child::XCUIElementTypeButton'
        """车库门开关"""
        GARAGE_DOOR='by.xpath|//XCUIElementTypeButton[@name="$replace"]/preceding-sibling::XCUIElementTypeButton'
        GARAGE_DOOR_OPENED='by.ios_predicate|label CONTAINS "Garage Door has been opened!"'
        GARAGE_DOOR_CLOSED='by.ios_predicate|label CONTAINS "Garage Door has been closed!"'
        GARAGE_DOOR_OPEN_STATUS = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Open"`]'
        GARAGE_DOOR_CLOSED_STATUS = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Closed"`]'
        OVERTIME_REMINDER='by.ios_predicate|label == "Overtime reminder"'
        OVERTIME_REMINDER_TIME='by.ios_predicate|label == "$replace"'
        SAVE_OVERTIME_REMINDER='by.ios_predicate|label == "Save"'
        OVERTIME_WARNING='by.ios_predicate|label == "Overtime Warning"'
        """空净控制"""
        AIR_ON_OFF ='by.ios_predicate|label == "iconMap100 onOff"'
        AIR_SPEED ='by.ios_predicate|label == "iconMap100 speed"'
        AIR_HIGH_SPEED ='by.ios_predicate|label =="iconMap100 hight"'
        AIR_MID_SPEED ='by.ios_predicate|label== "iconMap100 medium"'
        AIR_LOW_SPEED='by.ios_predicate|label=="iconMap100 low"'
        AIR_SLEEP_MODEL ='by.ios_predicate|label == "iconMap100 sleep"'
        AIR_CHILD_LOCK ='by.ios_predicate|label == "iconMap100 lock"'
        AIR_STATUS_ON='by.ios_predicate|label == "On"'
        AIR_STATUS_OFF ='by.ios_predicate|label == "Off"'
        """home双开关"""
        HOME_SWITCH_ONE ='by.xpath|//XCUIElementTypeButton[@name="$replace"]/following-sibling::XCUIElementTypeButton'
        HOME_SWITCH_TWO ='by.xpath|(//XCUIElementTypeButton[@name="$replace"])/following-sibling::XCUIElementTypeButton/following-sibling::XCUIElementTypeButton'
    else:
        logger.error(f"client异常：{Set.client}")