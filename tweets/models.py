from django.db import models
from cloudinary.models import CloudinaryField



# Create your models here

class Tweets(models.Model):
    class Meta(object):
        db_table = 'tweets'
    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )    
    body = models.CharField (
        'Body', blank=True, null=True, max_length=140, db_index=True
    )
    created_at = models.DateField('Created DateTime', blank=True, auto_now_add=True
    ) 
    image = CloudinaryField('image', blank=True, null=True
    )
    update_at = models.DateField(
        'Updated DateTime', blank=True, auto_now_add=True
    )