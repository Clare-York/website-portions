"""
配置文件
Time: 2020/4/27 10:22
Author: chengyao
Email: chengy_work@163.com
"""
# 监控信息配置
# 监控站点,str类型,以,分割在列表中填入
WEBSITES = [
    "www.mucheng.im",  # 测试网址,响应200
    "demo.mucheng.im",  # 测试网址,响应403
]

# 日志信息配置
# 日志名
LOG_NAME = "网站异常监控日志"

# 邮件信息配置
# 发送方邮箱
FROM_ADDR = "example@qq.com"

# 邮箱密码（授权码）
PASSWORD = "example"

# 邮箱服务提供方
SMTP_SERVER = "smtp.qq.com"

# 邮箱端口
SMTP_PORT = 465

# 接收邮件的邮箱地址,str类型,以,分割在列表中填入
SEND_ADDR = [
    'example@foxmail.com',  # cy的个人邮箱
]

# 邮件主题
SUBJECT = "网站异常信息报警"

# 邮件信息模板
EMAIL_TEMPLATE = "您监控的站点{} 有异常，异常信息：{}，请及时处理!"

# 短信通知配置
# 云片KEY
APIKEY = "example"

# 签名
SMS_SIGNATURE = "【example】"

# 收信人手机号,str类型,以,分割在列表中填入
MOBILES = [
    '18********6',
]

# 短信模板（固定,因带变量的通知类短信都需要和云片商务经理沟通）
SMS_TEMPLATE = "您好，您关注的站点有了新的变化，请前往邮箱查看！"
