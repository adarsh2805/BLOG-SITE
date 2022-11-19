from pickle import TRUE
from django.db import models
from datetime import datetime

# Create your models here.


class Post(models.Model):
    tittile = models.CharField(max_length=100,unique=TRUE)
    body=models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
