from datetime import date
from time import time
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
	title = models.CharField(max_length = 40)
	image = models.ImageField(upload_to='images/')
	price = models.IntegerField()
	brand = models.CharField(max_length = 40)
	stock = models.BooleanField()
	def __str__(self):
		return " {} {} {} {} {} ".format(self.title,self.image,self.price,self.brand,self.stock)
# Create your models here.
class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	price = models.FloatField(blank=True)
	date = models.DateField(auto_now_add = True)

