from Common.log import logger


class Set:
    client = None
    desired_caps = None
    driver = None
    driver_timeout=1000
    # 全局隐式等待时间
    wait_time = 0
    # 安卓包名
    Apk = None
    # app 名称
    app = 'meross'
    # email获取验证码相关
    email = None
    del_email = None
    origin_pwd = None
    changed_pwd = None
    # 录像开关
    record = None
    # 调试模式
    debug = None
    # 账号
    account = None
    # 测试报告
    report_switch = None
    # 是否重新登录
    re_login = None
    #
    tester=None
    # mqtt
    meross_login ={'apiStatus': 0, 'sysStatus': 0, 'info': '', 'timeStamp': 1672984881, 'data': {'userid': '2203602', 'email': '2392914540@qq.com', 'key': '486804daae34b928037cd2f1363652b2', 'token': '18e6180bbcf8ace0d136df3c69e286b832aab11523da72c4cf460d537a9a46c4', 'domain': 'https://iotx-us.meross.com', 'mqttDomain': 'mqtt-us-2.meross.com', 'mfaLockExpire': 0}}
    refoss_login = {'apiStatus': 0, 'sysStatus': 0, 'info': '', 'timeStamp': 1672984881, 'data': {'userid': '2765794', 'email': '2392914540@qq.com', 'key': '006c27bcf7da74261d3876ae840c94e5', 'token': '18e6180bbcf8ace0d136df3c69e286b832aab11523da72c4cf460d537a9a46c4', 'domain': 'https://iotx.refoss.net', 'mqttDomain': 'mqtt.refoss.net', 'mfaLockExpire': 0}}
    uuid_rule = None
    start_time=None
    time_diff=None
    check_msg=None
    result=None
    sign_meross='486804daae34b928037cd2f1363652b2'
    sign_refoss='006c27bcf7da74261d3876ae840c94e5'
    uuid_rule_collection=[]
    max_check_time=None
    check_result=True
