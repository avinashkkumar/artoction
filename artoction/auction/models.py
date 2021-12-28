from django.db import models
import uuid
import pathlib

# Create your models here.

# model product 

def uploadImageHandler(instance,filename):
    fpath = pathlib.Path(filename)
    newFileName = str(uuid.uuid1())
    return f"images/self/{newFileName}{fpath.suffix}"

class Product(models.Model):
    name                = models.CharField( max_length=50)
    current_price       = models.FloatField()
    current_bidder      = models.CharField(max_length=20)
    isSold              = models.BooleanField()
    listedBy            = models.CharField(max_length=20)
    notesByLister       = models.TextField()
    category            = models.CharField(max_length=50)
    image1              = models.ImageField(upload_to=uploadImageHandler, max_length=None)
    image2              = models.ImageField(upload_to=uploadImageHandler, max_length=None)
    image3              = models.ImageField(upload_to=uploadImageHandler, max_length=None)
    image4              = models.ImageField(upload_to=uploadImageHandler, max_length=None)
    image5              = models.ImageField(upload_to=uploadImageHandler, max_length=None)

    def __str__(self):
        return self.name
