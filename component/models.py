from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User


# Create your models here.


class AllCards(models.Model):
    image = models.ImageField(upload_to='cards', blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    date_added = models.DateTimeField(default=timezone.now)
    urls = models.URLField(max_length=300, blank=True, null=True)  # make sure it's URLField
    type = models.TextField(max_length=100)

    def __str__(self):
        return self.name



class Members(models.Model):
    image = models.ImageField(upload_to='cards',blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(default='')
    date_added = models.DateTimeField(default=timezone.now)
    position = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
    
    
    
    
class NewArrival(models.Model):
    image = models.ImageField(upload_to='cards', blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    date_added = models.DateTimeField(default=timezone.now)
    urls = models.URLField(max_length=300, blank=True, null=True)  # make sure it's URLField
    type = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    
    
class FeedBack(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    message = models.TextField(default='')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name