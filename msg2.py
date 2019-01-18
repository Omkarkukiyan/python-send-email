#Adding Attachments Using the email Package
#The code below shows how to send an email with a PDF file as an attachment:

import email ,smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

subject = "An email send from sender_email"
body = "This is an email with an attachment from sender"
sender_email = "my_email@gmail.com"
receiver_email = "your_email@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart()
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email
message["Bcc"] = receiver_email  #Recommended for mass emails

message.attach(MIMEText(body, "plain"))

filename = "document.pdf"

with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content Disposition",
    f"attachment;filename={filename}"
)

message.attach(part)
text = message.as_string()

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())