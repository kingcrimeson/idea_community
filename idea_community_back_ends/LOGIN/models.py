from django.db import models
from django.utils import timezone
class User (models.Model):
    openid=models.CharField(max_length=50,unique=True,primary_key=True)
    nickname=models.CharField(max_length=100)
    create_time=models.DateTimeField(auto_now_add=True)
# Create your models here.
