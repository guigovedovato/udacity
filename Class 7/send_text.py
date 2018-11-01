from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb9102aa1bbcc3ec28d6681068e25a977"
# Your Auth Token from twilio.com/console
auth_token  = "e199053a4e335694a43d832487eb3b47"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+353838930055", 
    from_="+353768888623",
    body="Hello, just test my code")

print(message.sid)
