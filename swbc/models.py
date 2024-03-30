from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255, unique=True)
    details = models.TextField(blank=True)
    feature_pic = models.ImageField(
        upload_to="service_images", default="feature_default.jpg"
    )

    def __str__(self):
        return f"{self.title}"
