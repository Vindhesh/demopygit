from twilio.rest import Client
import requests
account_sid = 'ACb440471d874f30b08a41f54fbdbda833'
auth_token = '8c11bc3f4854e8de0004f8c7f2fa117a'
client = Client(account_sid, auth_token)
r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()
number_iss = people['number']
Message = 'Hi Fun fact,Number of people in space right now is '+str(number_iss)
#formulate the message that will be sent
message = client.messages.create(to="+919869028839", from_="+919869028839", body=Message)
print(message.sid)
