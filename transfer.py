import json
import socket
from config import *


class Transfer:
    def __init__(self, s_host, s_port=6666):
        self._server_host = s_host
        self._server_port = s_port

    def msgSender(self, msg):
        s = socket.socket()
        s.connect((self._server_host, self._server_port))
        s.send(bytes(json.dumps(msg), encoding="utf-8")+MESSAGE_OVER_SIGN)
        s.close()
        return True
