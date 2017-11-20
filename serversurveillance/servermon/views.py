from django.shortcuts import render
from .models import Server
import redis

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
        server_id = request.POST['command']
    print(server_id)
    # queryset = Server.objects.filter(id=server_id)
    # print(queryset)
    context = {
        'object_list': 'abc'
    }
    return render(request, 'servermon/terminal.html', context)
