# -*- coding: utf-8 -*-
# @Time    : 2022/8/9 15:09
# @Author  : XuLei
# @FileName: Tools.py
# @Software: PyCharm
# 维护公共的工具方法 （不进行ui操作）
import json
import time
import threading
import allure
import jmespath

from Common.log import logger
from Common.set import Set
from Common.mqtt_data_deal import DealData


class Tools:
    @staticmethod
    def re_ele(old, re_str):
        re_str = old.replace('$replace', re_str)
        return re_str

    @staticmethod
    def start_deal(title, detail: dict):
        from Common.set import Set
        from Common.Flow import Flow
        logger.info(f"开始执行用例:{title}\n"
                    f"{detail}")
        allure.dynamic.title(title)
        # with allure.step(f"测试数据:{detail}"):
        #     pass
        if Set.debug == '0' or Set.debug == '1':
            logger.debug('关闭debug模式')
            if 'user' in detail.keys():
                if detail['user'] != Set.account:
                    logger.info('账号不同或未登录，尝试登出')
                    Flow.assert_log_out()
                    setattr(Set, 're_login', 1)
                else:
                    logger.info('账号相同，不重新登陆')
                    setattr(Set, 're_login', 0)
            else:
                setattr(Set, 're_login', 1)
                logger.info('账号不同或未登录，尝试登出')
                Flow.assert_log_out()
        else:
            logger.info('打开debug模式')
            setattr(Set, 're_login', 0)

    @staticmethod
    def step_log(ps, model='debug', shot='shot'):
        from PageEle.BasePage import Page
        if shot == 'shot':
            filepath = Page().shot()
            with allure.step(ps):
                allure.attach.file(filepath, fr'{ps}', attachment_type=allure.attachment_type.PNG)
        else:
            with allure.step(ps):
                pass
        if model == 'debug':
            logger.debug(ps)
        elif model == "info":
            logger.info(ps)
        elif model == "warn":
            logger.warning(ps)
        elif model == "error":
            logger.error(ps)

    @staticmethod
    def get_value(test_data, key):
        if type(test_data) is dict:
            if key in test_data.keys():
                return test_data[key]
            else:
                return None
        else:
            logger.error('不支持除dict以外的其他格式')

    @staticmethod
    def set_uuid_rule(rule=None, uuid=None, uuid_rule=None, time_diff=None, check_msg=None):
        time.sleep(5)
        if time_diff is not None:
            logger.debug(f'设置校验时间{time_diff}s')
            setattr(Set, 'start_time', time.time())
            setattr(Set, 'time_diff', time_diff)
        if Set.uuid_rule is None:
            if rule is not None:
                setattr(Set, 'check_msg', check_msg)
                return setattr(Set, 'uuid_rule', {uuid: rule})
            elif uuid_rule is not None:
                setattr(Set, 'check_msg', check_msg)
                return setattr(Set, 'uuid_rule', uuid_rule)
            else:
                logger.error('error')
        else:
            if '' in Set.uuid_rule.values():
                logger.debug('校验空规则成功，设备未发送msg')
            else:
                time.sleep(2)

    @staticmethod
    def uuid_rule_deal(uuid_rule, time_diff=0, msg=''):
        start_time = time.time()
        if type(uuid_rule) is str:
            uuid_rule = eval(uuid_rule)
        check_time = int(start_time) + time_diff + 5
        Tools.max_check_time(check_time)
        if type(uuid_rule) is list:
            for item in uuid_rule:
                item['start_time'] = start_time
                item['time_diff'] = time_diff
                item['msg'] = msg
                item['check_time'] = check_time
        elif type(uuid_rule) is dict:
            li = []
            uuid_rule['start_time'] = start_time
            uuid_rule['time_diff'] = time_diff
            uuid_rule['msg'] = msg
            uuid_rule['check_time'] = check_time
            li.append(uuid_rule)
            uuid_rule = li
        else:
            logger.error(f'不支持该类型:{type(uuid_rule)}')
        uuid_rule_collection = Set.uuid_rule_collection + uuid_rule
        setattr(Set, 'uuid_rule_collection', uuid_rule_collection)

    @staticmethod
    def max_check_time(check_time):
        if Set.max_check_time is not None:
            if check_time < int(Set.max_check_time):
                logger.debug('小于最大检测时间，不替换')
            else:
                logger.debug(f'大于最大检测时间,替换为{check_time}')
                setattr(Set, 'max_check_time', check_time)
        else:
            setattr(Set, 'max_check_time', check_time)

    @staticmethod
    def end_deal():
        cur_time = time.time()
        if cur_time < Set.max_check_time:
            Tools.sleep(Set.max_check_time - int(cur_time), '时间不足，等待后进行其他操作')
        else:
            logger.debug('时间已等待，直接进行后续操作')

    @staticmethod
    def assert_rule():
        while True:
            for uuid_rule in Set.uuid_rule_collection:
                if uuid_rule['check_time'] <= time.time() <= uuid_rule['check_time'] + 500:
                    DealData.check_dev_status(uuid_rule['uuid'], uuid_rule['rule'], uuid_rule['msg'])
                    uuid_rule_collection = Set.uuid_rule_collection
                    uuid_rule_collection.remove(uuid_rule)
                    setattr(Set, 'uuid_rule_collection', uuid_rule_collection)
                else:
                    time.sleep(1)
            time.sleep(1)

    @staticmethod
    def sleep(sleep_time, ps=None):
        logger.debug(f'开始等待{sleep_time}s {ps}')
        time.sleep(sleep_time)
        logger.debug('结束本次等待')

    @staticmethod
    def result_check(msg=None):
        if Set.time_diff is not None and Set.start_time is not None:
            now = time.time()
            time_diff = now - Set.start_time
            if time_diff < Set.time_diff:
                need_time = Set.time_diff - time_diff
                logger.debug(f'，开始等待{need_time}s')
                Tools.sleep(need_time, '未达到校验完成所需时间')
            else:
                logger.debug('无需等待')
        if Set.result is True:
            logger.info(f'✅{msg}校验通过')
        # elif Set.result is None and '' in Set.uuid_rule.values():
        #     logger.warning(f'✅{msg}不生效规则 校验通过')
        # else:
        #     logger.warning(f'{msg}消息校验可能失败，请检查')
        else:
            for uuid, rule in Set.uuid_rule.items():
                DealData.check_dev_status(uuid, rule, msg)
            setattr(Set, 'uuid', None)
        setattr(Set, 'result', None)

    @staticmethod
    def thread_start(target, args=(), timeout=None):
        try:
            thead = threading.Thread(target=target, args=args, daemon=True)
            thead.start()
            if timeout is not None:
                thead.join(timeout)
        except BaseException as e:
            logger.debug(e)

    @staticmethod
    def check_online(uuid, device_name='', model='check'):
        result = DealData.get_dev_status(uuid)
        if result is not None:
            online = jmespath.search('payload.all.system.online.status', json.loads(result))
            if online == 1:
                if model == 'check':
                    logger.debug(f'{device_name}设备实际在线')
                return True
            else:
                logger.debug(result)
                if model == 'check':
                    Tools.step_log(f'{device_name}设备实际离线,uuid:{uuid}', shot='')
                    assert False
                return False
        else:
            logger.warning(f'{device_name}设备实际离线,uuid:{uuid}')
            logger.debug(result)
            if model == 'check':
                Tools.step_log(f'{device_name}设备实际离线,uuid:{uuid}', shot='')
                assert False
            return False

    @staticmethod
    def set_all_onoff(onoff):
        logger.debug(f'将全部设备设置为{onoff}状态')
        from Common.data_deal import DataDeal
        if Set.app == 'meross' or Set.app == 'ehome' or Set.app == 'Meross' or Set.app == 'eHome':
             #添加Themorstat、ThemorstatB、SmartPlug的uuid
            yaml_data = DataDeal.get_yaml_data("base_info")['dev_uuid_mapping']
            dev_uuids = {}

            # 添加键值对
            dev_uuids.update({key: 'themorstat' for key in yaml_data['themorstat'].keys()})
            dev_uuids.update({key: 'themorstatB' for key in yaml_data['themorstatB'].keys()})
            dev_uuids.update({key: 'smartPlug' for key in yaml_data['smartPlug'].keys()})
            dev_uuids.update({key: 'hub_themorstat' for key in yaml_data['hub_Themorstat'].keys()})
            dev_uuids.update({key: 'diffuser' for key in yaml_data['diffuser'].keys()})
        else:
            dev_uuids = DataDeal.get_yaml_data("base_info")['dev_uuid_mapping_refoss'].keys()
        for uuid in dev_uuids:
           if dev_uuids[uuid] == 'themorstat':
                DealData.thermostat_mode(uuid, onoff)
           elif dev_uuids[uuid] == 'themorstatB':
                DealData.thermostat_modeB(uuid, onoff)
           elif dev_uuids[uuid] == 'hub_themorstat':
                DealData.hub_toggleX(uuid, onoff)
           elif dev_uuids[uuid] == 'diffuser':
                DealData.diffuser_Light(uuid, onoff)        
           else:
                DealData.toggleX(uuid, onoff)
           time.sleep(1)
        # assert False

    @staticmethod
    def check_online_all():
        from Common.data_deal import DataDeal
        if Set.app == 'meross' or Set.app == 'ehome' or Set.app == 'Meross' or Set.app == 'eHome':
            #添加Themorstat、ThemorstatB、SmartPlug的uuid
            yaml_data = DataDeal.get_yaml_data("base_info")['dev_uuid_mapping']
            dev_uuids = set(yaml_data['themorstat'].keys())
            dev_uuids.update(yaml_data['themorstatB'].keys())
            dev_uuids.update(yaml_data['smartPlug'].keys())
            dev_uuids.update(yaml_data['hub'].keys())
            dev_uuids.update(yaml_data['diffuser'].keys())
        else:
            dev_uuids = DataDeal.get_yaml_data("base_info")['dev_uuid_mapping_refoss'].keys()
        li = []
        for uuid in dev_uuids:
            result = Tools.check_online(uuid, model='no')
            li.append(result)
        if all(li) is True:
            logger.debug('待测设备全部在线，继续测试')
        else:
            Tools.step_log(ps='待测设备中存在离线状态设备，请检查后继续', shot='')
            assert False

    @staticmethod
    def date_time(ts):
        now = int(ts)
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        time_array = time.localtime(now)
        date_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        return date_time

    @staticmethod
    def to_exchange(model):
        if Set.app=='refoss' and model=='uid':
            return Set.refoss_login['data']['userid']
        elif Set.app=='meross' and model=='uid' or Set.app=='Meross' and model=='uid':
            return Set.meross_login['data']['userid']
        elif Set.app=='meross' and model=='key' or Set.app=='Meross' and model=='key':
            return Set.meross_login['data']['key']
        elif Set.app=='refoss' and model=='key':
            return Set.refoss_login['data']['key']

    @staticmethod
    def swipe_down(self):
        size = self.driver.get_window_size()
        print('当前屏幕分辨率为',size)
        start_x = int(size['width']*0.5)
        start_y = int(size['height'] * 0.8)
        end_x = start_x
        end_y = int(size['height'] * 0.2)
        self.driver.swipe(start_x, start_y, end_x, end_y)

    @staticmethod
    def time_to_timestamp(current_time: str):
        if "M" in current_time:
            if 'PM' in current_time:
                current_time1 = current_time.replace(current_time[0:2], str(int(current_time[0:2])+12), 1)
                current_time = current_time1[0:6] + current_time1[9::]
            else:
                current_time = current_time[0:6] + current_time[9::]
        array_time = time.strptime(current_time, "%H:%M %Y-%m-%d")

        # 转换为时间戳
        time_stamp = int(time.mktime(array_time))
        return time_stamp


if __name__ == '__main__':
    # print(Tools.date_time(time.time()))
    Tools.check_online_all()
#     {'apiStatus': 0, 'sysStatus': 0, 'info': '', 'timeStamp': 1672984791,
#      'data': {'userid': '2203602', 'email': '2392914540@qq.com', 'key': '486804daae34b928037cd2f1363652b2',
#               'token': '18e6180bbcf8ace0d136df3c69e286b855585a18b5db6677b3989f3852b6557b',
#               'domain': 'https://iotx-us.meross.com', 'mqttDomain': 'mqtt-us-2.meross.com', 'mfaLockExpire': 0}}
# 2023 - 01 - 06
# 13: 59:51.709 | DEBUG | __main__: get_data:137 - app
    # Tools.thread_start(target=Tools().assert_rule)
    # uuid_rule = [{'uuid': '2009281241656400042334298f1f2958', 'rule': 'togglex[0].channel==0,togglex[0].onoff==0'}]
    # Tools.uuid_rule_deal(uuid_rule)
    # time.sleep(60)
    # print(Set.uuid_rule_collection)
    # Tools.check_online('2206080341745800017334298f1f352d')
    # time.sleep(2000)
