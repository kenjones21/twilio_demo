from twilio.rest import Client

account_sid = 'AC579770ddf5d399394b9f93fd11612af6'
auth_token = '29d981b78d85e34b5b9b14ccf01596a2'

client = Client(account_sid, auth_token)

call = client.calls.create(
    url='http://demo.twilio.com/docs/voice.xml',
    to='+12674213214',
    from_='+12528882553'
)

print(call.sid)