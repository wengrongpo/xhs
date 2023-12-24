# -*- coding: utf-8 -*-
# @Time    : 2022/6/23 13:46
# @Author  : XuLei
# @FileName: NaviSelector.py
# @Software: PyCharm
from Common.set import Set
from PageEle.selector.HomeSelector import HomeSelector
from Common.log import logger


class NaviSelector:
    if Set.client == "android":
        HOME_MODEL = HomeSelector.HOME_MODEL  #底部导航栏Home模块
        USER_MODEL = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/navigation_title') and contains(@text, 'User')]"  #底部导航栏user模块
        SMART_MODEL=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/navigation_title') and contains(@text, 'Smart')]"  #底部导航栏Smart模块
        HOT_DEAL_MODEL=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/navigation_title') and contains(@text, 'Hot Deals')]"  #底部导航栏user模块
        FORUM_MODEL=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/navigation_title') and contains(@text, 'Forum')]"  #底部导航栏Forum模块
        HOME_TITLE=HomeSelector.HOME_TITLE  #HOME的title
        USER_TITLE=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'User')]"
        SMART_TITLE=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Smart')]"
        HOT_DEAL_TITLE=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Hot Deals')]"
        FORUM_TITLE=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Forum')]"
    elif Set.client == "ios":
        HOME_MODEL = HomeSelector.HOME_MODEL  # 底部导航栏Home模块
        USER_MODEL = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "User"`]'  # 底部导航栏user模块
        SMART_MODEL = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "Smart"`]'  # 底部导航栏Smart模块
        HOT_DEAL_MODEL ='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Hot Deals"`]'  # 底部导航栏user模块
        FORUM_MODEL = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "Forum"`]'  # 底部导航栏Forum模块
        HOME_TITLE = HomeSelector.HOME_TITLE  # HOME的title
        USER_TITLE = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "User"`]'
        SMART_TITLE = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Smart"`]'
        HOT_DEAL_TITLE = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Hot Deals"`]'
        FORUM_TITLE = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Forum"`]'
    else:
        logger.error(f"client异常：{Set.client}")