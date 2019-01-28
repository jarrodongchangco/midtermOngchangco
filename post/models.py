from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_update = models.DateTimeField(default=datetime.now, blank=True)
    content = models.TextField(max_length=100)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                                    related_name = 'choice',
                                    null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=100)
