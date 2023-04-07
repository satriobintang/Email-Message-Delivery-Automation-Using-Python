#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#April 2023

import smtplib
import xlrd
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders

#Email Account Settings
email_sender = "emailaccount@gmail.com"
password_sender = "usepasswordfromapppasswordgoogle"

#Opening an Excel file with a list of email addresses
cwd = os.getcwd()
email_list = xlrd.open_workbook(f'{cwd}\email_account_recipient.xls')
sheet = email_list.sheet_by_index(0)

#Reading message from a text file
with open("message.txt", "r") as file:
    message = file.read()

#Sending an email to each email address on the list
for i in range(0, sheet.nrows):
    email_recipient = sheet.cell_value(i, 0)

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = "Important Message"

    # Adding text message to the email
    msg.attach(MIMEText(message))

    # Attach file fileimage.jpg
    filename = "fileimage.jpg"
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
    msg.attach(part)

    # Attach file filedocument.pdf
    filename = "filedocument.pdf"
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
    msg.attach(part)

    # Attach file fileexcel.xls
    filename = "fileexcel.xls"
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
    msg.attach(part)

    # Attach file filedoc.docx
    filename = "filedoc.docx"
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
    msg.attach(part)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_sender, password_sender)
        server.sendmail(email_sender, email_recipient, msg.as_string())
        print(f"Email sent successfully to {email_recipient}")
    except Exception as e:
        print(f"Failed to send email to {email_recipient}. Error: {str(e)}")
    finally:
        server.quit()