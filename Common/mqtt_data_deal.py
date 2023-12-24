# -*- coding: utf-8 -*-
# @Time    : 2022/10/28 6:42 PM
# @Author  : XuLei
# @FileName: mqtt_data_deal.py
# @Software: PyCharm
import base64
import hashlib
import json
import time
from retrying import retry
import jmespath
import requests
import uuid
from Common.log import logger


class DealData:
    # 获取当前时间戳
    @staticmethod
    def get_timestamp():
        return str(int(time.time()))

    @staticmethod  # 封装md5加密方法
    def to_md5(msg):
        m = hashlib.md5()
        m.update(msg.encode(encoding='utf-8'))
        return m.hexdigest()

    # 封装params转json转base64方法
    @staticmethod
    def to_base64(params):
        params_json = json.dumps(params).encode('utf-8')
        params_base64 = base64.b64encode(params_json)
        return params_base64

    @staticmethod
    def get_msgId():
        uid = str(uuid.uuid4())
        suid = ''.join(uid.split('-'))
        return suid

    # 封装sign方法
    @staticmethod
    def to_sign(timestamp, params=None, messageId=None, key=None, ns=None):
        # 固件接口带namespace,sign = md5(messageId + key + timestamp)
        if ns != None:
            if key == None:
                key = 'a3eca56029a2b7677b731b7cab73fb86'
                sign = DealData.to_md5(messageId + key + timestamp)
                return sign
            else:
                sign = DealData.to_md5(messageId + key + timestamp)
                return sign
        # app接口,sign = md5(key + timestamp + Nonce + params_base64_str)
        Nonce = "autotest"
        params_base64 = DealData.to_base64(params)
        params_base64_str = params_base64.decode()
        if key is None:
            key = "23x17ahWarFH6w29"
            sign = DealData.to_md5(key + timestamp + Nonce + params_base64_str)
            return sign
        sign = DealData.to_md5(key + timestamp + Nonce + params_base64_str)
        return sign

    @staticmethod
    def meross_login(http_url, email, password, Vendor):
        url = http_url + "/v1/Auth/signIn"
        headers = {"Vendor": Vendor}
        params = {
            "email": email,
            "password": str(password)
        }
        timestamp = DealData.get_timestamp()
        params_base64 = DealData.to_base64(params)
        sign = DealData.to_sign(timestamp, params)
        from Common.set import Set
        setattr(Set, 'sign', sign)
        data = {
            "nonce": "autotest",
            "params": params_base64,
            "sign": sign,
            "timestamp": timestamp
        }

        r = requests.post(url, headers=headers, data=data, verify=True)
        result = r.json()
        if result['apiStatus'] == 0:
            pass
        else:
            print(result)
            logger.error("%s 登录失败 %s" % (Vendor, result['apiStatus']))
        return result

    @staticmethod
    def meross_logout(http_url, token, Vendor):
        url = http_url + "/v1/Profile/logout"
        headers = {"Vendor": Vendor, "Authorization": "Basic %s" % token}
        params = {
        }
        timestamp = DealData.get_timestamp()
        params_base64 = DealData.to_base64(params)
        sign = DealData.to_sign(timestamp, params)
        data = {
            "nonce": "autotest",
            "params": params_base64,
            "sign": sign,
            "timestamp": timestamp
        }
        r = requests.post(url, headers=headers, data=data, verify=True)
        result = r.json()
        if result['apiStatus'] == 0:
            logger.debug("%s 退出登录成功!" % Vendor)
        else:
            logger.debug("%s 退出登录失败 %s" % (Vendor, result['apiStatus']))

    def get_data(self, model, mac=None, device_uuid=None):
        from Common.set import Set
        from Common.data_deal import DataDeal
        user_info = DataDeal.get_base_info()["user_info"]
        if Set.app == 'meross' or Set.app == 'ehome':
            http_url = 'https://iotx-us.meross.com'
        else:
            http_url = 'https://iotx.refoss.net'
        if Set.meross_login is None:
            result = self.meross_login(http_url, user_info['user'], user_info['pwd'], Set.app)
            logger.debug('login start')
            setattr(Set, "meross_login", result)
            setattr(Set,'sign',result['data']['key'])
            logger.debug(result)
        else:
            logger.debug('跳过登陆')
            result = Set.meross_login
        mqtt_host = result['data']['mqttDomain']
        userid = result['data']['userid']
        key = result['data']['key']
        if model == 'app':
            password = self.to_md5(userid + key)
            client_id = 'app:' + '5bbd27fdef2e9951d6a80195da0380a71a69c797'
            sub_topic = "/app/" + userid + "/subscribe"
            logger.debug('app')
            return {"client_id": client_id, "sub_topic": sub_topic, "username": userid, 'password': password,
                    'mqtt_host': mqtt_host}
        elif model == 'device':
            password = str(userid) + "_" + self.to_md5(mac + key)
            bind_id = self.to_md5(self.get_timestamp())[0:16]
            client_id = 'fmware:' + device_uuid + '_' + bind_id
            sub_topic = "/appliance/" + device_uuid + "/subscribe"
            return {"client_id": client_id, "sub_topic": sub_topic, "username": mac, 'password': password,
                    'mqtt_host': mqtt_host}
        else:
            logger.error('error')

    @staticmethod
    def sys_all_msg(topic, dev_uuid):
        msg_id = DealData.get_msgId()
        timestamp = DealData.get_timestamp()
        from Common.set import Set
        sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign_meross, ns='namespace')
        msg = {
            "header": {
                "messageId": msg_id,
                "namespace": "Appliance.System.All",
                "method": "GET",
                "timestamp": int(timestamp),
                "sign": sign,
                "from": topic,
                'payloadVersion': 1,
                'triggerSrc': 'Android',
                'uuid': dev_uuid
            },
            "payload": {
            }
        }
        return msg

    @staticmethod
    def toggleX(dev_uuid, onoff):
        headers = {'contentType': 'application/json'}
        from Common.data_deal import DataDeal
        ip = DataDeal.get_dev_ip(dev_uuid)
        url = f'http://{ip}/config'
        msg_id = DealData.get_msgId()
        timestamp = DealData.get_timestamp()
        from Common.set import Set
        if Set.sign_meross is None:
            DealData().get_data('app',device_uuid=uuid)
        if Set.app == 'meross' or Set.app == 'ehome' or Set.app == 'Meross' or Set.app == 'eHome':
            sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign_meross, ns='namespace')
        else:
            sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign_refoss, ns='namespace')
        #sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign, ns='namespace')
        from Common.Tools import Tools
        uid = Tools.to_exchange('uid')
        if onoff == 'off':
            dev_status = 0
        elif onoff == 'on':
            dev_status = 1
        msg = {
            "header": {
                "from": f"/app/{uid}-15ec7e29a3aa42e19fbcf941d26e54f0/subscribe",  # meross2203602   refoss2765794
                "messageId": msg_id,
                "method": "SET",
                "namespace": "Appliance.Control.ToggleX",
                "payloadVersion": 1,
                "sign": sign,
                "timestamp": int(timestamp),
                "triggerSrc": "UIAUTO",
                "uuid": dev_uuid
            },
            "payload": {
                "togglex": {
                    "channel": 0,
                    "onoff": dev_status,
                    'lmTime': timestamp
                }
            }
        }
        # logger.debug(msg)
        try:
            res = requests.request(method='post', data=json.dumps(msg), url=url, timeout=20, headers=headers)
            print(res.json())
            return json.dumps(res.json())
        except BaseException as e:
            logger.error(e)
            pass

    @staticmethod
    def thermostat_mode(dev_uuid, onoff):
        headers = {'contentType': 'application/json'}
        from Common.data_deal import DataDeal
        ip = DataDeal.get_dev_ip(dev_uuid)
        url = f'http://{ip}/config'
        msg_id = DealData.get_msgId()
        timestamp = DealData.get_timestamp()
        from Common.set import Set
        if Set.sign_meross is None:
            DealData().get_data('app', device_uuid=uuid)
        if Set.app == 'meross' or Set.app == 'ehome' or Set.app == 'Meross' or Set.app == 'eHome':
            sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign_meross, ns='namespace')
        else:
            sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign_refoss, ns='namespace')
        from Common.Tools import Tools
        uid = Tools.to_exchange('uid')
        if onoff == 'off':
            dev_status = 0
        elif onoff == 'on':
            dev_status = 1
        msg = {
            "header": {
                "from": f"/app/{uid}-15ec7e29a3aa42e19fbcf941d26e54f0/subscribe",  # meross2203602   refoss2765794
                "messageId": msg_id,
                "method": "SET",
                "namespace": "Appliance.Control.Thermostat.Mode",
                "payloadVersion": 1,
                "sign": sign,
                "timestamp": int(timestamp),
                "triggerSrc": "UIAUTO",
                "uuid": dev_uuid
            },
            "payload": {
                "mode": [{
                    "channel": 0,
                    "onoff": dev_status
                    # 'lmTime': timestamp
                }]
            }
        }
        # logger.debug(msg)
        try:
            res = requests.request(method='post', data=json.dumps(msg), url=url, timeout=20, headers=headers)
            print(res.json())
            return json.dumps(res.json())
        except BaseException as e:
            logger.error(e)
            pass

    @staticmethod
    def thermostat_modeB(dev_uuid, onoff):
        headers = {'contentType': 'application/json'}
        from Common.data_deal import DataDeal
        ip = DataDeal.get_dev_ip(dev_uuid)
        url = f'http://{ip}/config'
        msg_id = DealData.get_msgId()
        timestamp = DealData.get_timestamp()
        from Common.set import Set
        if Set.sign_meross is None:
            DealData().get_data('app', device_uuid=uuid)
        if Set.app == 'meross' or Set.app == 'ehome' or Set.app == 'Meross' or Set.app == 'eHome':
            sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign_meross, ns='namespace')
        else:
            sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign_refoss, ns='namespace')
        from Common.Tools import Tools
        uid = Tools.to_exchange('uid')
        if onoff == 'off':
            dev_status = 0
        elif onoff == 'on':
            dev_status = 1
        msg = {
            "header": {
                "from": f"/app/{uid}-15ec7e29a3aa42e19fbcf941d26e54f0/subscribe",  # meross2203602   refoss2765794
                "messageId": msg_id,
                "method": "SET",
                "namespace": "Appliance.Control.Thermostat.ModeB",
                "payloadVersion": 1,
                "sign": sign,
                "timestamp": int(timestamp),
                "triggerSrc": "UIAUTO",
                "uuid": dev_uuid
            },
            "payload": {
                "modeB": [{
                    "channel": 0,
                    "onoff": dev_status
                    # 'lmTime': timestamp
                }]
            }
        }
        # logger.debug(msg)
        try:
            res = requests.request(method='post', data=json.dumps(msg), url=url, timeout=20, headers=headers)
            print(res.json())
            return json.dumps(res.json())
        except BaseException as e:
            logger.error(e)
            pass

    @staticmethod
    def hub_toggleX(dev_uuid, onoff):
        headers = {'contentType': 'application/json'}
        from Common.data_deal import DataDeal
        ip = DataDeal.get_dev_ip(dev_uuid)
        dev_id=DataDeal.get_dev_hub_id(dev_uuid)
        url = f'http://{ip}/config'
        msg_id = DealData.get_msgId()
        timestamp = DealData.get_timestamp()
        from Common.set import Set
        if Set.sign_meross is None:
            DealData().get_data('app', device_uuid=uuid)
        if Set.app == 'meross' or Set.app == 'ehome' or Set.app == 'Meross' or Set.app == 'eHome':
            sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign_meross, ns='namespace')
        else:
            sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign_refoss, ns='namespace')
        from Common.Tools import Tools
        uid = Tools.to_exchange('uid')
        if onoff == 'off':
            dev_status = 0
        elif onoff == 'on':
            dev_status = 1
        msg = {
            "header": {
                "from": f"/app/{uid}-15ec7e29a3aa42e19fbcf941d26e54f0/subscribe",  # meross2203602   refoss2765794
                "messageId": msg_id,
                "method": "SET",
                "namespace": "Appliance.Hub.ToggleX",
                "payloadVersion": 1,
                "sign": sign,
                "timestamp": int(timestamp),
                "triggerSrc": "UIAUTO",
                "uuid": dev_uuid
            },
            "payload": {
                "togglex": [{
                    "channel": 0,
                    "onoff": dev_status,
                    "id": dev_id
                    # 'lmTime': timestamp
                }]
            }
        }
        # logger.debug(msg)
        try:
            res = requests.request(method='post', data=json.dumps(msg), url=url, timeout=20, headers=headers)
            print(res.json())
            return json.dumps(res.json())
        except BaseException as e:
            logger.error(e)
            pass

    @staticmethod
    def diffuser_Light(dev_uuid, onoff):
        headers = {'contentType': 'application/json'}
        from Common.data_deal import DataDeal
        ip = DataDeal.get_dev_ip(dev_uuid)
        url = f'http://{ip}/config'
        msg_id = DealData.get_msgId()
        timestamp = DealData.get_timestamp()
        from Common.set import Set
        if Set.sign_meross is None:
            DealData().get_data('app', device_uuid=uuid)
        if Set.app == 'meross' or Set.app == 'ehome' or Set.app == 'Meross' or Set.app == 'eHome':
            sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign_meross, ns='namespace')
        else:
            sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign_refoss, ns='namespace')
        from Common.Tools import Tools
        uid = Tools.to_exchange('uid')
        if onoff == 'off':
            dev_status = 0
        elif onoff == 'on':
            dev_status = 1
        msg = {
            "header": {
                "from": f"/app/{uid}-15ec7e29a3aa42e19fbcf941d26e54f0/subscribe",  # meross2203602   refoss2765794
                "messageId": msg_id,
                "method": "SET",
                "namespace": "Appliance.Control.Diffuser.Light",
                "payloadVersion": 1,
                "sign": sign,
                "timestamp": int(timestamp),
                "triggerSrc": "UIAUTO",
                "uuid": dev_uuid
            },
            "payload": {
                "light": [{
                    "channel": 0,
                    "onoff": dev_status,
                    "type": 'mod100'
                    # 'lmTime': timestamp
                }]
            }
        }
        # logger.debug(msg)
        try:
            res = requests.request(method='post', data=json.dumps(msg), url=url, timeout=20, headers=headers)
            print(res.json())
            return json.dumps(res.json())
        except BaseException as e:
            logger.error(e)
            pass

    def retry_if_result_none(result):
        """Return True if we should retry (in this case when result is None), False otherwise"""
        return result is None

    

    @staticmethod
    @retry(stop_max_attempt_number=3, wait_fixed=5, retry_on_result=retry_if_result_none)
    def get_dev_status(uuid):
        headers = {'contentType': 'application/json'}
        msg_id = DealData.get_msgId()
        timestamp = DealData.get_timestamp()
        from Common.data_deal import DataDeal
        ip = DataDeal.get_dev_ip(uuid)
        url = f'http://{ip}/config'
        from Common.set import Set
        if Set.sign_meross is None:
            DealData().get_data('app',device_uuid=uuid)
        if Set.app == 'meross' or Set.app == 'ehome' or Set.app == 'Meross' or Set.app == 'eHome':
            sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign_meross, ns='namespace')
        else:
            sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign_refoss, ns='namespace')
        #sign = DealData.to_sign(timestamp=timestamp, messageId=msg_id, key=Set.sign_meross, ns='namespace')
        from Common.Tools import Tools
        uid = Tools.to_exchange('uid')
        data = {"header": {
            "from": f"/app/{uid}-15ec7e29a3aa42e19fbcf941d26e54f0/subscribe",  #meross2203602   refoss2765794
            "messageId": msg_id,
            "method": "GET",
            "namespace": "Appliance.System.All",
            "payloadVersion": 1,
            "sign": sign,
            "timestamp": timestamp,
            "triggerSrc": "UIAUTO",
            "uuid": uuid
        },
            "payload": {
            }}
        try:
            res = requests.request(method='post', data=json.dumps(data), url=url, timeout=15, headers=headers)
            return json.dumps(res.json())
        except BaseException as e:
            logger.error(e)
            return None

    @staticmethod
    def check_dev_status(uuid, rule, msg=''):
        dev_data = DealData.get_dev_status(uuid)
        li = []
        if rule.find(',') != -1:
            rule_list = rule.split(',')
            for single_rule in rule_list:
                result = DealData.check_single_rule(single_rule, dev_data)
                li.append(result)
            assert_result = all(li)
        else:
            assert_result = DealData.check_single_rule(rule, dev_data)
        from Common.Tools import Tools
        if assert_result:
            Tools.step_log(fr'✅{msg}中规则{rule}在{uuid}校验成功')
        else:
            Tools.step_log(fr'❎{msg}校验失败，规则:{rule}，数据:{dev_data}')
            from Common.set import Set
            setattr(Set, 'check_result', False)

    @staticmethod
    def check_single_rule(single_rule, dev_data):
        single_rule = single_rule.split('==')
        if single_rule[0].find('control') != -1:
            exp = 'payload.all.' + single_rule[0]
        else:
            exp = 'payload.all.digest.' + single_rule[0]
        result = jmespath.search(exp, json.loads(dev_data))
        if str(result) == single_rule[1]:
            return True
        else:
            return False


if __name__ == '__main__':
    DealData().get_data('app',device_uuid='1812142018080529088434298f198337')

