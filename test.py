import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def send_mail(email_info):
    subject = email_info['sub']
    body = email_info['Message']
    sender_email = email_info['sender']
    receiver_email = email_info['receiver']
    bcc_email = email_info['bcc']
    password = ("Type your password and press enter:")

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # message["Bcc"] = bcc_email  # Recommended for mass emails
    # message["body"]='Subject: {}\n\n{}'.format(subject, body)
    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # filename = "file.pdf"  # In same directory as script

    # # Open PDF file in binary mode
    # with open(filename, "rb") as attachment:
    #     # Add file as application/octet-stream
    #     # Email client can usually download this automatically as attachment
    #     part = MIMEBase("application", "octet-stream")
    #     part.set_payload(attachment.read())

    # # Encode file in ASCII characters to send by email    
    # encoders.encode_base64(part)

    # # Add header as key/value pair to attachment part
    # part.add_header(
    #     "Content-Disposition",
    #     f"attachment; filename= {filename}",
    # )

    # # Add attachment to message and convert message to string
    # message.attach(part)
    # text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, body)
