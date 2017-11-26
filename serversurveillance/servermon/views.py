from django.shortcuts import render
from .models import Server
import redis
from channels.channel import Channel

redis_conn = redis.Redis("localhost", 6379)

def server_list(request):
    queryset = Server.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'servermon/index.html', context)

def server_details(request):
    if request.method == 'GET':
            server_id = request.GET['server_id']
    
    queryset = Server.objects.filter(id=server_id)
    context = {
        'object_list': queryset
    }
    return render(request, 'servermon/server_details.html', context)
    
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
    return render(request, 'servermon/terminal.html', context)
