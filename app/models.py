from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tuto(models.Model):
    cle_tuto = models.CharField(primary_key=True, max_length = 7)
    typeTuto = models.CharField(max_length = 50)
    idTutoVideo = models.CharField(max_length = 700)
    client_url = models.CharField(default="",max_length = 700)
    clientName = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tuto'