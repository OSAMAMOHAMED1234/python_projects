import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = '' # email
password = '' # password

def send_mail(text='Python body', subject='Python subject', from_email=f'Python Mail<{username}>', to_emails=None, html=None):
  host = 'smtp.gmail.com'
  port = 587
  assert isinstance(to_emails, list)
  msg = MIMEMultipart('alternative')
  msg['From'] = from_email
  msg['To'] = ', '.join(to_emails)
  msg['Subject'] = subject
  txt_part = MIMEText(text, 'plain')
  msg.attach(txt_part)
  if html != None:
    html_part = MIMEText(html, 'html')
    msg.attach(html_part)
  msg_str = msg.as_string()
  server = smtplib.SMTP(host=host, port=port)
  server.ehlo()
  server.starttls()
  server.login(username, password)
  server.sendmail(from_email, to_emails, msg_str)
  server.quit()


send_mail(subject='subject here', text='email body text here',  to_emails=['..........@gmail.com'])