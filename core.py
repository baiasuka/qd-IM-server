# -*- coding: UTF-8 -*-
import asyncio
import json
import datetime

import config
from handler import MessageHandler


message_handler = MessageHandler()


class ServerCore:
    def __init__(self, port=config.SERVER_LISTENING_PORT, limit=config.SERVER_LISTENING_LIMIT):
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
        raw_data = await reader.readuntil(config.MESSAGE_OVER_SIGN)
        # 二进制转字符串
        recieved_msg = raw_data.decode("utf-8")[0:-7]
        # 字符串解析为字典
        request = json.loads(recieved_msg)
        response = message_handler.handle(request)
        response_json = json.dumps(response)
        writer.write(bytes(response_json, encoding="utf-8")+config.MESSAGE_OVER_SIGN)
        await writer.drain()

    async def main(self):
        """
        主运行函数
        :return:
        """
        print("IM-server start")
        server = await asyncio.start_server(self.msgHandler,
                                            '0.0.0.0', self._port, limit=self._limit)
        async with server:
            await server.serve_forever()
