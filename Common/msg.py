# -*- coding: utf-8 -*-
# @Time    : 2022/9/29 13:42
# @Author  : XuLei
# @FileName: msg.py
# @Software: PyCharm
import requests
from Common.log import logger
from Common.set import Set


def push_test_report(report):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=528edc8299a166cf1bfe3bef59e2968b86bde93982013e312228bc1527496f4e'
    header = {"Content-Type": "application/json"}
    report_url = 'https://cn-cd-dx-4.natfrp.cloud:19382/'
    pass_case=report["case_pass"]
    fail_case=report["case_fail"]
    time=int(report["case_time"])

    client=Set.client
    if client=='ios':
        client='iOS'
    elif client =='android':
        client='Android'
    app=Set.app
    if app=='eHome':
        app='eHomeLife'
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    start_time=report['case_start_time']
    end_time=report['case_end_time']
    all_case=pass_case + fail_case + report['case_error']
    pass_per='{:.2%}'.format(pass_case/all_case)
    time_consuming = "%02d小时%02d分钟%02d秒" % (h, m, s)
    json = {"msgtype": "text", "text": {"content": f"APP UI自动化测试报告推送\n"
                                                   f"测试时间:{start_time}~{end_time}\n"
                                                   f"耗时:{time_consuming}\n"
                                                   f"测试App:{app} {client}客户端\n"
                                                   f"测试人员:{Set.tester}\n"
                                                   f"测试通过率:{pass_per}\n"
                                                   f"测试通过:{pass_case}条,测试不通过:{fail_case}条\n"
                                                   f"测试报告地址:{report_url}"}}
    if pass_case>15 and Set.debug=='0':
        requests.request(method='POST', headers=header, url=url, json=json)
    else:
        logger.info('调试不发报告')
    logger.info(json)
