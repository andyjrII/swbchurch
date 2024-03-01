from django.db import models


class NewsEvent(models.Model):
    title = models.CharField(max_length=255)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True)
    feature_pic = models.ImageField(
        upload_to="newsevent_images", default="feature_default.jpg"
    )
    content_pic = models.ImageField(
        upload_to="newsevent_images", default="content_default.jpg"
    )
    unique_together = [title, date_published]

    def __str__(self):
        return f"{self.title} - {self.date_published}"
