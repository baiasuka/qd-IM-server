import json
import socket
from config import *


class Transfer:
    def __init__(self, target_host, target_port=6666):
        self._target_host = target_host
        self._target_port = target_port

    def msgSender(self, msg):
        s = socket.socket()
        s.connect((self._target_host, self._target_port))
        s.send(bytes(json.dumps(msg), encoding="utf-8")+MESSAGE_OVER_SIGN)
        s.close()
        return True
