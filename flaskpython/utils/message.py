from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def sendermessage(config_data,receiver,title,note):
 try:
   msg=MIMEMultipart()
   msg['Subject']=Header(title,'utf-8')
   msg["From"] = config_data['sender_email']
   msg["To"] = Header(receiver,"utf-8")

   msg.attach(MIMEText(note,'plain','utf-8'))

   smtp=SMTP_SSL(config_data['host_server'])
   smtp.login(config_data['sender_email'],config_data['pwd'])
   smtp.sendmail(config_data['sender_email'],receiver,msg.as_string())
   smtp.quit()
   return True
 except:
   return  False

def checkemilaccount(smtpservice,email,pwd):
   try:
     smtp = SMTP_SSL(smtpservice)
     smtp.login(email,pwd)
     return True

   except:
     return False






