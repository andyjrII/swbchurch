from django.db import models


class Devotional(models.Model):
    title = models.CharField(max_length=255, unique=True)
    contents = models.TextField(blank=True)
    date = models.DateField(null=True)
    reference_text = models.TextField(blank=True)
    daily_bible_reading = models.CharField(max_length=255)
    week_teaching = models.CharField(max_length=255)
    confession = models.TextField(blank=True)

    unique_together = [title, date]

    def __str__(self):
        return f"{self.title} - {self.date}"
