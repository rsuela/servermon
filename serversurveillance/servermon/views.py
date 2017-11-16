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

