import os
import webbrowser
from Common.set import Set

buildNumber = os.getenv("build_number")

run_case = {'case_id': '','tag':'meross',  #通过case_id、tag筛选用例；tag区分了meross、merossAn和refoss
            'cycles_num':1,  #重复次数 测试稳定性使用
            'phone_id': 26,  # 测试手机参数 从phone_info.yaml选取测试手机
            'app': 'xhs',  #测试app meross ehome Refoss
            'record': '0',  #录像开关 默认关
            'debug': '0',  #调试开关
            'report_switch': '0'}  #测试报告发送开关


if __name__ == '__main__':
    if run_case['debug']=='0':
        from Common.Tools import Tools
        # Tools.check_online_all() 
        # Tools.set_all_onoff('off')
        os.system('pytest  -s -v '
                  ' --reruns 2 --reruns-delay 2')
        """allure报告生成"""
        # os.system('allure generate %s -o %s --clean' % ('TestReport/result/%s'% buildNumber, 'TestReport/report')) 
        # """自动打开报告"""
        # webbrowser.open('http://localhost:63342/app-auto/TestReport/report/index.html')
    else:
        from Common.Tools import Tools
        Tools.set_all_onoff('off')
        os.system('pytest '
                  ' -s -v  '
                  ' --alluredir  TestReport/debug_result/%s'% buildNumber)
        os.system('allure generate %s -o %s --clean' % ('TestReport/debug_result/%s'% buildNumber, 'TestReport/debug_report'))
        webbrowser.open('http://localhost:63342/app-auto/TestReport/debug_report/index.html')

    #

