from django.shortcuts import render
from channels.channel import Channel
from .search import *
from .models import Server
import redis
import json

redis_conn = redis.Redis("localhost", 6379)

def server_list(request):
    
    queryset = Server.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'index.html', context)

def server_details(request):
    if request.method == 'GET':
            server_id = request.GET['server_id']
    
    queryset = Server.objects.filter(id=server_id)
    softwares = json.loads(str(queryset.values_list('softwares', flat=True)[0]).replace("'", "\""))
    software_list = []
    for key in softwares:
        software_list.append("%s %s"%(key,softwares[key]))
    context = {
        'object_list': queryset,
        'software_list': software_list
    }
    return render(request, 'server_details.html', context)
    
def terminal(request):
    if request.method == 'POST':
        command = request.POST['command']
        server_id = request.POST['server_id']
    print(server_id)
    print(command)

    # get the reply channel
    channel_reply = Server.objects.filter(id=server_id).values('channel_reply')[0]['channel_reply']
    print('from views ' + channel_reply)
    Channel(channel_reply).send({ "text": command})
    
    context = {
        'object_list': 'abc'
    }
    return render(request, 'terminal.html', context)
    
def search(request):
    
    queryset = Server.objects.all()
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['name', 'ipaddress',])
        found_entries = Server.objects.filter(entry_query)
        queryset = found_entries
    context = {
        'object_list': queryset
    }
    return render(request, 'search.html', context)
