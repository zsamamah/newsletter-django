from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        'auth.User',
        models.CASCADE
    )
    body = models.TextField()

    def __str__(self):
        return self.title
