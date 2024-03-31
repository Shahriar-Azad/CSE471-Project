from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TutorDetail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact=models.CharField(max_length=15, null=True)
    gender=models.CharField(max_length=50, null=True)
    date=models.DateField(null=True)


    def __str__(self):
        return self.user.username

from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()


class Data(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


    def __str__(self):
        return self.location
