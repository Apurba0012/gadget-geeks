from django.db import models

# Create your models here.
from home.models import Customer
from item.models import Products, Cart


class Order(models.Model):
    o_id = models.IntegerField(primary_key=True)
    o_total = models.FloatField(max_length=20)
    p_id = models.ForeignKey(Products, related_name='o_p_id', default='1', on_delete=models.SET_NULL, null=True)
    o_quantity = models.IntegerField()
    cart_id = models.ForeignKey(Cart, related_name='o_c_id', default='1', on_delete=models.SET_NULL, null=True)

class Payment(models.Model):
    pa_id = models.IntegerField(primary_key=True)
    pa_type = models.CharField(max_length=20)
    pa_confirm = models.CharField(max_length=20)
    c_id = models.ForeignKey(Customer,related_name='pa_c_id', default='1', on_delete=models.SET_NULL,null=True)
    cart_id = models.ForeignKey(Cart, related_name='pay_c_id', default='1', on_delete=models.SET_NULL, null=True)
