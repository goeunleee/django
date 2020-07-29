from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.

class Profile(models.Model):
    title = models.CharField(max_length=255)

    image = ProcessedImageField(
        upload_to='image/',  
        processors=[ResizeToFill(500, 500)],  
        format='JPEG',  
        options={'quality': 90},  
    )
    def __str__(self):
        return self.title 
