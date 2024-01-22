from django.db import models

class NewsEvents(models.Model):
    title = models.CharField(max_length=255)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True)
    unique_together = [title,date_published]


class Sermons(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    link = models.URLField(unique=True,null=True)
    date_preached = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    unique_together = [title,author]
