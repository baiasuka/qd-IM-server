# -*- coding: UTF-8 -*-
import asyncio
import json
import datetime

from handlers import MessageHandler
from config import *

message_handler = MessageHandler()

class ServerCore:
    def __init__(self, port=5001, limit=1024):
        self._port = port
        self._limit = limit

    @staticmethod
    async def msgHandler(reader, writer):
        """

        :param reader:
        :param writer:
        :return:
        """
        # 获取请求内容
        raw_data = await reader.readuntil(MESSAGE_OVER_SIGN)
        # 二进制转字符串
        recieved_msg = raw_data.decode("utf-8")[0:-7]
        # 字符串解析为字典
        request = json.loads(recieved_msg)
        response = message_handler.handle(request)
        response = json.dumps(response)
        writer.write(bytes(response, encoding="utf-8")+MESSAGE_OVER_SIGN)
        await writer.drain()

    async def main(self):
        """
        主运行函数
        :return:
        """
        print("qd-IM-server start")
        server = await asyncio.start_server(self.msgHandler,
                                            '0.0.0.0', self._port, limit=self._limit)
        addr = server.sockets[0].getsockname()
        with open('server_log.txt', 'a') as f:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(current_time+' 收到来自：'+str(addr)+'的连接\n')
        async with server:
            await server.serve_forever()
