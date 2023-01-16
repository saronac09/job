
from datetime import date
from django.db import models
class Register(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=50,choices=[('male','male'),('female','female'),('other','other')])
    address=models.TextField()
   
    category=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pin=models.TextField()
    phone=models.BigIntegerField()
    salary=models.TextField(default='Null')
    employess=models.TextField(default='Null')



class userform(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phone=models.BigIntegerField()

class employeeform(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    gender=models.CharField(max_length=50,choices=[('male','male'),('female','female'),('other','other')])
    phone=models.BigIntegerField()
    qualification=models.CharField(max_length=50)
    headrid=models.TextField()
    category=models.CharField(max_length=50)

class requestform(models.Model):
    headerid=models.TextField()
    userid=models.TextField()
    date=models.DateField()
    employe=models.TextField()
    salary=models.TextField(default='Null')

