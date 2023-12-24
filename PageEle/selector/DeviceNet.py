# -*- coding: utf-8 -*-
# @Time    : 2022/6/24 16:55
# @Author  : XuLei
# @FileName: DeviceNet.py
# @Software: PyCharm
from Common.set import Set
from Common.log import logger


class DeviceNet:
    if Set.client == "android":
        NEXT=f"by.id|{Set.Apk}:id/bt_next"
        CHECK_LED_LIGHT_NEXT=f"by.id|{Set.Apk}:id/bt_auto"
        TURN_ON_LOCATION = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/alertTitle') and contains(@text, 'Turn on location service')]"
        SURE="by.xpath|//*[contains(@resource-id,'android:id/button1') and contains(@text, 'Sure')]"
        MIUI_PERMISSION="by.id|com.lbe.security.miui:id/parentPanel"
        MIUI_LOCATION_PERMISSION="by.id|com.lbe.security.miui:id/permission_allow_foreground_only_button"  #miui的位置权限bn
        ANDROID_WIFI_SELECT=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')]"  #设备本身wifi
        Multiple_Device_Found=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Multiple Devices Found')]"  #多个设备wifi页面
        RESCAN=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/bt_rescan') and contains(@text, 'Rescan')]"  #重新扫描按钮
        CONNECT_WIFI="by.xpath|//*[contains(@resource-id,'android:id/button1') and contains(@text, 'Connect')]"  #连接wifi
        BIND_SUCCESS="by.xpath|//*[contains(@text, 'Successfully connected to Meross Wi-Fi')]"  #成功连接wifi 提示
        """重命名设备"""
        RENAME_DEVICE = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Rename Your Device')]"
        DEVICE_NAME=f"by.id|{Set.Apk}:id/et_name"  #设备名称
        CUSTOMIZE_YOUR_ICON=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Choose Device Icon')]"  #设备icon
        JOIN_YOUR_HOME_WIFI=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Join Your Home Wi-Fi')]"
        WIFI_BT=f"by.id|{Set.Apk}:id/ll_wifi"
        NEW_NETWORK=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')]"
        REFRESH_WIFI=f"by.id|{Set.Apk}:id/iv_right"
        PWD=f"by.id|{Set.Apk}:id/et_passWd"
        WIFI_BIND_SUCCESS=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Congratulations!')]"
        DONE=f'by.id|{Set.Apk}:id/bt_done'
        NO_DEVICE_TOAST="by.xpath|//*[ contains(@text, 'No Meross device is detected.')]"  #没发现该类设备wifi的提示
        GARAGE_DOOR_OPENER_SKIP="by.xpath|//*[contains(@text, 'Skip compatibility check.')]"
        SKIP_HARDWARE_DEPLOYMENT = "by.xpath|//*[contains(@text, 'Skip hardware deployment.')]"
        # 设备入网失败
        DN_ERROR = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Installation Failed')]"
        # DN_EXIT = f'by.id|{Set.Apk}:id/tv_exit'
        # 入网成功配第三方
        NOT_NOW=f'by.id|{Set.Apk}:id/btn_submit'
    elif Set.client == "ios":
        NEXT = 'by.ios_predicate|label == "Next" AND name == "Next" AND value == "Next"'
        # NEXT = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Next"`]'
        # HK 配网专属元素
        ADD_HOMEKIT_DEVICE='by.ios_predicate|label == "Add HomeKit Device"'
        ADD_HOMEKIT_NEXT='by.ios_predicate|label == "Next" AND name == "Next" AND type == "XCUIElementTypeButton"'
        CHECK_LED_LIGHT_NEXT = NEXT
        ADD_ACCESSORY='by.ios_predicate|label == "Add Accessory"'
        CANT_SCAN='by.ios_predicate|label == "Scan code or hold iPhone near the accessory. More options…"'
        DEVICE_ICON='by.ios_class_chain|**/XCUIElementTypeCell[`label == "$replace"`]'
        ENTER_SETUP_CODE='by.ios_predicate|label == "Enter HomeKit Setup Code"'
        SETUP_CODE='by.ios_class_chain|**/XCUIElementTypeKey[`label == "$replace"`]'
        CONTINUE_BT='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Continue"`]'
        CLOSE_BT='by.ios_predicate|label == "close"'
        BIND_DONE='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Done"`]'
        HK_DEVICE_NAME='by.ios_predicate|type == "XCUIElementTypeTextField"'
        HK_DEVICE_IDENTIFY='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Identify"`]'
        HK_BIND_FAIL='by.ios_predicate|label=="Accessory is not reachable."'
        HK_BIND_FAIL_FINE='by.ios_predicate|label=="OK"'
        """选择设备版本"""
        SELECT_VERSION='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Select the Version"`]'
        NO_HK='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Non-HomeKit Version"`]'
        HK='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "HomeKit Version"`]'
        TURN_ON_LOCATION = 'by.ios_class_chain|**/XCUIElementTypeAlert[`label == "Turn on Precise Location Service"`]'
        SURE = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "OK"`]'
        """ios设置里的wifi"""
        CONNECT_TO_DEVICE='by.ios_predicate|label == "Connect to Device"'
        GOTO_WIFI_SETTINGS='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Go to Wi-Fi settings"`]'
        SET_WIFI='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "WLAN"`]'  #ios设置里的wifi图标
        WIFI_NAME='by.ios_predicate|label == "$replace"'  #ios wifi设置里的wifi名
        WIFI_SWITCH='by.ios_class_chain|**/XCUIElementTypeSwitch[`label == "WLAN"`]'
        CONNECTED_WIFI="""by.ios_predicate|label == "I've connected to the device Wi-Fi." AND name == "I've connected to the device Wi-Fi." AND type == "XCUIElementTypeButton"""
        """重命名设备"""
        RENAME_DEVICE='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Rename Your Device"`]'
        DEVICE_NAME='by.ios_predicate|type=="XCUIElementTypeTextField"'
        CUSTOMIZE_YOUR_ICON='by.ios_predicate|label == "Customize Your Icon"'
        """连接wifi"""
        JOIN_YOUR_HOME_WIFI='by.ios_predicate|name == "Join Your Home Wi-Fi" AND type == "XCUIElementTypeNavigationBar"'
        WIFI_BT='by.xpath|//XCUIElementTypeImage[@name="上下"]/preceding-sibling::XCUIElementTypeButton'
        NEW_NETWORK='by.ios_predicate|label == "$replace"'
        REFRESH_WIFI='by.ios_class_chain|**/XCUIElementTypeNavigationBar[`name == "Change Network"`]/XCUIElementTypeButton[2]'
        PWD='by.ios_predicate|type="XCUIElementTypeSecureTextField"'
        WIFI_BIND_SUCCESS ='by.ios_predicate|label == "Congratulations!"'
        DONE = 'by.ios_predicate|label == "Done" AND name == "Done" AND type == "XCUIElementTypeButton"'
        NO_DEVICE_TOAST = ''  #没发现该类设备wifi的提示
        GARAGE_DOOR_OPENER_SKIP='by.ios_class_chain|**/XCUIElementTypeLink[`label == "Skip compatibility check."`]'
        SKIP_HARDWARE_DEPLOYMENT="by.ios_predicate|label=='Skip hardware deployment.'"
        # 设备入网失败
        DN_ERROR = "by.ios_predicate|label =='Installation Failed'"
        # 入网成功配第三方
        NOT_NOW='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Not now"`]'
    else:
        logger.error(f"client异常：{Set.client}")

