from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=64)	
    date = models.DateTimeField(default=datetime.now())	
    added = models.DateTimeField(auto_now_add=True)
    head = models.TextField(blank=True)
    body = models.TextField()
    visible = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to='uploads/%Y/%m')
    slug = models.SlugField(primary_key=True, max_length=64)

    def __unicode__(self):
        return self.title
