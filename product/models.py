from django.db import models

# Create your models here.
from home.models import Category, Customer



class Products(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=20)
    p_price = models.FloatField(max_length=20)
    p_rating = models.FloatField(max_length=20, default='1')
    p_details = models.TextField(max_length=40)
    ca_id = models.ForeignKey(Category,related_name='p_ca_id', default='1', on_delete=models.SET_NULL,null=True)

class Cart(models.Model):
    cart_id= models.IntegerField(primary_key=True)
    cart_totalAmmount= models.FloatField(max_length=20)
    ca_id = models.ForeignKey(Category,related_name='c_p_ca_id', default='1', on_delete=models.SET_NULL,null=True)

class Wishlist(models.Model):
    w_id = models.IntegerField(primary_key=True)
    c_id = models.ForeignKey(Customer, related_name='w_c_id', default='1', on_delete=models.SET_NULL, null=True)
    p_id = models.ForeignKey(Products, related_name='w_p_id', default='1', on_delete=models.SET_NULL, null=True)
    c_id = models.ForeignKey(Customer,related_name='W_c_id', default='1', on_delete=models.SET_NULL,null=True)

class Review(models.Model):
    r_id = models.IntegerField(primary_key=True)
    review = models.FloatField(max_length=20)
    star = models.ForeignKey(Products,related_name='star', default='1', on_delete=models.SET_NULL,null=True)
    c_id = models.ForeignKey(Customer,related_name='R_c_id', default='1', on_delete=models.SET_NULL,null=True)
    p_id = models.ForeignKey(Products,related_name='R_p_id', default='1', on_delete=models.SET_NULL,null=True)

