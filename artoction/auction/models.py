from django.db import models
import uuid
import pathlib

from account.models import Account

# Create your models here.

# model product 

def uploadImageHandler(instance,filename):
    fpath = pathlib.Path(filename)
    newFileName = str(uuid.uuid1())
    return f"images/product/{newFileName}{fpath.suffix}"

class Product(models.Model):
    name                = models.CharField( max_length=50)
    base_price          = models.FloatField(default=None)
    current_price       = models.FloatField()
    current_bidder      = models.CharField(max_length=20,null=True,blank=True)
    listedBy            = models.ForeignKey(Account, on_delete=models.CASCADE)
    description         = models.TextField()
    category            = models.CharField(max_length=50, null= True, blank=True)
    upload_date         = models.DateField(auto_now=False, auto_now_add=True)
    last_bid_date       = models.DateField(auto_now=True, auto_now_add=False)
    image1              = models.ImageField(upload_to=uploadImageHandler, max_length=None)
    image2              = models.ImageField(upload_to=uploadImageHandler, max_length=None)
    image3              = models.ImageField(upload_to=uploadImageHandler, max_length=None)
    image4              = models.ImageField(upload_to=uploadImageHandler, max_length=None)
    image5              = models.ImageField(upload_to=uploadImageHandler, max_length=None)
    # setting the category for auction like upcoming, ongoing and completed
    isUpcoming          = models.BooleanField(default=True)
    isOngoing           = models.BooleanField(default=False)
    isSold              = models.BooleanField(default=False)

    def __str__(self):
        return self.name
