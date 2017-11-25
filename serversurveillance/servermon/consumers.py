from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from .models import Server

def ws_connect(message):
    # queryset = list(Server.objects.values_list('ip'))
    # client_ip = message.content['client'][0]
    # if client_ip in queryset:
        # print("naa")
    # else:
        # print("Registering %s" %(client_ip) )
        # Server(ip=client_ip
    print(message.reply_channel)
    message.reply_channel.send({"accept": True})
    

# Connected to websocket.receive
def ws_message(message):

    queryset = list(Server.objects.values_list('ip'))
    data_list = message.content['text'].split(",")
    client_os = ""
    client_ip = ""
    hostname = ""
    for data in data_list:
        key = data.split(":")[0]
        value = data.split(":")[-1]
        # print(key)
        if key == "os":
            client_os = value
        elif key == "hostname":
            hostname = value
        elif key == 'ip':
            client_ip = value
    # endfor
    registered_ips = (str(queryset)
                        .replace("[","")
                        .replace("'","")
                        .replace("]","")
                        .replace("(","")
                        .replace(",), ",",")
                        .replace(",)","")).split(",")

    if client_ip in registered_ips:
        print("naa")
    else:
        print("Registering %s" %(client_ip) )
        s1 = Server(ip=client_ip,
                    processor="Intel(R) Core(TM) i5-3320M CPU @ 2.60GHz",
                    memory="8.00 GB",
                    arch="64-bit Operating System, x64 Based Processor",
                    mac="84-3A-4B-77-B0-D0",
                    os=client_os,
                    name=hostname,
                    channel_reply=message.reply_channel)
        s1.save()
        
    print('ws_message ' + message.content['text'])
    message.reply_channel.send({
        "text": "YOLO",
    })


# Connected to websocket.disconnect
def ws_disconnect(message):
    print('sulodz disconnect')
    # Group("chat").discard(message.reply_channel)