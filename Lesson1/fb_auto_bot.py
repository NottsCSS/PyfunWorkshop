# Docs: https://fbchat.readthedocs.io/en/master/api.html
from threading import Thread
import getpass
import sys

from fbchat import Client, Message, ThreadType
from win10toast import ToastNotifier


class CustomClient(Client):
    def __init__(self, email, password):
        super(CustomClient, self).__init__(email=email, password=password)
        self.notifier = ToastNotifier()

    def onMessage(self, mid=None, author_id=None,
                  message=None, message_object=None,
                  thread_id=None, thread_type=ThreadType.USER,
                  ts=None, metadata=None, msg=None):
        thread_obj = self.fetchThreadInfo(thread_id)[str(thread_id)]
        if(thread_obj.name != "Inbox event"):
            if(thread_obj.name == "Chen Wen Kang"):
                thread_obj.name = "Probably Myself"
            if(thread_obj.name == "Jun Lin"):
                # Do anything you want here with the information, 
                # you can reply to user if you know it's your friend.
                thread_obj.name = "RoomMate Jun Lin" 
            print(f"{thread_obj.name} : {message}")
            self.notifier.show_toast(
                thread_obj.name,
                message,
                icon_path=None,
                duration=5,
                threaded=True
            )


email = input("input your email:")
password = getpass.getpass()
client = CustomClient(email, password)
try:
    client.listen()
except KeyboardInterrupt:
    client.logout()
    sys.exit(1)
    print("exit!")
