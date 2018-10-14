# Docs: https://fbchat.readthedocs.io/en/master/api.html
from threading import Thread
import getpass

from fbchat import Client, Message, ThreadType
from win10toast import ToastNotifier


class CustomClient(Client):
    def __init__(self, *args, **kwargs):
        super(CustomClient, self).__init__(args, kwargs)
        self.notifier = ToastNotifier()

    def onMessage(self, mid=None, author_id=None,
                  message=None, message_object=None,
                  thread_id=None, thread_type=ThreadType.USER,
                  ts=None, metadata=None, msg=None):
        thread_obj = self.fetchThreadInfo(thread_id)[str(thread_id)]
        print(f"{thread_obj.name}({thread_obj.last_message_timestamp}) : {message}")
        self.notifier.show_toast(
            f"{thread_obj.name}({thread_obj.last_message_timestamp})",
            message,
            icon_path=None,
            duration=5,
            threaded=True
        )


email = input("input your email:")
password = getpass.getpass()
client = CustomClient(email, password)
