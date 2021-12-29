import json
import os
from getpass import getpass
from twilio.rest import Client

twilio_sid = '' # https://www.twilio.com/console/projects/summary
twilio_secret = ''

# # set creds
# reset_creds = False
# if reset_creds:
#   twilio_sid = getpass("What's the Twilio Account SID?")
#   twilio_secret = getpass("What's the Twilio Secret?")
#   data = {
#     'twilio_sid': twilio_sid,
#     'twilio_secret': twilio_secret
#   }
#   json_data = json.dumps(data)
#   with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'creds.json'), 'w') as f:
#     f.write(json_data)

# # get creds
# with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'creds.json'), 'r') as f:
#   raw_data = f.read()
#   cred_data = json.loads(raw_data)
#   twilio_sid = cred_data.get('twilio_sid')
#   twilio_secret = cred_data.get('twilio_secret')


client = Client(twilio_sid, twilio_secret)
my_number = ''
to_number = ''
body = 'Hi OSAMA\nThis message was sent from Python Programming script \nBy: OSAMA \nPython Developer :)'
message_twilio = client.messages.create(
  body=body,
  from_=my_number,
  to=to_number
)


# get message details
msg_sid = message_twilio.sid
msg_ctx = client.messages.get(msg_sid)
msg_instance = msg_ctx.fetch()
print(msg_sid, msg_instance.from_, msg_instance.body, msg_instance.to)


ignore_numbers = []
# get list of sent messages
messages = client.messages.list(limit=20)#, to=to_number)
for i, record in enumerate(messages):
  from_ = record.from_
  to = record.to
  if from_ in ignore_numbers:
    from_ = '~hidden~'
  if to in ignore_numbers:
    to = '~hidden~'
  from_me = False
  if from_ == my_number:
    from_me = True
  print(i, record.body, to, from_, from_me)