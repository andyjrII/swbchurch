from django.db import models

class NewsEvent(models.Model):
    title = models.CharField(max_length=255)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    feature_pic = models.ImageField(upload_to='newsevent_images', default='feature_default.jpg')
    content_pic1 = models.ImageField(upload_to='newsevent_images')
    content_pic2 = models.ImageField(upload_to='newsevent_images')
    unique_together = [title,date_published]

    def __str__(self):
        return f'{self.title}'


class Sermon(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    link = models.URLField(unique=True,null=True)
    date_preached = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    unique_together = [title,author]
    feature_pic = models.ImageField(upload_to='sermon_images', default='feature_default.jpg')

    def __str__(self):
        return f'{self.title}'

class Service_Details(models.Model):
    title = models.CharField(max_length=255, unique=True)
    details = models.TextField(blank=True)
    feature_pic = models.ImageField(upload_to='service_images', default='feature_default.jpg')
    content_pic = models.ImageField(upload_to='service_images')

    def __str__(self):
        return f'{self.title}'