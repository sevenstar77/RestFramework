from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Post(models.Model):
    boardIx = models.CharField(max_length=1024)
    title = models.CharField(max_length=1024)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(User)
    regdate = models.DateTimeField(auto_created=True, auto_now_add=True)
