from django.db import models

# Create your models here.

class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    
     


class Traveler(models.Model):
    travelername = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    location = models.CharField(max_length=100)
    review = models.CharField(max_length=300)
    
    
    