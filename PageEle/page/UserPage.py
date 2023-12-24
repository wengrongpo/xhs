import time
import allure
from PageEle.BasePage import Page
from PageEle.selector.UserSelector import *
from Common.mail import GetCode
from Common.data_deal import DataDeal


class UserPage(Page):
    @allure.step("进入注册登录页面")
    def start_login(self):
        self.find_element(UserSelector.START_LOGIN).click()
        self.assert_ele(UserSelector.LOGIN_IN, "进入注册登录页面")

    @allure.step('关闭注册登录页面')
    def close_start_login(self):
        self.find_element(UserSelector.CLOSE_BT).click()

    @allure.step("选择登录入口")
    def login_in(self):
        self.find_element(UserSelector.LOGIN_IN).click()
        self.assert_ele(UserSelector.USER, '选择登录入口')

    @allure.step("选择注册入口")
    def sign_up(self, email, pwd, judge=None):
        self.find_element(UserSelector.SIGN_UP).click()
        self.assert_ele(UserSelector.SIGN_UP_NAVI, "进入注册账号页面")
        self.find_element(UserSelector.SIGN_UP_EMAIL).send_keys(email)
        self.find_element(UserSelector.SIGN_UP_PWD).send_keys(pwd)
        self.hide_keyboard()
        #  特殊 操作不同
        if judge == "uncheck_agreement":
            self.find_element(UserSelector.SIGNUP_BT).click()
            self.find_element(UserSelector.AGREE_SIGN).click()
        self.find_element(UserSelector.AGREE_SIGN).click()
        time.sleep(0.5)
        self.find_element(UserSelector.SIGNUP_BT).click()

    @allure.step('注册校验')
    def signup_judge(self, judge, email, pwd):
        """判断注册是否正确响应"""
        if judge == "normal":
            self.assert_ele(UserSelector.USER_TITLE, f"{email}账号注册")
        elif judge == "invalid_email":
            self.assert_ele(UserSelector.INVALID_EMAIL, f"{email}异常格式")
        elif judge == "registered":
            self.assert_ele(UserSelector.REGISTERED, f"{email}账号已注册")
            self.find_element(UserSelector.REGISTERED_LOGIN).click()
            self.assert_ele(UserSelector.LOGIN_BTN, f"已注册账号跳转login页面")
        elif judge == "pwd_less":
            time.sleep(3)
            self.assert_ele(UserSelector.SIGN_UP_NAVI, f"{pwd}密码不符合规定，注册失败")
        elif judge == "uncheck_agreement":
            time.sleep(3)
            self.assert_ele(UserSelector.SIGN_UP_NAVI, "未勾选注册协议，不能注册")
        else:
            logger.error(f"不支持该judge：{judge}")

    @allure.step("输入账密,点击登录")
    def login(self, user, pwd, judge="normal"):
        self.find_element(UserSelector.USER).clear()
        self.find_element(UserSelector.USER).send_keys(user)
        self.find_element(UserSelector.PWD).send_keys(pwd)
        if judge == 'uncheck_agreement':
            self.find_element(UserSelector.LOGIN_BTN).click()
            self.find_element(UserSelector.AGREE_SIGN).click()
        self.hide_keyboard()
        self.find_element(UserSelector.AGREE_SIGN).click()
        self.find_element(UserSelector.LOGIN_BTN).click()
        while self.find_element(UserSelector.NO_NETWORK,model='assert'):
            self.find_element(UserSelector.NO_NETWORK_OK).click()
            self.find_element(UserSelector.LOGIN_BTN).click()
            logger.warning('网络状况可能不好')
            time.sleep(3)

    @allure.step('登录校验')
    def login_judge(self, judge='normal', user=None):
        if judge == 'normal':
            user_li = user.split("@")[0]
            username = UserSelector.USER_NAME.replace('$replace', user_li)
            if self.assert_ele(username, "账号正常登录", 30):
                setattr(Set, 'account', user)
        elif judge == 'pwd_wrong':
            self.assert_ele(UserSelector.PWD_WRONG, "登陆时密码错误")
        elif judge == 'uon_exist_user':
            self.assert_ele(UserSelector.UON_EXIST_USER, "输入不存在的账号")
        elif judge == 'uncheck_agreement':
            self.assert_ele(UserSelector.LOGIN_BTN, "不同意协议无法登录")
        else:
            logger.error('error')

    @allure.step("进入账号详情")
    def user_detail(self):
        self.find_element(UserSelector.USER_DETAIL).click()
        self.assert_ele(UserSelector.ACCOUNT_TITLE, '进入用户详情')

    @allure.step("账号登出")
    def log_out(self):
        self.user_detail()
        self.find_element(UserSelector.LOG_OUT).click()
        self.find_element(UserSelector.CONFIRM_LOG_OUT).click()
        self.assert_ele(UserSelector.SIGN_UP, "账号登出")

    @allure.step("点击忘记密码")
    def forget_pwd(self, email, new_pwd, judge):
        self.find_element(UserSelector.FORGOT_PASSWORD).click()
        self.assert_ele(UserSelector.FORGOT_TITLE, "进入修改密码页面")
        # 仅支持修改test_data配置的邮箱密码
        time.sleep(2)
        self.find_element(UserSelector.FORGOT_EMAIL).clear()
        self.find_element(UserSelector.FORGOT_EMAIL).send_keys(email)
        self.find_element(UserSelector.FORGOT_SUBMIT).click()
        self.assert_ele(UserSelector.ENTER_CODE, '输入验证码')
        time.sleep(2)
        code = GetCode.get_code()
        self.find_element(UserSelector.V_CODE,50).send_keys(code)
        self.find_element(UserSelector.FORGOT_NEXT).click()
        self.assert_ele(UserSelector.RESET_PASSWORD, "重置密码")
        self.find_element(UserSelector.NEW_PWD).send_keys(new_pwd)
        self.find_element(UserSelector.SUBMIT_NEW_PWD).click()
        if self.find_element(UserSelector.SAME_PWD, timeout=10, model='assert'):
            self.find_element(UserSelector.SAME_PWD_OK).click()
            new_pwd='test_pwd'
            self.find_element(UserSelector.NEW_PWD).clear()
            self.find_element(UserSelector.NEW_PWD).send_keys(new_pwd)
            self.find_element(UserSelector.SUBMIT_NEW_PWD).click()
            logger.info('密码相同，已进行异常处理')
        if judge == "normal":
            self.assert_ele(UserSelector.PASSWORD_CHANGED, "密码修改")
            self.find_element(UserSelector.PASSWORD_CHANGED_OK).click()
            return new_pwd

    @allure.step("删除账号")
    def delete_account(self, pwd):
        self.find_element(UserSelector.DELETE_ACCOUNT).click()
        self.assert_ele(UserSelector.DELETE_ACCOUNT_TITLE, '进入删除账号')
        self.find_element(UserSelector.DELETE_ACCOUNT_PWD).send_keys(pwd)
        self.find_element(UserSelector.DELETE_ACCOUNT_TITLE).click()
        self.hide_keyboard()
        self.find_element(UserSelector.DELETE_CONTINUE).click()
        #  隐藏键盘
        self.find_element(UserSelector.DELETE_CODE).click()
        self.hide_keyboard()
        self.assert_ele(UserSelector.VERIFICATION, '进入校验验证码页面')
        code = GetCode.get_code(use="del_user")
        self.find_element(UserSelector.DELETE_CODE).send_keys(code)
        self.assert_ele(UserSelector.DELETE_SUCCESS, "删除账号", 60)
        self.find_element(UserSelector.DELETE_EXIT).click()

    @allure.step('修改邮箱')
    def change_email(self, email, pwd):
        self.find_element(UserSelector.CHANGE_EMAIL, 20).click()
        self.assert_ele(UserSelector.CHANGE_EMAIL_TITLE, "进入修改邮箱页面")
        self.find_element(UserSelector.CHANGE_EMAIL_PWD).send_keys(pwd)
        self.find_element(UserSelector.CHANGE_NEW_EMAIL).send_keys(email)
        self.find_element(UserSelector.CHANGE_EMAIL_TITLE).click()
        self.find_element(UserSelector.CHANGE_EMAIL_NEXT).click()
        self.find_element(UserSelector.DELETE_CODE).click()
        self.hide_keyboard()
        self.assert_ele(UserSelector.VERIFICATION, '进入校验验证码页面', 20)
        code = GetCode().get_code(use="change_email")
        self.find_element(UserSelector.DELETE_CODE,40).send_keys(code)
        self.assert_ele(UserSelector.CHANGE_EMAIL_SUCCESS, "修改邮箱成功")
        self.find_element(UserSelector.CHANGE_EMAIL_LOGIN).click()

    @allure.step('修改密码')
    def change_pwd(self, pwd, model=None):
        self.find_element(UserSelector.CHANGE_PWD).click()
        self.assert_ele(UserSelector.CHANGE_PASSWORD_TITLE, "进入修改密码页面")
        self.find_element(UserSelector.CHANGE_PASSWORD_SUBMIT).click()
        self.assert_ele(UserSelector.CHANGE_PASSWORD_ENTER_CODE, '进入输入验证码页面')
        if model == 'resend_code':
            from Common.Tools import Tools
            Tools.step_log('等待120s重发验证码')
            time.sleep(120)
            self.find_element(UserSelector.CHANGE_PASSWORD_RESEND_CODE).click()
        code = GetCode.get_code('change_pwd')
        self.find_element(UserSelector.CHANGE_PASSWORD_CODE,60).send_keys(code)
        self.find_element(UserSelector.CHANGE_PASSWORD_NEXT).click()
        self.assert_ele(UserSelector.CHANGE_PASSWORD_RESET_PASSWORD, "进入重置密码界面")
        self.find_element(UserSelector.CHANGE_PASSWORD_NEW_PWD).send_keys(pwd)
        self.find_element(UserSelector.CHANGE_PASSWORD_RESET_SUBMIT).click()
        if self.find_element(UserSelector.SAME_PWD, timeout=10, model='assert'):
            self.find_element(UserSelector.SAME_PWD_OK).click()
            pwd='test_pwd'
            self.find_element(UserSelector.NEW_PWD).clear()
            self.find_element(UserSelector.NEW_PWD).send_keys(pwd)
            self.find_element(UserSelector.SUBMIT_NEW_PWD).click()
        self.assert_ele(UserSelector.PASSWORD_CHANGED, "密码重置")
        self.find_element(UserSelector.PASSWORD_CHANGED_OK).click()
        return pwd

    @allure.step('不发送短信直接修改密码')
    def change_pwd_no_sms(self, pwd):
        self.find_element(UserSelector.CHANGE_PWD).click()
        self.assert_ele(UserSelector.CHANGE_PASSWORD_TITLE, "进入修改密码页面")
        self.find_element(UserSelector.CHANGE_PASSWORD_SUBMIT).click()
        self.assert_ele(UserSelector.CHANGE_PASSWORD_ENTER_CODE, '进入输入验证码页面')
        self.find_element(UserSelector.CHANGE_PASSWORD_STILL_NOT_RECEIVE).click()
        self.assert_ele(UserSelector.CHANGE_PASSWORD_RESET_ACCOUNT_TITLE, '进入重置账号页面')
        self.find_element(UserSelector.CHANGE_PASSWORD_AGREE_RESET).click()
        self.find_element(UserSelector.CHANGE_PASSWORD_RESET_NEW_PWD).send_keys(pwd)
        self.find_element(UserSelector.CHANGE_PASSWORD_RESET_CONFIRM_PWD).send_keys(pwd)
        self.hide_keyboard()
        self.find_element(UserSelector.CHANGE_PASSWORD_RESET_CONFIRM_BTN).click()

    @staticmethod
    def yaml_pwd_change(new_pwd):
        pwd_list = ['justTest0.', 'test0.aa']
        pwd_list.remove(new_pwd)
        old_pwd = pwd_list[0]
        DataDeal.set_email_pwd(new_pwd, old_pwd)

    @allure.step('Alexa跳转验证')
    def integration_alexa(self):
        self.find_element(UserSelector.INTEGRATION_ALEXA).click()
        self.find_element(UserSelector.LINK_WITH_ALEXA_ALLOW)
        self.assert_ele(UserSelector.LINK_WITH_ALEXA_ALLOW,"跳转Alexa应该正确")
        self.find_element(UserSelector.LINK_BACK).click()

    @allure.step('google跳转验证')
    def integration_google(self):
        self.find_element(UserSelector.INTEGRATION_GOOGLE).click()
        self.find_element(UserSelector.LINK_WITH_GOOGLE_ALLOW)
        self.assert_ele(UserSelector.LINK_WITH_GOOGLE_ALLOW,"跳转google应该正确")
        self.find_element(UserSelector.LINK_BACK).click()