# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1.��������
smtpsever = "smtp.qq.com"
port = 465
sender = "283340479@qq.com"
psw = "��Ȩ��"
# receiver = ["283340479@qq.com"]  # �����ռ���

# ����ռ���
receiver = ["283340479@qq.com","1942875703@qq.com","247869184@qq.com","1165219980@qq.com"]

# ��д��ģ��
msg = MIMEMultipart()
msg['Subject'] = "�ʼ�������"
msg['From'] = sender
msg['To'] = ";".join(receiver)         # str

f = open("result.html", encoding="utf-8")
mail_body = f.read()
f.close()

# �Ӹ���
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename= "result.html"'
msg.attach(att)

# ������
body = MIMEText(mail_body, 'html', 'utf-8')
msg.attach(body)


# 3.д�ŵ�����
smtp = smtplib.SMTP_SSL(smtpsever,port)  # ��Ȩ���¼
smtp.login(sender,psw)
smtp.sendmail(sender,receiver, msg.as_string())
smtp.quit()


# -------�˺������¼----------------------
# smtp = smtplib.SMTP()
# smtp.connect(smtpsever,port)
# smtp.login(sender,psw)
# smtp.sendmail(sender,receiver, msg.as_string())
# smtp.quit()


