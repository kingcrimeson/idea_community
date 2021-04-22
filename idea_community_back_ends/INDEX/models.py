from django.db import models
from LOGIN.models import User
class article(models.Model):
    article_id=models.AutoField(primary_key=True)
    article_title=models.CharField(max_length=100,blank=False)
    article_short=models.CharField(max_length=500,blank=False)
    article_content=models.TextField()
    article_author=models.ForeignKey(User,on_delete=models.CASCADE)
# Create your models here.
class tag(models.Model):
    article_id=models.ForeignKey(article,on_delete=models.CASCADE)
    article_tag=models.CharField(max_length=20,blank=False)
