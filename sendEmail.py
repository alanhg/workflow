"""
给目标邮箱地址发送邮件
"""
from email.header import Header
from email.mime.text import MIMEText

import smtplib


class EMailSender(object):


    def send(self,content):
        sender = 'i@alanhe.me'
        receivers = ['qianghe421@163.com']  # 接收邮件

        message = MIMEText(content, 'html', 'utf-8')
        message['From'] = Header("Alan", 'utf-8')
        message['To'] = Header("Alan He", 'utf-8')

        subject = '定期发送报告'
        message['Subject'] = Header(subject, 'utf-8')

        mail_host = "mail.alanhe.me"  # 设置服务器
        mail_user = sender  # 用户名
        mail_pass = "alanhe"  # 口令

        try:
            server = smtplib.SMTP()
            server.connect(mail_host, 25) # 25 为 SMTP 端口号
            server.set_debuglevel(1)
            server.login(mail_user, mail_pass)
            server.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
            server.close()
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


sender=EMailSender()
sender.send("<h1>hello world</h1>")
