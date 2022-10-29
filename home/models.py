from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Customer(models.Model):
    c_id = models.IntegerField(primary_key=True)
    c_user = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    c_address = models.TextField(max_length=80)
    c_phoneNum = models.CharField(max_length=20)

class Category(models.Model):
    ca_id = models.IntegerField(primary_key=True)
    ca_name = models.CharField(max_length=20)

class Sub_Category(models.Model):
    sc_id = models.IntegerField(primary_key=True)
    sc_name = models.CharField(max_length=20)
