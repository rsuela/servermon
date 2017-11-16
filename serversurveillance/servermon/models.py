from django.db import models

# Create your models here.
class Server(models.Model):
    os = models.CharField(max_length=120)
    ip = models.CharField(unique=True, max_length=30)
    name = models.CharField(max_length=120)
    channel_reply = models.CharField(max_length=255)

    def __str__(self):
        return self.name