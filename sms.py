import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="hey There I am Yash Dewangan",
                     from_='+12515640135',
                     to='+918602842290'
                 )

print(message.sid)