from twilio.rest import Client

account_sid = 'ACb440471d874f30b08a41f54fbdbda833'
auth_token = '8c11bc3f4854e8de0004f8c7f2fa117a'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12016902211',
                     to='+91 98690 28839'
                 )

print(message.sid)
