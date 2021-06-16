from django.db import models

# Create your models here.

class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    
     


class Traveler(models.Model):
    
    review = models.CharField(max_length=300)
    image = models.ImageField(upload_to='pics')
    travelername = models.CharField(max_length=100)
    location = models.CharField(max_length=100)