# import smtplib, ssl
# import datetime as dt
# import time

# sender_email = "mdsobahanmia1998@gmail.com"
# receiver_email = "jobayer.sikder.3032@gmail.com"
# password = "lpcx dgyb rzga cbym" 
# port = 587
# smtp_server = "smtp.gmail.com"

# message = '''\
# Subject: Request to Schedule an Appointment for Study visa

# Hello!! Brother'''

# context = ssl.create_default_context()

# try:
#     send_time = dt.datetime(2024, 6, 4, 00, 25, 00)
#     sleep_time = send_time.timestamp() - time.time()
    
#     if sleep_time > 0:
#         time.sleep(sleep_time)
    
#     with smtplib.SMTP(smtp_server, port) as email:
#         email.starttls(context=context)
#         email.login(sender_email, password)
#         email.sendmail(sender_email, receiver_email, message)
#         print('Email has been sent.')
# except Exception as e:
#     print(f'An error occurred: {e}')


import smtplib, ssl
import datetime as dt
import time
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender_email = 'mdsobahanmia1998@gmail.com'
receiver_email = 'visa_newdelhi@mvz.cz'
password = "lpcx dgyb rzga cbym"
port = 587
smtp_server = 'smtp.gmail.com'

# Email subject and body
subject = "Request for Appointment: John Doe"
body = '''\


Hello!! Brother!
attached my Documents'''

# Path to the PDF file
pdf_file_paths = ['Offer_letter.pdf', 'Passport_Scan.pdf']

# Create a multipart message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Attach the body with the msg instance
message.attach(MIMEText(body, 'plain'))

# Open the file in binary mode
for pdf_file_path in pdf_file_paths:
    try:
        # Open the file in binary mode
        with open(pdf_file_path, 'rb') as attachment:
            # Instance of MIMEBase and named as part
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(pdf_file_path)}')
            message.attach(part)
    except FileNotFoundError:
        print(f"The file {pdf_file_path} was not found.")
        continue  # Skip to the next file if the current file is not found

context = ssl.create_default_context()

try:
    send_time = dt.datetime(2024, 6, 4, 1, 17, 00)
    sleep_time = send_time.timestamp() - time.time()
    
    if sleep_time > 0:
        time.sleep(sleep_time)
    
    with smtplib.SMTP(smtp_server, port) as email:
        email.starttls(context=context)
        email.login(sender_email, password)
        email.sendmail(sender_email, receiver_email, message.as_string())
        print('Email has been sent.')
except Exception as e:
    print(f'An error occurred: {e}')



