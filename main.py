import os
from twilio.rest import Client

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Yay! Push event triggered in master branch',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+6596669675']
                          )

print("Message ID:",message.sid)
