from django.db import models

# Create your models here.
class category(models.Model):
    class Meta(object):
        db_table="category"
    
    name=models.CharField('name', blank=False, null=False, max_length=100)
    created_at=models.DateTimeField('createDateTime', blank=True, auto_now_add=True)
    updated_at=models.DateTimeField('createDateTime', blank=True, auto_now_add=True)