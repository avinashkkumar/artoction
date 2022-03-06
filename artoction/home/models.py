from django.db import models
from account.models import Account
# Create your models here.


class Feedback(models.Model):
    user        = models.ForeignKey(Account, on_delete=models.CASCADE)
    feedback    = models.TextField()
    status      = models.CharField(max_length=12,default="unattended")