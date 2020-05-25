from twilio.rest import Client

account_sid = '[enter the id]'
auth_token = '[enter the auth token]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='[enter the senders number]',
    body='this was send using python',
    to='[enter the receivers number]'
)

print(message.sid)
