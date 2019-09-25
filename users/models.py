from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
from django import forms
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    state_of_origin = models.CharField(max_length=20, default='')
    age = models.IntegerField(default=0)
    phone_no = models.IntegerField(default=0)
    address = models.CharField(max_length = 100, default ='')
    sex = (
        ('m','Male'),
        ('f','Female')
    )
    gender = models.CharField(max_length=100, choices=sex, default ='')

    stat = {
        ('c', 'Corper'),
        ('p', 'Passed-Out')
    }
    status = models.CharField(max_length=100, choices=stat, default ='')

    off = {
        ('n','NIL'),
        ('p','President'),
        ('vp','Vice-president'),
        ('s','Secretary'),
        ('ss','Sisters cod'),
        ('as/f','Ass Secretary/Fin sec'),
        ('ws','Welfare secretary'),
        ('bs','Bible study secretary'),
        ('es','Evangelism secretary'),
        ('t','Treasurer'),
        ('aes','Ass Evangelism sec'),
        ('a','As. Welfare'),
        ('pro','PRO'),
        ('md','Music Director.')
    }
    office = models.CharField(max_length=100, choices=off, default ='')
    
    qualification = models.CharField(max_length = 100, default ='')
    state_code = models.CharField(max_length=20, default='')
    ppa = models.CharField(max_length = 100, default ='')

    def __str__(self):
        return f'{self.user.username} Profile'

#    def save(self, *args, **kwargs):
 #       super(Profile, self).save(*args, **kwargs)

#        img = Image.open(self.image.path)

#        if img.height > 300 or img.width > 300:
#            output_size = (300, 300)
#            img.thumbnail(output_size)
#            img.save(self.image.path)
