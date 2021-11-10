from django.db import models

from admin_advisor.models import advisor_name

# Create your models here.

class register(models.Model):
    name = models.CharField(max_length=100,default = 'user')
    email = models.CharField(max_length=100,default = 'user.com')
    password = models.CharField(max_length=100,default = 'user')
    user_id = models.IntegerField(default = 0)
    def __str__(self):
        return self.name
        
    
class login(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    
class booking(models.Model):
    booking_time = models.CharField(max_length=20)
    advisor_id = models.IntegerField(default = 0)
    user_id = models.IntegerField(default = 0)
    booking_id = models.IntegerField(default = 0)
    