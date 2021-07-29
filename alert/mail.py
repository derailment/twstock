import smtplib
from email.message import EmailMessage

dir='/home/ubuntu/twstock/'

class Mail:
    smtp=smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    f = open(dir+'google.secret')
    def send(self, content):
        
        secret = self.f.readlines()
        my_addr = secret[0].rstrip('\n')
        my_password = secret[1].rstrip('\n')
        
        self.smtp.login(my_addr,my_password)
        from_addr=my_addr
        to_addr=my_addr

        msg = EmailMessage()
        msg['Subject'] = "TWSTOCK Alert"
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg.set_content(content)
        
        status=self.smtp.send_message(msg)
        if status=={}:
            print("Successfully sent the mail!")
        else:
            print("Failed to send the mail!")
        self.smtp.quit()
