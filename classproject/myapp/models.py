from django.db import models

# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    mobile=models.IntegerField()
    email=models.EmailField()
    city=models.CharField(max_length=100)
    address=models.TextField()
    password=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to='profile_pic/')

    def __str__(self):
        return self.fname

class Contact(models.Model):
    fname=models.CharField(max_length=100)
    mobile=models.IntegerField()
    email=models.EmailField()
    remarks=models.TextField()

    def __str__(self):
        return self.fname
    
