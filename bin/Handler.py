#!/usr/bin/env python
import Queue
import threading
import time

from bin.EmailHandler import EmailHandler
from bin.RequestHandler import RequestHandler

email_handler = EmailHandler()
request_handler = RequestHandler()


queue = Queue.Queue()

votes = 0


class CheckMail(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        if queue.qsize() > 0:
            md5_email = queue.get()
            if md5_email:
                activation_url = request_handler.get_activation_url(md5_email)
                if activation_url:
                    request_handler.send_get_request(activation_url)
                    global votes
                    votes += 1
                else:
                    queue.put(md5_email)


class CreateMail(threading.Thread):
    def __init__(self, user_id):
        threading.Thread.__init__(self)
        self.user_id = user_id

    def run(self):
        if queue.qsize() < 100:
            email_blob = email_handler.generate_mail_id()
            md5_email = email_blob[1]
            email = email_blob[0]
            request_handler.vote(email, self.user_id)

            queue.put(md5_email)


class MainFactory:
    def __init__(self):
        pass

    @staticmethod
    def run(user_id):
        while True:
            p = CreateMail(user_id)
            p.setDaemon(True)
            p.start()

            time.sleep(0.3)  # To prevent to much load.

            t = CheckMail()
            t.setDaemon(True)
            t.start()

            print 'Total votes succeeded: {0}'.format(votes)

            time.sleep(0.3)



