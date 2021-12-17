import os
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



class Emailer:
  host = 'smtp.gmail.com'
  port = 587
  username = '' # email
  password = '' # password
  from_email = f'Python Mail<{username}>'
  subject = ''
  text = None
  context = {}
  to_emails = []
  test_send = False
  has_html = False
  template_html = None
  template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')


  def __init__(self, subject='', text=None, context={}, to_emails=None, template_html=None, test_send=False, *args, **kwargs):
    assert isinstance(to_emails, list)
    self.subject = subject
    self.context = context
    self.to_emails = to_emails
    self.test_send = test_send
    self.text = text
    if template_html != None:
      self.template_html = template_html
      self.has_html = True

  def format_msg(self):
    msg = MIMEMultipart('alternative')
    msg['From'] = self.from_email
    msg['To'] = ', '.join(self.to_emails)
    msg['Subject'] = self.subject
    if self.text != None:
      txt_part = MIMEText(self.text, 'plain')
      msg.attach(txt_part)
    if self.template_html:
      self.template_path = os.path.join(self.template_path, self.template_html)
      if not os.path.exists(self.template_path):
        raise Exception('This path does not exist')
      template_string = ''
      with open(self.template_path, 'r') as f:
        template_string = f.read()
        template_string = template_string.format(**self.context)
    if self.template_html != None:
      html_part = MIMEText(template_string, 'html')
      msg.attach(html_part)
    msg_str = msg.as_string()
    return msg_str

  def send(self):
    msg = self.format_msg()
    did_send = False
    if not self.test_send:
      with smtplib.SMTP(host=self.host, port=self.port) as server:
        server.ehlo()
        server.starttls()
        server.login(self.username, self.password)
        try:
          server.sendmail(self.from_email, self.to_emails, msg)
          did_send = True
        except:
          did_send = False
    return did_send


obj = Emailer(subject='subject here', text='email body text here', template_html='template.html', context={'name': 'OSAMA'},  to_emails=['..........@gmail.com'],  test_send=False)
obj.send()