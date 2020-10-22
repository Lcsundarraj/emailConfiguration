"""
#This one not Working
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='malliksiddharth@gmail.com',
    to_emails='siddharthmallik404@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient('Enter api here')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr='malliksiddharth@gmail.com'
to_addr=['siddharthmallik404@gmail.com','lcsundarraj@gmail.com','priyankamahaku31@gmail.com']
msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
msg['subject']='hi how are you hope you fine'

body='hello world'

msg.attach(MIMEText(body,'plain'))

email=' '
password=' '

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('malliksiddharth@gmail.com','password')
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = 'Hello'
'''This is a test mail.
In this mail we are sending some attachments.
The mail is sent using Python SMTP library.
Thank You'''

#The mail addresses and password
sender_address = 'malliksiddharth@gmail.com'
sender_pass = 'password'
receiver_address = 'siddharthmallik404@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'
#The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'file.pdf'
attach_file = open('file.pdf', 'rb') # Open the file as binary mode
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) #encode the attachment
#add payload header with filename
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')



import yagmail

receiver = "siddharthmallik404@gmail.com"
body = "Hello there from Yagmail"
filename = "file.pdf"

yag = yagmail.SMTP("malliksiddharth@gmail.com")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body, 
    attachments=filename,
)

"""





import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_mail(email_info):
    print("entering to send mail module")
    sender_email = email_info['sender']
    receiver_email = email_info['receiver']
    password = input("Type your password and press enter:")
    message = MIMEMultipart("alternative")
    message["Subject"] = email_info['sub']
    message["From"] = sender_email
    message["To"] = receiver_email
    # Create the plain-text and HTML version of your message
    text = email_info['Message']
    html = home.html
    

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


