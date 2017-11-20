from django.db import models

# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length=120)
    # System
    processor = models.CharField(max_length=120)
    memory = models.CharField(max_length=120)
    arch = models.CharField(max_length=120)
    os = models.CharField(max_length=120)
    
    # IP configuration
    ip = models.CharField(unique=True, max_length=30)
    mac = models.CharField( max_length=30)
    
    # Misc
    channel_reply = models.CharField(max_length=255)

    def __str__(self):
        return self.name