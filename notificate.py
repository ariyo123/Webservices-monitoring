
from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

app = Flask(__name__)

def send_test_mail(body):
    sender_email = "aomolade@gmail.com.ng"
    receiver_email = "aomolade@gmail.com.ng"

    msg = MIMEMultipart()
    msg['Subject'] = '[Email Test]'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msgText = MIMEText('<b>%s</b>' % (body), 'html')
    msg.attach(msgText)

    filename = "status.csv"
    msg.attach(MIMEText(open(filename).read()))

    with open('status.csv', 'rb') as fp:
        img = fp.read()
        img.add_header('Content-Disposition', 'attachment', filename="status.csv")
        msg.attach(img)
        
    pdf = MIMEApplication(open("status.csv", 'rb').read())
    pdf.add_header ('Content-disposition', 'attachment', filename=('utf-8','',status.csv'))
    #msg.add_header('content-disposition', 'attachment',
    msg.attach(csv)

    try:
        with smtplib.SMTP('smtp.office365.com', 587) as smtpObj
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login("aomolade@nibss-plc.com.ng", "Magfum12345@")
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Except
def hello_world():
    return "Hello world!"

if __name__ == "__main__":
    send_test_mail("Welcome to Medium!")
    app.run('0.0.0.0',port=5000)
