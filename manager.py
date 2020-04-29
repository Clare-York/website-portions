"""
程序启动页
Time: 2020/4/27 9:05
Author: chengyao
Email: chengy_work@163.com
"""
import requests
from mail.py_email import Mailer
from sms.yunpianSMS import SMS
from config.settings import WEBSITES, EMAIL_TEMPLATE
from log.log import Log

email = Mailer()
sms = SMS()
log = Log(__name__).getlog()


def main():
    """
    程序入口
    :return:
    """
    for item in WEBSITES:
        url = "http://{}".format(item)
        response = requests.get(url)
        if response.status_code == 200:
            log.info("网站:{},正常".format(url))
            continue
        else:
            content = EMAIL_TEMPLATE.format(url, response.status_code)
            log.info(content)
            sendmsg(content)


def sendmsg(text):
    """
    发送邮件和短信的简单封装
    :param text: 邮件内容
    :return:
    """
    email.content = text
    email.sendemail()
    sms.sendSMS()


if __name__ == '__main__':
    main()
