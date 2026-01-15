from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage, RawMediaCloudinaryStorage


class Sermon(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    audio_file = models.FileField(
        upload_to="sermon_audio",
        storage=RawMediaCloudinaryStorage(),
        null=True,
        blank=True,
        help_text="Upload audio file to Cloudinary"
    )
    date_preached = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    feature_pic = models.ImageField(
        upload_to="sermon_images",
        storage=MediaCloudinaryStorage(),
        default="feature_default.jpg"
    )
    unique_together = [title, author]

    def __str__(self):
        return f"{self.title} - {self.date_preached}"
    
    @property
    def has_audio(self):
        """Check if sermon has an audio file"""
        return bool(self.audio_file)