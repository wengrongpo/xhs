# -*- coding: utf-8 -*-
# @Time    : 2022/9/7 16:41
# @Author  : XuLei
# @FileName: SmartSelector.py
# @Software: PyCharm
from Common.set import Set
from Common.log import logger


class SmartSelector:
    if Set.client == "android":
        ROUTINE_TAB=f'by.id|{Set.Apk}:id/tv_smart_routines'
        SCENE_TAB=f'by.id|{Set.Apk}:id/tv_smart_scenes'
        PLUS_BT=f'by.id|{Set.Apk}:id/iv_right'
        ROUTINE_SETUP=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Routine Setup')]"
        AUTO_OFF=f"by.xpath|//*[contains(@text,'Auto off after X min')]"
        ON_OFF_SCHEDULE=f"by.xpath|//*[contains(@text,'On/off on a schedule')]"
        ROUTINE_SWITCH= f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')]/../following-sibling::android.widget.Switch"
        # AUTO_OFF
        SELECT_DEVICE_TITLE=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, '1/2 Select a Device')]"
        SELECT_DEVICE=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_content') and contains(@text, '$replace')]"
        SELECT_TIME_TITLE=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, '2/2 Select a Time')]"
        SELECT_TIME_NEXT=f'by.id|{Set.Apk}:id/bt_next'
        # ON_OFF_SCHEDULE
        SELECT_DEVICE_OR_SCENE_TITLE=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, '1/2 Select a Device or Scene')]"
        SELECT_DEVICE_OR_SCENE=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_content') and contains(@text, '$replace')]"
        SELECT_STATUS_TITLE=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, '1/2 Select a Status')]"
        SELECT_STATUS=f"by.xpath|//*[contains(@text,'$replace')]"
        # 命名 ROUTINE
        NAME_ROUTINE_TITLE = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Name Your Routine')]"
        NAME_ROUTINE = f'by.id|{Set.Apk}:id/et_name'
        SAVE_ROUTINE = f'by.id|{Set.Apk}:id/bt_ok'
        ROUTINE_SUCCESS=f'by.id|{Set.Apk}:id/positiveButton'
        # routine 详情
        ROUTINE_DETAIL_TITLE= f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Edit Routine')]"
        ROUTINE_DETAIL = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')]"
        DELETE_ROUTINE=f'by.id|{Set.Apk}:id/bt_del'
        CONFIRM_DELETE=f"by.xpath|//*[contains(@resource-id,'android:id/button1') and contains(@text, 'Delete')]"
        CANCEL_DELETE=f"by.xpath|//*[contains(@resource-id,'android:id/button2') and contains(@text, 'Cancel')]"
        EDIT_TIME=f'by.id|{Set.Apk}:id/ll_time'
        EDIT_DEVICE=f'by.id|{Set.Apk}:id/ll_device'
        EDIT_NAME=f'by.id|{Set.Apk}:id/ll_name'
        NEW_NAME=f'by.id|{Set.Apk}:id/et_name'
        EDIT_STATUS=f'by.id|{Set.Apk}:id/ll_status'
        ROUTINE_EDIT_SCENE=f'by.id|{Set.Apk}:id/ll_device'
        SAVE=f"by.xpath|//*[contains(@text, 'Save')]"
        BACK=f'by.id|{Set.Apk}:id/iv_left_gone'
        # scene
        CREATE_SCENE_NAME = f'by.id|{Set.Apk}:id/et_name'
        CREATE_SCENE_TITLE = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Create Scene')]"
        AWAY_SCENE = f"by.xpath|(//*[contains(@resource-id,'{Set.Apk}:id/iv_icon')])[1]"
        HOME_SCENE = f"by.xpath|(//*[contains(@resource-id,'{Set.Apk}:id/iv_icon')])[2]"
        SELECT_DEVICES_TITLE = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Select Devices')]"
        SCENE_SELECT_DEVICE =f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')]"
        ADD_ALL =f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_select_all') and contains(@text,'Add all')]"
        REMOVE_ALL = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_select_all') and contains(@text, 'Remove all')]"
        SCENE_DONE = f'by.id|{Set.Apk}:id/tv_done'
        ADD_REMOVE_DEVICES = f'by.id|{Set.Apk}:id/ll_change_device'
        DEVICES_SAVE = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_right ') and contains(@text, 'Save')]"
        EDIT_SCENE_NAME = f'by.xpath|{Set.Apk}:id/tv_scene_name'
        EDIT_SCENE_NAME_INPUT = f'by.xpath|{Set.Apk}:id/et_name'
        EDIT_SCENE_NAME_SAVE = f"by.xpath|{Set.Apk}:id/bt_save"
        SCENE_SETTINGS = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Scene Settings')]"
        LIGHT_SPRAY=f'by.id|{Set.Apk}:id/tv_mode_discontinuous'
        SCENE_MODIFY=f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_scene_name') and contains(@text, 'scene_modify')]"
        SCENE_DETAIL_DONE = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_right') and contains(@text, 'Done')]"
        RUN_SCENE = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')]/../following-sibling::android.view.ViewGroup"
        SCENE_DETAIL = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_name') and contains(@text, '$replace')]"
        DELETE_SCENE = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_done') and contains(@text, 'Delete scene')]"
        DELETE_ALL_SCENE=f"by.xpath|(//*[contains(@resource-id,'{Set.Apk}:id/tv_name')])[1]"
        DELETE_ALL_ROUTINE=f"by.xpath|(//*[contains(@resource-id,'{Set.Apk}:id/tv_name')])[1]"
        CONFIRM_DELETE_SCENE =f"by.xpath|//*[contains(@resource-id,'android:id/button1') and contains(@text, 'Delete')]"

    elif Set.client == "ios":
        ROUTINE_TAB = 'by.ios_predicate|label == "Routines"'
        SCENE_TAB = 'by.ios_predicate|label == "Scenes"'
        PLUS_BT = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "add"`]'
        ROUTINE_SETUP = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Routine Setup"`]'
        AUTO_OFF = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Auto off after X min"`]'
        ON_OFF_SCHEDULE = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "On/off on a schedule"`]'
        ROUTINE_SWITCH=f'by.xpath|//XCUIElementTypeStaticText[@name="$replace"]/following-sibling::XCUIElementTypeButton'
        # AUTO_OFF
        SELECT_DEVICE_TITLE = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "1/2 Select a Device"`]'
        SELECT_DEVICE = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "$replace"`]'
        SELECT_TIME_TITLE = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "2/2 Select a Time"`]'
        SELECT_TIME_NEXT = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Next"`]'
        # ON_OFF_SCHEDULE
        SELECT_DEVICE_OR_SCENE_TITLE = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "1/2 Select a Device or Scene"`]'
        SELECT_DEVICE_OR_SCENE = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "$replace"`]'
        SELECT_STATUS_TITLE = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "1/2 Set a Status"`]'
        SELECT_STATUS = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "$replace"`]'
        # 命名 ROUTINE
        NAME_ROUTINE_TITLE = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Name Your Routine"`]'
        NAME_ROUTINE = f'by.ios_predicate|type == "XCUIElementTypeTextField"'
        SAVE_ROUTINE = f'by.ios_class_chain|**/XCUIElementTypeButton[`label == "Save"`]'
        ROUTINE_SUCCESS=f'by.ios_class_chain|**/XCUIElementTypeButton[`label == "Got it"`]'
        # routine 详情
        ROUTINE_DETAIL_TITLE = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Edit Routine"`]'
        ROUTINE_DETAIL = f'by.ios_predicate|label == "$replace"'
        DELETE_ROUTINE = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Delete routine"`]'
        CONFIRM_DELETE = f'by.ios_class_chain|**/XCUIElementTypeButton[`label == "Delete"`]'
        CANCEL_DELETE = f'by.ios_class_chain|/XCUIElementTypeButton[`label == "Cancel"`]'
        EDIT_TIME = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Time"`]'
        EDIT_DEVICE = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Device"`]'
        EDIT_NAME = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Routine name"`]'
        NEW_NAME = f'by.ios_predicate|type=="XCUIElementTypeTextField"'
        EDIT_STATUS = f'by.ios_predicate|label == "Status"'
        ROUTINE_EDIT_SCENE = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Scenes"`]'
        SAVE = f'by.ios_predicate|label == "Save"'
        BACK = f'by.ios_predicate|label == "return"'
        # scene
        CREATE_SCENE_NAME='by.ios_predicate|type="XCUIElementTypeTextField"'
        CREATE_SCENE_TITLE='by.ios_predicate|label == "Create Scene"'
        AWAY_SCENE='by.xpath|(//XCUIElementTypeCollectionView/XCUIElementTypeCell)[1]'
        HOME_SCENE='by.xpath|(//XCUIElementTypeCollectionView/XCUIElementTypeCell)[2]'
        SELECT_DEVICES_TITLE='by.ios_predicate|label == "Select Devices"'
        SCENE_SELECT_DEVICE='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "$replace"`]'
        ADD_ALL='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Add all"`]'
        REMOVE_ALL='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Remove all"`]'
        SCENE_DONE='by.ios_predicate|label == "Done"'
        ADD_REMOVE_DEVICES='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Add or remove devices"`]'
        DEVICES_SAVE='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Save"`]'
        EDIT_SCENE_NAME='by.ios_predicate|label == "Scene name"'
        EDIT_SCENE_NAME_INPUT='by.ios_predicate|type="XCUIElementTypeTextField"'
        EDIT_SCENE_NAME_SAVE='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Save"`]'
        SCENE_SETTINGS='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Scene Settings"`]'
        SCENE_DETAIL_DONE='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Done"`]'
        RUN_SCENE='by.xpath|(//XCUIElementTypeStaticText[@name="$replace"]/preceding-sibling::XCUIElementTypeButton[@name="Run"])[1]'
        SCENE_DETAIL='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "$replace"`][1]'
        DELETE_SCENE='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Delete scene"`]'
        DELETE_ALL_SCENE='by.xpath|//XCUIElementTypeButton[@name="Run"][1]/following-sibling::XCUIElementTypeImage'
        DELETE_ALL_ROUTINE='by.xpath|(//XCUIElementTypeStaticText/following-sibling::XCUIElementTypeStaticText)[1]'
        CONFIRM_DELETE_SCENE='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Delete"`]'
