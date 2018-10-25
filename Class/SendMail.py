import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendMail(object):
    def __init__(self, from_who, password, to, message):
        self.from_who = from_who
        self.password = password
        self.to = to
        self.message = message


    def send(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.from_who, self.password)
        msg = MIMEMultipart()
        msg['Subject'] = "Weather forecast"
        msg.attach(MIMEText(self.message, 'plain'))
        text = str(msg)
        server.sendmail("Weather App", self.to, text)
        server.quit()
