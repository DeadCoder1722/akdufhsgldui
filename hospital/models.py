from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.



departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

def defaultuser():
    us = User(username="deleteduser",email="deleteduser@deleted.com")
    return us.id

class Doctor(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE,related_name="Doctor")
    image = models.ImageField(default="default.png",upload_to="profile_pics")
    firstname = models.CharField(max_length=100,default='firstname')
    lastname = models.CharField(max_length=100,default='lastname')
    age = models.IntegerField(default=0)
    dob = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=300,default="address")
    city = models.CharField(max_length=100,default="city")
    country = models.CharField(max_length=100,default="country")
    postalcode = models.IntegerField(default=0)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    def __str__(self):
        return f'{self.user.username} Doctor Profile'


class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Admin")
    image = models.ImageField(default="default.png",upload_to="profile_pics")
    firstname = models.CharField(max_length=100,default='firstname')
    lastname = models.CharField(max_length=100,default='lastname')
    age = models.IntegerField(default=0)
    dob = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=300,default="address")
    city = models.CharField(max_length=100,default="city")
    country = models.CharField(max_length=100,default="country")
    postalcode = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.user.username} Admin Profile'


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Patient")
    image = models.ImageField(default="default.png",upload_to="profile_pics")
    firstname = models.CharField(max_length=100,default='firstname')
    lastname = models.CharField(max_length=100,default='lastname')
    age = models.IntegerField(default=0)
    dob = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=300,default="address")
    city = models.CharField(max_length=100,default="city")
    country = models.CharField(max_length=100,default="country")
    postalcode = models.IntegerField(default=0)
    symptoms = models.CharField(max_length=100,default="fever")
    def __str__(self):
        return f'{self.user.username} Patient Profile'