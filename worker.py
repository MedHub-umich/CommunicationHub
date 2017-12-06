from threading import *
import requests


class worker(Thread):
    def __init__(self, host, postdata):
        Thread.__init__(self)
        self.host = host
        self.json = postdata
        self.start()

    def run(self):
        requests.post(self.host, json=self.json)