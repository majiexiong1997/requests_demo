import base64
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from config import getpathinfo
import runner
msg_from = '1455080341@qq.com'  # 发送方邮箱
passwd = 'zzocwflwjavqigjc'  # 填入发送方邮箱的授权码
msg_to = '1455080341@qq.com'  # 收件人邮箱

subject = "接口自动化测试结果"  # 主题
content = "附件为接口自动化测试结果"

txt_path = getpathinfo.get_result_path()[0]
report_path = getpathinfo.get_result_path()[1]
msg = MIMEText(content,_charset='utf-8')


msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com".encode(), 465) # 邮件服务器及端口号
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print("发送成功")

except Exception as e:
    print("发送失败")
finally:
    s.quit()


