# 消息转发
import json
import socket
import config


class Transfer:
    """
    用于消息的即时转发
    """
    def __init__(self, target_host, target_port=config.CILENT_LISTENING_PORT):
        self._target_host = target_host
        self._target_port = target_port

    def msgSender(self, msg):
        s = socket.socket()
        s.connect((self._target_host, self._target_port))
        s.send(bytes(json.dumps(msg), encoding="utf-8")+config.MESSAGE_OVER_SIGN)
        s.close()
        return True