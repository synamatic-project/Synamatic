from email.mime import image
from django.db import models
from cloudinary.models import cloudinaryField
from apps.categories.models import category


# Create your models here.
class movies(models.Model):
    MY_CHOICES = (('Newly Released'), ('Coming Soon'))
    class Meta(object):
        db_table="movies"

name = models.CharField('name', blank=False, null=False,  max_length= 50, db_index=True)
description = models.CharField('description', blank=False, null=False, max_length= 250)
image = cloudinaryField(image, blank=True, null=True)
image_mobile = cloudinaryField(image, blank=True, null=True)
released_type = models.CharField('released_type', black=False, null=False, max_length=50, choices=MY_CHOICES)
category_id = models.ForeignKey(category, on_delete=models.CASCADE )
ratings = models.IntegerField('ratings',  blank=False, null=False)
release_date = models.IntegerField('release_date',  blank=False, null=False)
trailer = models.CharField ('trailer', blank=False, null=False, max_length=800)
created_at=models.DateTimeField('createDateTime', blank=True, auto_now_add=True)
updated_at=models.DateTimeField('createDateTime', blank=True, auto_now_add=True)

