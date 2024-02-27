from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table='Post'

    name=models.CharField(
        'Name',max_length=30,db_index=True,blank=True,null=False
    )

    body=models.CharField(
        'Body',max_length=500,blank=True
    )

    created_at=models.DateTimeField(
        'Created DateTime',blank=True,auto_now_add=True
    )

    image=models.ImageField(
        'Image',upload_to='subX/files/images',blank=True
    )