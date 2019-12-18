import asyncio
import json

from transfer import Transfer


def test(params):
    """
    测试
    :param params:
    :return:
    """
    print(params["content"])
    return {"route": "/test", "data": "消息已收到"}


def user_send_to_user(params):
    """
    一对一发消息
    :param params:
    :return:
    """
    target_addr = params["target_addr"]
    content = params["content"]
    trans = Transfer(target_addr)
    result = trans.msgSender({
        "content": content
    })
    if result:
        return {"route": "/message/send", "data": "消息发送成功"}
    else:
        return {"route": "/message/send", "data": "消息发送失败"}


class MessageHandler:
    def parser(self, route):
        router = {
            "/test": test,
            "/message/send": user_send_to_user
        }
        return router[route]

    def handle(self, request):
        route = request["data"]["route"]
        func = self.parser(route)
        return func(request["data"])

