# -*- coding: utf-8 -*-
# @Time    : 2022/10/31 10:49 AM
# @Author  : XuLei
# @FileName: mqtt_check.py
# @Software: PyCharm
# python3.6
import json
import re
import time
import threading
import _thread
from Common.log import logger
from paho.mqtt import client as mqtt_client
from Common.mqtt_data_deal import DealData
from Common.set import Set
import random
import jmespath
from datetime import datetime

mqtt_msg = None


def connect_mqtt(mqtt_data) -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            pass
        else:
            logger.error(f"Failed to connect, return code {rc}")

    client = mqtt_client.Client(client_id=mqtt_data['client_id'],clean_session=False)
    client.username_pw_set(username=mqtt_data['username'], password=mqtt_data['password'])
    client.tls_set()
    client.on_connect = on_connect
    client.connect(mqtt_data['mqtt_host'], 443)
    return client


def subscribe(client: mqtt_client, topic):
    def on_message(client, userdata, msg):
        global mqtt_msg
        mqtt_msg = msg.payload.decode()
        mqtt_msg = eval(mqtt_msg)
        logger.debug(f'收到消息：{json.dumps(mqtt_msg)}，从`{msg.topic}` topic')
        filer_data(client)
    client.subscribe(topic)
    client.on_message = on_message


def sub_topic(client, topic):
    subscribe(client, topic)


def filer_data(client):
    if Set.uuid_rule is not None:
        if 'uuid' in mqtt_msg['header'].keys():
            uuid = mqtt_msg['header']['uuid']
            if uuid in Set.uuid_rule.keys():
                logger.debug(f'开始匹配{Set.uuid_rule[uuid]},收到{mqtt_msg}')
                rule_deal(client, mqtt_msg, uuid, Set.uuid_rule[uuid])
            else:
                logger.warning(f'error uuid:{Set.uuid_rule[uuid]},msg:{mqtt_msg}')
        elif mqtt_msg['header']['namespace'] == 'Appliance.Control.Diffuser.Spray':
            pattern = "[" + r'\\/appliancepublish' + "]"
            uuid = re.sub(pattern, "", mqtt_msg['header']['from'])
            if uuid in Set.uuid_rule.keys():
                logger.debug(f'开始匹配{Set.uuid_rule[uuid]},收到{mqtt_msg}')
                rule_deal(client, mqtt_msg, uuid, Set.uuid_rule[uuid])
            else:
                logger.warning(f'error uuid:{Set.uuid_rule[uuid]},msg:{mqtt_msg}')
        else:
            logger.debug(f'uuid不匹配，无需校验{mqtt_msg}')


def rule_deal(client, msg, uuid, rule):
    li = []
    if rule.find(',') != -1:
        rule_list = rule.split(',')
        for single_rule in rule_list:
            result = check_rule(client, single_rule, msg)
            li.append(result)
        assert_result = all(li)
    elif rule == '':
        if 'triggerSrc' in msg['header']:
            if msg['header']['triggerSrc'] == 'CloudSchedule':
                assert_result = False
                setattr(Set, 'result', assert_result)
    else:
        assert_result = check_rule(client, rule, msg)
    if assert_result is True:
        logger.debug('✅本次mqtt判断为真')
        del Set.uuid_rule[uuid]
    else:
        logger.warning(f'❎{Set.check_msg}校验可能失败,{msg}消息未匹配上规则:{rule},请检查')
        setattr(Set, 'check_result', False)
    if Set.uuid_rule == {}:
        setattr(Set, 'result', True)
        setattr(Set, 'uuid_rule', None)
        from Common.Tools import Tools
        Tools.step_log(f'✅{Set.check_msg}成功',shot='')
        if Set.start_time is not None:
            end_time = time.time()
            time_diff = end_time - Set.start_time
            if Set.time_diff - 100 < time_diff < Set.time_diff + 100:
                logger.info(f'✅校验:时间差{Set.time_diff}s 校验成功')
            else:
                logger.warning(f'❎时间校验可能失败,预期时间{Set.time_diff},实际时间{time_diff}')
            setattr(Set, 'start_time', None)
            setattr(Set, 'time_diff', None)
        elif Set.time_diff is None:
            setattr(Set, 'result', None)


def check_rule(client, single_rule, msg):
    single_rule = single_rule.split('==')
    result = jmespath.search('payload.' + single_rule[0], msg)
    try:
        if str(result) == single_rule[1]:
            return True
        else:
            return False
    except BaseException as e:
        logger.error(f'❎报错{e},result:{result},{single_rule[1]},{type(result)},{type(single_rule[1])}')


def app_check():
    logger.debug('开始连接mqtt')
    mqtt_data = DealData().get_data('app')
    mq_client = connect_mqtt(mqtt_data)
    sub_topic(mq_client, mqtt_data["sub_topic"])
    mq_client.loop_forever()


def ack_check():
    logger.debug('开始连接mqtt')
    mqtt_data = DealData().get_data('app')
    mq_client = connect_mqtt(mqtt_data)
    sub_topic(mq_client,'/app/2101871-eefe7b21578cfbfa6c1eb22a886ad38c/subscribe')
    mq_client.loop_start()


def device_check(mac, uuid):
    logger.debug('开始连接mqtt')
    mqtt_data = DealData().get_data('device', mac, uuid)
    mq_client = connect_mqtt(mqtt_data)
    sub_topic(mq_client, mqtt_data["sub_topic"])
    mq_client.loop()
    return mq_client


if __name__ == "__main__":
    pass
    t1 = threading.Thread(target=app_check)
    t1.start()
    # uuid = '2103025607485600014734298f1f2cb7'
    # mac = '34:29:8f:1f:2c:b7'
    # recv_topic = '/app/2101871-eefe7b21578cfbfa6c1eb22a886ad38c/subscribe'
    # send_topic = f'/appliance/{uuid}/subscribe'
    # mqtt_data = DealData().get_data('app')
    # print(mqtt_data)
    # mq_client = connect_mqtt(mqtt_data)
    # sub_topic(mq_client, send_topic)
    # mq_client.loop()
    # msg = DealData.sys_all_msg(recv_topic, uuid)
    # print(msg)
    # mq_client.publish(send_topic, payload=json.dumps(msg))
    # print('end')
    # client.publish(topic,json.dumps(msg))
    # client.loop()
    time.sleep(3000)
    # t1 = threading.Thread(target=device_check,args=('48:e1:e9:97:20:0f', '1805217646202425132534298f11a5e7',),daemon=True)
    # t1.start()
    #
    # # setattr(Set, 'uuid_rule', {'2009281241656400042334298f1f2958
    # print('hhhhh')
    # time.sleep(2000)
# if __name__ == '__main__':
#     _thread.start_new_thread(app_check, ())
#     # _thread.start_new_thread(device_check, ('48:e1:e9:97:20:0f', '1805217646202425132534298f11a5e7',))
#     time.sleep(3000)
# _thread.start_new_thread(mqtt_check, ('app','togglex[0].onoff==1,togglex[0].channel==0','1805217646202425132534298f11a5e7',))
# _thread.start_new_thread(mqtt_check, (
#     'app', 'payload.togglex.channel|1,payload.togglex.onoff|1', '2009281241656400042334298f1f2958
