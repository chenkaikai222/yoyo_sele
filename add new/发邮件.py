# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1.参数配置
smtpsever = "smtp.qq.com"
port = 465
sender = "283340479@qq.com"
psw = "授权码"
# receiver = ["283340479@qq.com"]  # 单个收件人

# 多个收件人
receiver = ["283340479@qq.com","1942875703@qq.com","247869184@qq.com","1165219980@qq.com"]

# 建写信模板
msg = MIMEMultipart()
msg['Subject'] = "邮件的主题"
msg['From'] = sender
msg['To'] = ";".join(receiver)         # str

f = open("result.html", encoding="utf-8")
mail_body = f.read()
f.close()

# 加附件
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename= "result.html"'
msg.attach(att)

# 加正文
body = MIMEText(mail_body, 'html', 'utf-8')
msg.attach(body)


# 3.写信的流程
smtp = smtplib.SMTP_SSL(smtpsever,port)  # 授权码登录
smtp.login(sender,psw)
smtp.sendmail(sender,receiver, msg.as_string())
smtp.quit()


# -------账号密码登录----------------------
# smtp = smtplib.SMTP()
# smtp.connect(smtpsever,port)
# smtp.login(sender,psw)
# smtp.sendmail(sender,receiver, msg.as_string())
# smtp.quit()


