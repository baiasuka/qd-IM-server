import asyncio
import json

from transfer import Transfer


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
