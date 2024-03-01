from django.db import models


class Sermon(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    link = models.URLField(unique=True, null=True)
    date_preached = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    feature_pic = models.ImageField(
        upload_to="sermon_images", default="feature_default.jpg"
    )
    unique_together = [title, author]

    def __str__(self):
        return f"{self.title} - {self.date_preached}"
