from PageEle.selector.NaviSelector import NaviSelector
from Common.set import Set
from Common.log import logger


class UserSelector:
    USER_TITLE = NaviSelector.USER_TITLE
    if Set.client == "android":
        # 注册登录
        START_LOGIN = f'by.id|{Set.Apk}:id/tv_login'   # user模块未登录时的登入按钮
        CLOSE_BT=f'by.id|{Set.Apk}:id/iv_left_gone'
        SIGN_UP = f'by.id|{Set.Apk}:id/bt_create_account'  # 注册登录页面 注册按钮
        LOGIN_IN = f"by.id|{Set.Apk}:id/bt_sign_in"  # 注册登录页面 登录按钮
        USER = f'by.id|{Set.Apk}:id/et_username'
        PWD = f'by.id|{Set.Apk}:id/et_password'
        LOGIN_BTN = f'by.id|{Set.Apk}:id/bt_login'
        UON_EXIST_USER = f'by.id|{Set.Apk}:id/alertTitle'  # 登录账号不存在提示
        PWD_WRONG = "by.xpath|//*[contains(@resource-id,'android:id/message') and contains(@text, 'Password is wrong.')]"  # 登录账号密码错误
        NO_NETWORK="by.xpath|//*[contains(@resource-id,'android:id/message') and contains(@text, 'Please check network.')]"
        NO_NETWORK_OK="by.xpath|//*[contains(@resource-id,'android:id/button1') and contains(@text, 'OK')]"
        # 忘记密码
        FORGOT_PASSWORD = f'by.id|{Set.Apk}:id/tv_forget'
        FORGOT_TITLE = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Forgot Password')]"
        FORGOT_EMAIL = f'by.id|{Set.Apk}:id/et_tel'
        FORGOT_SUBMIT = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/bt_register') and contains(@text, 'Next')]"
        ENTER_CODE = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Enter Code')]"
        V_CODE = f"by.id|{Set.Apk}:id/input"
        FORGOT_NEXT = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/bt_register') and contains(@text, 'Next')]"
        RESEND_CODE = f'by.id|{Set.Apk}:id/tv_resend'
        NEW_PWD = f'by.id|{Set.Apk}:id/et_password'
        RESET_PASSWORD = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Reset Password')]"
        SUBMIT_NEW_PWD = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/bt_change') and contains(@text, 'Submit')]"
        PASSWORD_CHANGED = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/alertTitle') and contains(@text, 'Password Changed')]"
        PASSWORD_CHANGED_OK = f"by.xpath|//*[contains(@class,'android.widget.Button') and contains(@text,'OK')]"
        SAME_PWD=f"by.xpath|//*[contains(@resource-id,'android:id/message') and contains(@text, 'New password shall not be the same as old password.')]"
        SAME_PWD_OK="by.xpath|//*[contains(@resource-id,'android:id/button1') and contains(@text,'OK')]"
        #  删除账号
        DELETE_ACCOUNT =  f'by.id|{Set.Apk}:id/lyt_item_delete_account'
        DELETE_ACCOUNT_TITLE = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Delete account')]"
        DELETE_ACCOUNT_PWD = f'by.id|{Set.Apk}:id/et_code'
        DELETE_CONTINUE =f'by.id|{Set.Apk}:id/btn_continue'
        DELETE_CANCEL =f'by.id|{Set.Apk}:id/btn_cancel'
        DELETE_CODE =f'by.id|{Set.Apk}:id/code_input'
        VERIFICATION =f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Verification')]"
        DELETE_RESEND_CODE =f'by.id|{Set.Apk}:id/btn_resend'
        CANT_RECEIVE_EMAIL =f'by.id|{Set.Apk}:id/tv_can_not_receive'
        DELETE_PROCESS =f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_1') and contains(@text, 'Deleting Account')]"
        DELETE_SUCCESS =f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_subtitle') and contains(@text, 'Account Deleted Successfully')]"
        DELETE_EXIT =f'by.id|{Set.Apk}:id/btn_got_it'
        # user 首页
        USER_NAME = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_nickname') and contains(@text, '$replace')]"
        USER_DETAIL = f'by.id|{Set.Apk}:id/lyt_item_head'
        # user 详情
        ACCOUNT_TITLE =f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Account')]"
        CHANGE_PWD =f'by.id|{Set.Apk}:id/lyt_item_pwd'
        NICK_NAME =f'by.id|{Set.Apk}:id/tv_nickname_'
        INPUT_NICK =f'by.id|{Set.Apk}:id/et_name'
        SAVE_NICK =f'by.id|{Set.Apk}:id/btn_save'
        CHANGE_EMAIL =f'by.id|{Set.Apk}:id/tv_email'
        LOG_OUT =f'by.id|{Set.Apk}:id/lyt_item_logout'
        CONFIRM_LOG_OUT='by.id|android:id/button1'
        CANCEL_LOG_OUT='by.id|android:id/button2'
        # 修改邮箱
        CHANGE_EMAIL_TITLE =f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Change Email')]"
        CHANGE_EMAIL_PWD =f'by.id|{Set.Apk}:id/et_code'
        CHANGE_NEW_EMAIL =f'by.id|{Set.Apk}:id/et_new_email'
        CHANGE_EMAIL_NEXT =f'by.id|{Set.Apk}:id/btn_next'
        CHANGE_EMAIL_SUCCESS =f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_subtitle') and contains(@text, 'Account Email Changed!')]"
        CHANGE_EMAIL_LOGIN =f'by.id|{Set.Apk}:id/btn_got_it'
        # 修改密码
        CHANGE_PASSWORD_TITLE =f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Change Password')]"
        CHANGE_PASSWORD_SUBMIT =f'by.id|{Set.Apk}:id/bt_submit'
        #  暂时无法定位
        CREATE_NEW_ACCOUNT ='??'
        CHANGE_PASSWORD_CODE =f'by.id|{Set.Apk}:id/input'
        CHANGE_PASSWORD_NEXT =f'by.id|{Set.Apk}:id/bt_next'
        CHANGE_PASSWORD_ENTER_CODE =f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Enter Code')]"
        CHANGE_PASSWORD_RESEND_CODE =f'by.id|{Set.Apk}:id/tv_resend'
        CHANGE_PASSWORD_STILL_NOT_RECEIVE =f'by.id|{Set.Apk}:id/tv_not_receive'
        CHANGE_PASSWORD_RESET_PASSWORD =f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Reset Password')]"
        CHANGE_PASSWORD_NEW_PWD =f'by.id|{Set.Apk}:id/et_password'
        CHANGE_PASSWORD_RESET_SUBMIT =f'by.id|{Set.Apk}:id/bt_change'
        CHANGE_PASSWORD_RESET_ACCOUNT_TITLE = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Reset Account')]"
        CHANGE_PASSWORD_AGREE_RESET = f'by.id|{Set.Apk}:id/bt_reset'
        CHANGE_PASSWORD_DISAGREE_RESET = f'by.id|{Set.Apk}:id/bt_not_reset'
        CHANGE_PASSWORD_RESET_NEW_PWD = f'by.id|{Set.Apk}:id/et_password'
        CHANGE_PASSWORD_RESET_CONFIRM_PWD = f'by.id|{Set.Apk}:id/et_confirm_password'
        CHANGE_PASSWORD_RESET_CONFIRM_BTN = f'by.id|{Set.Apk}:id/bt_done'
        CHANGE_PASSWORD_RESET_REFUSE = f'by.id|{Set.Apk}:id/bt_refuse'
        # 注册页面
        SIGN_UP_NAVI = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/tv_title_info') and contains(@text, 'Sign up')]"
        SIGN_UP_EMAIL = f'by.id|{Set.Apk}:id/et_email'
        SIGN_UP_PWD = f'by.id|{Set.Apk}:id/et_password'
        AGREE_SIGN = f'by.id|{Set.Apk}:id/cb_term'
        SIGNUP_BT = f'by.id|{Set.Apk}:id/bt_register'
        REGISTERED = f"by.xpath|//*[contains(@resource-id,'{Set.Apk}:id/alertTitle') and contains(@text, 'Existing account')]"
        REGISTERED_LOGIN=f"by.xpath|//*[contains(@resource-id,'android:id/button1') and contains(@text, 'Log in')]"
        INVALID_EMAIL = "by.xpath|//*[contains(@resource-id,'android:id/message') and contains(@text, 'Invalid email address.')]"
        # integration
        INTEGRATION_ALEXA=f'by.id|{Set.Apk}:id/lyt_item_amazon_alexa'
        LINK_WITH_ALEXA_ALLOW=f'by.id|{Set.Apk}:id/btn_allow'#com.refoss.refoss:id/btn_allow
        INTEGRATION_GOOGLE=f'by.id|{Set.Apk}:id/lyt_item_google_assistant'
        LINK_WITH_GOOGLE_ALLOW = f'by.id|{Set.Apk}:id/btn_allow'
        LINK_BACK= f'by.id|{Set.Apk}:id/iv_back'
    elif Set.client == "ios":
        # 注册登录
        START_LOGIN = "by.id|Log in"  # user模块未登录时的登入按钮
        CLOSE_BT='by.xpath|//XCUIElementTypeNavigationBar/XCUIElementTypeButton'  #关闭按钮
        SIGN_UP = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "Sign up"`]'  # 注册登录页面 注册按钮
        LOGIN_IN = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Log in"`]'  # 注册登录页面 登录按钮
        USER ='by.ios_predicate|type == "XCUIElementTypeTextField"'
        PWD ='by.ios_predicate|type == "XCUIElementTypeSecureTextField"'
        LOGIN_BTN ='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Log in"`]'
        UON_EXIST_USER='by.ios_predicate|label == "This email is not registered."'  #登录账号不存在提示
        PWD_WRONG='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Password is wrong."`]'  #登录账号密码错误
        NO_NETWORK='by.ios_predicate|label == "The Internet Connection error, please try again later.(h:-1009)"'
        NO_NETWORK_OK='by.ios_predicate|label == "OK"'
        # 忘记密码
        FORGOT_PASSWORD='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Forgot password?"`][1]'
        FORGOT_TITLE='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Forgot Password"`]'
        FORGOT_EMAIL="by.ios_predicate|type='XCUIElementTypeTextField'"
        FORGOT_SUBMIT='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Submit"`]'
        ENTER_CODE='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Enter Code"`]'
        V_CODE="""by.xpath|//XCUIElementTypeStaticText[@name="We just sent you a confirmation code via email to help reset your password. Check your junk folder if you didn't receive it."]/following-sibling::XCUIElementTypeOther"""
        FORGOT_NEXT='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Next"`]'
        RESEND_CODE='by.ios_class_chain|**/XCUIElementTypeLink[`label == "Resend code"`]'
        NEW_PWD='by.ios_predicate|type="XCUIElementTypeSecureTextField"'
        RESET_PASSWORD='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Reset Password"`]'
        SUBMIT_NEW_PWD='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Submit"`]'
        PASSWORD_CHANGED='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Password changed"`]'
        PASSWORD_CHANGED_OK = f"by.ios_predicate|label='OK'"
        SAME_PWD='by.ios_predicate|label == "New password can not be the same as previously used passwords."'
        SAME_PWD_OK='by.ios_predicate|label=="OK"'
        #  删除账号
        DELETE_ACCOUNT='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Delete account"`]'
        DELETE_ACCOUNT_TITLE='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Delete Account"`]'
        DELETE_ACCOUNT_PWD='by.ios_class_chain|**/XCUIElementTypeSecureTextField[`value == "Enter password to continue"`]'
        DELETE_CONTINUE='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Continue"`]'
        DELETE_CANCEL='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Cancel"`]'
        DELETE_CODE="""by.xpath|//XCUIElementTypeStaticText[@name="Note: You can also check the junk and spam folders if you can't receive the email."]/../following-sibling::XCUIElementTypeOther[1]"""
        VERIFICATION='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Verification"`]'
        DELETE_RESEND_CODE='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Resend code"`]'
        CANT_RECEIVE_EMAIL="""by.ios_class_chain|**/XCUIElementTypeButton[`label == "I can't receive the email."`][1]"""
        DELETE_PROCESS='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Deleting Account"`][2]'
        DELETE_SUCCESS='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Account Deleted Successfully"`]'
        DELETE_EXIT='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Exit"`]'
        # user 首页
        USER_NAME = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "$replace"`]'
        USER_DETAIL='by.xpath|(//XCUIElementTypeOther[@name="Integration"])[1]/preceding-sibling::XCUIElementTypeCell'
        # user 详情
        ACCOUNT_TITLE='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Account"`]'
        CHANGE_PWD='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Password"`]'
        NICK_NAME='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Nickname"`]'
        INPUT_NICK="by.ios_predicate|type='XCUIElementTypeTextField'"
        SAVE_NICK='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Save"`]'
        CHANGE_EMAIL='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Email"`]'
        LOG_OUT = 'by.ios_predicate|label == "Log out"'
        CONFIRM_LOG_OUT = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "Log out"`]'
        CANCEL_LOG_OUT = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "Cancel"`]'
        # 修改邮箱
        CHANGE_EMAIL_TITLE='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Change Email"`]'
        CHANGE_EMAIL_PWD="by.ios_predicate|type='XCUIElementTypeSecureTextField'"
        CHANGE_NEW_EMAIL='by.ios_class_chain|**/XCUIElementTypeTextField[`value == "Enter your email address"`]'
        CHANGE_EMAIL_NEXT='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Next"`]'
        CHANGE_EMAIL_SUCCESS='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Account Email Changed!"`]'
        CHANGE_EMAIL_LOGIN='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Log in"`]'
        # 修改密码
        CHANGE_PASSWORD_TITLE='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Change Password"`]'
        CHANGE_PASSWORD_SUBMIT='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Submit"`]'
        CREATE_NEW_ACCOUNT='by.ios_class_chain|**/XCUIElementTypeLink[`label == "go to create a new account"`]'
        CHANGE_PASSWORD_CODE="""by.xpath|//XCUIElementTypeStaticText[@name="We just sent you a confirmation code via email to help reset your password. Check your junk folder if you didn't receive it."]/following-sibling::XCUIElementTypeOther"""
        CHANGE_PASSWORD_NEXT='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Next"`]'
        CHANGE_PASSWORD_ENTER_CODE='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Enter Code"`]'
        CHANGE_PASSWORD_RESEND_CODE='by.ios_class_chain|**/XCUIElementTypeLink[`label == "Resend code"`]'
        CHANGE_PASSWORD_STILL_NOT_RECEIVE='by.ios_class_chain|**/XCUIElementTypeLink[`label == "Still not receive?"`]'
        CHANGE_PASSWORD_RESET_PASSWORD='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Reset Password"`]'
        CHANGE_PASSWORD_NEW_PWD='by.ios_predicate|type="XCUIElementTypeSecureTextField"'
        CHANGE_PASSWORD_RESET_SUBMIT='by.ios_class_chain|**/XCUIElementTypeButton[`label == "Submit"`]'
        CHANGE_PASSWORD_RESET_ACCOUNT_TITLE = f'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Reset Account"`]'
        CHANGE_PASSWORD_AGREE_RESET = f'by.ios_class_chain|**/XCUIElementTypeButton[`label == "Yes, I do."`]'
        CHANGE_PASSWORD_DISAGREE_RESET = f"""by.ios_class_chain|**/XCUIElementTypeButton[`label == "NO, I don't."`]"""
        CHANGE_PASSWORD_RESET_NEW_PWD = f'by.xpath|//XCUIElementTypeButton[@name="New password (6-32 characters):"]/following-sibling::XCUIElementTypeTextField'
        CHANGE_PASSWORD_RESET_CONFIRM_PWD = f'by.xpath|//XCUIElementTypeButton[@name="Confirm password (6-32 characters):"]/following-sibling::XCUIElementTypeTextField'
        CHANGE_PASSWORD_RESET_CONFIRM_BTN = f'by.ios_class_chain|**/XCUIElementTypeButton[`label == "Done"`]'
        CHANGE_PASSWORD_RESET_REFUSE = f"""by.ios_class_chain|**/XCUIElementTypeButton[`label == "NO, I don't."`]"""
        # 注册页面
        SIGN_UP_NAVI='by.ios_predicate|name == "Sign up" AND type == "XCUIElementTypeNavigationBar"'
        SIGN_UP_EMAIL='by.ios_predicate|type == "XCUIElementTypeTextField"'
        SIGN_UP_PWD='by.ios_predicate|type == "XCUIElementTypeSecureTextField"'
        AGREE_SIGN= """by.xpath|(//XCUIElementTypeButton[@name="I agree to ${app}'s Terms of use and Privacy policy."])[1]/following-sibling::XCUIElementTypeButton"""
        SIGNUP_BT='by.ios_predicate|label == "Sign up" AND name == "Sign up" AND type == "XCUIElementTypeButton"'
        REGISTERED='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Already registered."`]'
        REGISTERED_LOGIN='by.ios_predicate|label == "Log in"'
        INVALID_EMAIL='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Invalid email address."`]'
        # integration
        INTEGRATION_ALEXA='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Amazon Alexa"`]'
        LINK_WITH_ALEXA_ALLOW='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Allow"`]'
        INTEGRATION_GOOGLE='by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Google Assistant"`]'
    else:
        logger.error(f"client异常：{Set.client}")
