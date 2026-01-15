from django.db import models

class Service(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('weekly', 'Weekly Service'),
        ('special', 'Special Service'),
    ]
    
    title = models.CharField(max_length=255)
    service_type = models.CharField(max_length=10, choices=SERVICE_TYPE_CHOICES, default='special')
    day = models.CharField(max_length=50, blank=True, help_text="e.g., Sundays, Wednesdays, Saturdays")
    time = models.CharField(max_length=20, blank=True, help_text="e.g., 8:00AM, 5:30PM")
    details = models.TextField(blank=True)
    feature_pic = models.ImageField(
        upload_to="service_images", default="feature_default.jpg"
    )
    order = models.IntegerField(default=0, help_text="Order for displaying services (lower numbers appear first)")

    class Meta:
        ordering = ['order', 'title']
        unique_together = [['title', 'service_type']]

    def __str__(self):
        return f"{self.title} ({self.service_type})"
