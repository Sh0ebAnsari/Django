from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    author_name=models.CharField(max_length=10)
    title=models.CharField(max_length=20)
    desc=models.TextField()
    publish_date=models.DateTimeField(blank=True,auto_now=True)