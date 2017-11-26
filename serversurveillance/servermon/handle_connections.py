# handle_connections.py
# check if machine is already registered

import json
from .models import Server
from django.core.exceptions import ObjectDoesNotExist

def is_registered(ipaddress):
    print("Checking %s"%ipaddress)

def register(message):
    server_data_json = json.loads(message.content['text'].replace("'", "\""))
    
    obj, created = Server.objects.update_or_create(
        ipaddress=server_data_json['ipaddress'],
         defaults={ 'channel_reply':message.reply_channel,
                    'mac':server_data_json['mac'],
                    'system':server_data_json['system'],
                    'arch':server_data_json['arch'],
                    'memory':server_data_json['memory'],
                    'processor':server_data_json['processor'],
                    'name':server_data_json['name'],
                  },
    )
    
    print(created)

def unregister(channel_reply):
    channel = Server.objects.get(channel_reply__exact=channel_reply)
    channel.delete()