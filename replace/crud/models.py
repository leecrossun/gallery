from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# DB정보 hyosun / 3katherine3

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True)
    reference = models.TextField(max_length=500)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(120, 120)])

    def __str__(self):
        return self.title

    def summary(self):
        return self.reference[:100]
    