import time

import requests


class ProtobufInterFace(object):
    def __init__(self,url,userid,token,**kwargs):
        self.url = url
        self.userid = userid
        self.token = token

        self.session = requests.Session()

        self.event = None



        start_time = time.time()
    def close(self):
        self.session.close()