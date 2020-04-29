"""
python发送smtp邮件
Time: 2020/4/27 9:49
Author: chengyao
Email: chengy_work@163.com
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from log.log import Log
from config.settings import SEND_ADDR, SMTP_PORT, SMTP_SERVER, SUBJECT, PASSWORD, FROM_ADDR

log = Log(__name__).getlog()


class Mailer:
    def __init__(self):
        self.msg_from = FROM_ADDR  # 发件人邮箱
        self.passwd = PASSWORD  # 授权码
        self.smtp_server = SMTP_SERVER  # 邮件服务提供商
        self.smtp_port = SMTP_PORT  # 邮件服务端口
        self.msg_to = SEND_ADDR  # 接收邮件的人（可以是列表）
        self.subject = SUBJECT  # 邮件主题
        self.content = None  # 邮件内容

    def sendemail(self):
        """
        发送email
        :return:
        """
        msg = MIMEText(self.content, 'plain', 'utf-8')  # 生成一个MIMEText对象（还有一些其它参数）
        msg['Subject'] = Header(self.subject, 'utf-8')  # 放入邮件主题
        msg['From'] = Header("SHV网站监控", 'utf-8')  # 放入发件人称呼
        try:
            server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)  # 通过ssl方式发送，服务器地址，端口
            # server.set_debuglevel(1)# 调试等级
            server.login(self.msg_from, self.passwd)  # 登录到邮箱
            server.sendmail(self.msg_from, self.msg_to, msg.as_string())  # 发送邮件：发送方，收件方，要发送的消息
            log.info("向{}发送邮件成功".format(self.msg_to))
        except server.SMTPException as ex:
            log.error(ex)
        finally:
            server.quit()
