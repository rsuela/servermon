from django.http import HttpResponse
from channels.handler import AsgiHandler
from .handle_connections import register, unregister

def ws_connect(message):
    message.reply_channel.send({"accept": True}) # accept all connections

# Connected to websocket.receive
def ws_message(message):
    register(message)

    print('ws_message ' + message.content['text'])
    message.reply_channel.send({
        "text": "YOLO",
    })


# Connected to websocket.disconnect
def ws_disconnect(message):
    # must remove channel_reply
    unregister(message.reply_channel)
    # print(message.reply_channel)
    # Group("chat").discard(message.reply_channel)