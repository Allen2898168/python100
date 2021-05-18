"""
    python笔记3
    发送smtplib邮件
"""

# coding:utf-8
import smtplib
from email.mime.text import MIMEText

smtpserver = "smtp.qq.com"
port = 465
sender = "283340479@qq.com"
psw = "**************"
receiver = "283340479@qq.com"

# ----------2.编辑邮件的内容------
subject = "这个是主题QQ"
body = '<p>这个是发送的QQ邮件</p>'
msg = MIMEText(body, "html", "utf-8")
msg['from'] = sender
msg['to'] = "283340479@qq.com"
msg['subject'] = subject

# ----------3.发送邮件------
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver)
smtp = smtplib.SMTP_SSL(smtpserver, port)
smtp.login(sender, psw)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()