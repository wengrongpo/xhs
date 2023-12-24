# -*- coding: utf-8 -*-
# @Time    : 2022/7/14 3:13 PM
# @Author  : XuLei
# @FileName: data_deal.py
# @Software: PyCharm
import allure
import yaml
import traceback
import string
import random
from Common.log import logger
from run import *


class DataDeal:
    @staticmethod
    def get_yaml_data(model):
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        if model == 'case_info':
            path = path + '/TestData/case_info.yaml'
        elif model == 'device_info':
            path = path + '/TestData/device_info.yaml'
        elif model == 'phone_info':
            path = path + '/TestData/phone_info.yaml'
        elif model == "base_info":
            path = path + '/TestData/base_info.yaml'
        else:
            logger.error("error")
        with open(path, 'r', encoding='utf-8') as f:
            cfgs = yaml.safe_load(f)
            return cfgs

    @staticmethod
    def get_email():
        email_info = DataDeal.get_yaml_data('base_info')["email_info"]
        setattr(Set, 'email', email_info["email"])
        setattr(Set, 'del_email', email_info["del_email"])
        setattr(Set, 'origin_pwd', email_info["origin_pwd"])
        setattr(Set, 'changed_pwd', email_info["changed_pwd"])
        return email_info

    @staticmethod
    def get_base_info():
        return DataDeal.get_yaml_data('base_info')

    @staticmethod
    def get_pop_up_window():
        return DataDeal.get_yaml_data('base_info')["pop_up_window"]

    @staticmethod
    def setting():
        phone_id = run_case["phone_id"]
        record = run_case["record"]
        debug = run_case["debug"]
        debug = DataDeal.switch_assert(debug, 'debug')
        record = DataDeal.switch_assert(record, 'record')
        setattr(Set, "record", record)
        setattr(Set, "debug", debug)
        # if Set.debug =='0':
        #     tester = input('\n***********请输入测试人员姓名以继续：*********\n')
        #     setattr(Set, 'tester', tester)
        # setattr(Set, "report_switch", run_case['report_switch'])
        app = run_case["app"]
        desired_caps = DataDeal.get_yaml_data('phone_info')
        for desired_cap in desired_caps:
            if desired_cap["phone_id"] == phone_id:
                client = desired_cap["platformName"]
                if client=='iOS':
                    client='ios'
                app = DataDeal.app_package(app, client=client)
                DataDeal.set_desired_caps(desired_cap, app)

    @staticmethod
    def debug_model(case):
        debug = case["debug"]
        debug = DataDeal.switch_assert(debug, 'debug')
        setattr(Set, "debug", debug)

    @staticmethod
    def switch_assert(v, msg):
        if v == "1" or v == "0":
            return v
        elif v == 1 or v == 0:
            return str(v)
        else:
            logger.error(f"{msg} model error:{v}")

    @staticmethod
    def set_desired_caps(desired_cap, app):
        client = desired_cap["platformName"]
        if client=='iOS':
            client='ios'
        setattr(Set, "client", client)
        del desired_cap["phone_id"]
        if client == 'ios':
            desired_cap["app"] = app
        elif client == "android":
            desired_cap["appPackage"] = app
        else:
            logger.error("error")
        desired_cap['newCommandTimeout'] = Set.driver_timeout
        logger.debug(f'driver的最长等待时间是{Set.driver_timeout}')
        setattr(Set, "Apk", app)
        setattr(Set, "desired_caps", desired_cap)
        appname = app.split('.')[2]
        setattr(Set, "app", appname)

    @staticmethod
    def get_case_info():
        case_info = DataDeal().select_case()
        device_info = DataDeal.get_yaml_data("device_info")
        wifi_info = DataDeal.get_yaml_data("base_info")["wifi_info"]
        user_info = DataDeal.get_yaml_data("base_info")["user_info"]
        re_data = {**wifi_info, **user_info}
        case_info = DataDeal.replace_data(case_info, re_data)
        for case in case_info:
            for device in device_info:
                if 'device_id' in case:
                    if device["device_id"] == case['device_id']:
                        for key, value in device.items():
                            case[key] = value
        return case_info

    @staticmethod
    def replace_data(case_info, re_data):
        for case in case_info:
            for key, value in re_data.items():
                if key in case.keys():
                    if case[key] == "$":
                        case[key] = value
            for key2, value2 in case.items():
                if type(value2) is str:
                    if value2.find("$random_str") != -1:
                        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 12))
                        value2 = case[key2].replace("$random_str", ran_str)
                        case[key2] = value2
        return case_info

    @staticmethod
    @allure.step("获取测试用例")
    def get_test_data(func):
        case_info = DataDeal().get_case_info()
        test_data = []
        for case in case_info:
            if case["func"] == func:
                test_data.append(case)
        if type(run_case['cycles_num']) is int:
            if run_case['cycles_num'] > 1:
                test_data=run_case['cycles_num']*test_data
        return test_data

    @staticmethod
    def select_case():
        rule = run_case
        case_info = DataDeal.get_yaml_data("case_info")
        case_rule = rule["case_id"]
        tags = rule["tag"]
        case_rule_list = DataDeal().case_id_rule(case_rule, case_info)
        tags_list = DataDeal().tag_rule(tags, case_info)
        case_list = case_rule_list + tags_list
        case_list = DataDeal().del_repeat(case_list, "case_id")
        return case_list

    @staticmethod
    def case_id_rule(case_rule, case_info):
        test_case = []
        if case_rule in ['all', "ALL"]:
            test_case = case_info
        elif case_rule == '':
            pass
        else:
            for case_id in case_rule.split(','):
                if case_id.find(":") != -1:
                    case_list = case_id.split(':')
                    a = int(case_list[0]) - 1
                    b = int(case_list[1])
                    new_case = case_info[a:b]
                    test_case.extend(new_case)
                else:
                    for case_single in case_info:
                        if case_single["case_id"] == case_id:
                            test_case.append(case_single)
        return test_case

    @staticmethod
    def tag_rule(tags, case_info):
        test_case = []
        if tags == '':
            pass
        else:
            for case_single in case_info:
                for tag in tags.split(","):
                    if "tag" in case_single.keys():
                        for tag2 in case_single['tag'].split(","):
                            if tag2==tag:
                                test_case.append(case_single)
                    else:
                        logger.error(f"case_single:{case_single}没有tag")
        return test_case

    @staticmethod
    def del_repeat(data, key):  # data 列表  key 去重的键
        new_data = []  # 用于存储去重后的list
        values = []  # 用于存储当前已有的值
        for d in data:
            if d[key] not in values:
                new_data.append(d)
                values.append(d[key])
        return new_data

    @staticmethod
    def set_email_pwd(origin_pwd, changed_pwd):
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        path = path + '/TestData/base_info.yaml'
        with open(path, 'r', encoding='utf-8') as f:
            cfgs = yaml.load(f.read(), Loader=yaml.FullLoader)
            cfgs['email_info']['origin_pwd'] = origin_pwd
            cfgs['email_info']['changed_pwd'] = changed_pwd
            with open(path, 'w', encoding='utf-8') as w_f:
                yaml.dump(cfgs, w_f)  # 覆盖原先的配置文件
                logger.info(f'成功更新初始密码{origin_pwd}')

    @staticmethod
    def app_package(app, client):
        if app == 'meross' and client == 'ios':
            app_package = 'com.meross.Meross'
        elif app== 'xhs':
            app_package = 'com.xingin.xhs'
        elif app == 'merossbeta' and client == 'ios':
            app_package = 'com.meross.merossBeta'
        elif app == 'merossbeta' and client == 'android':
            app_package = 'com.meross.meross.beta'
        elif app == 'meross' and client == 'android':
            app_package = 'com.meross.meross'
        elif app == 'ehome' and client == 'ios':
            app_package = 'com.meross.eHome'
        elif app == 'ehome' and client == 'android':
            app_package = 'com.meross.ehome'
        elif app == 'Refoss' and client == 'ios':
            app_package = 'com.refoss.refoss'
        elif app == 'Refoss' and client == 'android':
            app_package = 'com.refoss.refoss'
        else:
            app_package = ''
            logger.error('error')
        return app_package

    @staticmethod
    def get_dev_ip(uuid):
        yaml_data = DataDeal.get_yaml_data("base_info")['dev_uuid_mapping']
        dev_uuids = {}
            # 添加键值对
        dev_uuids.update(yaml_data['themorstat'].items())
        dev_uuids.update(yaml_data['themorstatB'].items())
        dev_uuids.update(yaml_data['smartPlug'].items())
        dev_uuids.update(yaml_data['hub'].items())
        dev_uuids.update(yaml_data['diffuser'].items())
        if uuid in dev_uuids :
            return dev_uuids[uuid]
        else:
            dev_uuid = DataDeal.get_yaml_data("base_info")["dev_uuid_mapping_refoss"]
            return dev_uuid[uuid]

    @staticmethod
    def get_dev_hub_id(uuid):
        dev_uuids = DataDeal.get_yaml_data("base_info")['dev_uuid_mapping']['hub_Themorstat']
        if uuid in dev_uuids :
            return dev_uuids[uuid]
        else:
            dev_uuid = DataDeal.get_yaml_data("base_info")["dev_uuid_mapping_refoss"]
            return dev_uuid[uuid]    


if __name__ == '__main__':
    logger.debug(DataDeal.get_test_data('test_do_network_normal'))
