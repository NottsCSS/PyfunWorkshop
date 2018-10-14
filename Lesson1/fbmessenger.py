# Docs: https://fbchat.readthedocs.io/en/master/api.html

from fbchat import Client, Message
import getpass

email = input("input your email:")
password = getpass.getpass()
client = Client(email, password)

for i in range(0,10):
    # user = client.searchForUsers("alphonsuschen", limit=1)
    # user = user[0]
    client.send(Message(text="Lol Im spamming myself lol."), thread_id=client.uid)
client.logout()
