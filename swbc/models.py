from django.db import models

class NewsEvents(models.Model):
    title = models.CharField(max_length=255)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    content = models.TextField

class Sermons(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    link = models.URLField
    date_preached = models.DateField
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
