import zmail
import re
from Common.data_deal import DataDeal
from Common.log import logger
import time
from datetime import datetime


class GetCode:
    @staticmethod
    def get_code(use='forgot_pwd'):
        email_info = DataDeal.get_email()
        logger.debug("开始获取验证码")
        if use == 'forgot_pwd' or use == 'change_pwd':
            server = zmail.server(email_info['email'], email_info["pwd"])
        elif use == 'del_user' or use == 'change_email':
            server = zmail.server(email_info['del_email'], email_info["del_pwd"])
        else:
            logger.error('use error')
        time.sleep(30)
        try:
            while True:
                latest_mail = server.get_latest()
                if latest_mail["from"].find("meross.com") != -1 or latest_mail["from"].find("refoss.net") != -1:  #兼容refoss的邮件发送地址
                    content_html = latest_mail["content_html"]
                    date = latest_mail["date"]
                    now_time = datetime.utcnow()
                    dd = (now_time.replace(tzinfo=None) - date.replace(tzinfo=None)).seconds / 60
                    if -3 <= dd <= 3:
                        dr = re.compile(r'<[^>]+>', re.S)
                        mail = dr.sub('', str(content_html))
                        mail = mail.replace(r'\r', '')
                        mail = mail.replace(r'\n', '')
                        locate = mail.find('Note: The code will expire in 24 hours.')
                        if locate != -1:
                            server.delete(latest_mail["Id"])
                            code = mail[locate - 6:locate]
                            logger.debug(f"删除验证码邮件并成功获取验证码:{code}")
                            return code
                        else:
                            logger.debug(f'邮件信息:{mail}')
                    else:
                        logger.debug(f'删除过时邮件{latest_mail["Id"]}')
                        server.delete(latest_mail["Id"])

        except BaseException as e:
            pass
            time.sleep(2)
            logger.info(e)


if __name__ == '__main__':
    a = GetCode.get_code('change_pwd')
    print(a)
