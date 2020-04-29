"""
云片网提供的SDK，用于发送短信
Time: 2020/4/27 11:08
Author: chengyao
Email: chengy_work@163.com
"""
from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient
from config.settings import APIKEY, SMS_SIGNATURE, MOBILES, SMS_TEMPLATE
from log.log import Log

log = Log(__name__).getlog()


class SMS:
    """
    云片SDK，利用restful风格进行封装，方便调用和维护
    """

    def __init__(self):
        self.key = APIKEY  # 云片key
        self.clnt = YunpianClient(self.key)
        self.mobile_list = MOBILES  # 收信人手机号（列表）
        self.mobile = None
        self.content = SMS_TEMPLATE  # 短信主体内容
        self.signature = SMS_SIGNATURE  # 短信签名

    def sendSMS(self):
        """
        发送短信
        :return:
        """
        content = self.signature + self.content
        for item in self.mobile_list:
            if item != "":
                self.mobile = item
                param = {YC.MOBILE: self.mobile, YC.TEXT: content}
                try:
                    r = self.clnt.sms().single_send(param)
                    log.info(r.msg())
                except Exception as ex:
                    log.error(ex)
# 获取返回结果, 返回码:r.code(),返回码描述:r.msg(),API结果:r.data(),其他说明:r.detail(),调用异常:r.exception()
# 短信:clnt.sms() 账户:clnt.user() 签名:clnt.sign() 模版:clnt.tpl() 语音:clnt.voice() 流量:clnt.flow()
