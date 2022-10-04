from datetime import datetime
from time import timezone
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        'auth.User',
        models.CASCADE
    )
    body = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    message = models.TextField()
    date_sent = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.subject
