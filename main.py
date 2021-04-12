import os
from twilio.rest import Client

client = Client(os.environ['account_sid'], os.environ['auth_token'])

# +14155238886 is the Twilio sandbox testing number

client.messages.create(body='Github Updated!',
                       from_='whatsapp:+14155238886',
                       to='whatsapp:'+os.environ['contact_no'])

print(message.sid)
