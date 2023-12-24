# -*- coding: utf-8 -*-
# @Time    : 2022/6/23 15:56
# @Author  : XuLei
# @FileName: DeviceSelect.py
# @Software: PyCharm
from Common.set import Set
from Common.log import logger


class DeviceSelector:
    if Set.client == "android":
        TITLE=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Select a Device')]"
        SEARCH=f"by.id|{Set.Apk}:id/et_search"
        CATE_REPLACE=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')]"
        DEVICE_REPLACE=f"by.xpath|(//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')])[1]"
        MORE=f"by.id|{Set.Apk}:id/tv_more"
        ENABLE_BLUETOOTH=f"by.xpath|//*[contains(@resource-id,'android:id/alertTitle') and contains(@text, 'Enable Bluetooth')]"
        ENABLE_BLUETOOTH_OK=f"by.id|android:id/button1"
        CHOOSE_THE_MODEL=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Choose the Model')]"
    elif Set.client == "ios":
        TITLE = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Select a Device"`]'
        SEARCH = 'by.ios_class_chain|**/XCUIElementTypeSearchField[`label == "Search with product name or model."`]'
        CATE_REPLACE ='by.xpath|//XCUIElementTypeOther[@name="Please select a device you would like to install."]/following-sibling::XCUIElementTypeCell/XCUIElementTypeStaticText[@name="$replace"]'
        DEVICE_REPLACE = 'by.xpath|(//*[contains(@name,"$replace")])[1]'
        MORE = 'by.ios_predicate|label == "More" AND name == "More" AND value == "More"'
        ENABLE_BLUETOOTH = "by.ios_predicate|label == 'Enable Bluetooth'"
        ENABLE_BLUETOOTH_OK = "by.ios_predicate|label == 'OK' and type='XCUIElementTypeButton'"
        CHOOSE_THE_MODEL="by.ios_predicate|label == 'Choose the Model'"
    else:
        logger.error(f"client异常：{Set.client}")