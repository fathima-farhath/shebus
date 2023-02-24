from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    Catering = 'C'
    Women = 'W'


    desginations_choice = [
        (Catering,'Catering'),
        ( Women,'Women'),
    ]
    designation = models.CharField(max_length=1,choices=desginations_choice,default=Women)
    phone = models.CharField(max_length=10,null=True,blank=True)
    db_table = 'User'
   

 
   
