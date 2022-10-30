from django.db import models
from django.contrib.auth.models import User

Order_choices = [
    ('pending', 'pending'),
    ('sucess', 'sucess'),
    ('failed', 'failed'),
]


class TimeStampBaseModel(models.Model):
    created_on =  models.DateTimeField(auto_now_add=True ,null = True)
    updated_on =  models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 

class Product(TimeStampBaseModel):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    brand = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    stock = models.BooleanField(default=True)

    def __str__(self):
        return " {} {} {} {} {} ".format(self.title, self.image, self.price, self.brand, self.stock)

class Cart(TimeStampBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True)
    date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return " {} {} {} {} {} ".format(self.user, self.product, self.quantity, self.price, self.date)


class Order(TimeStampBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Cart)
    tax = models.FloatField(null=True)
    total_product_cost = models.PositiveIntegerField(null=True)
    order_status = models.CharField(
        max_length=15,
        choices=Order_choices,
        default='pending'
    )

    def __str__(self):
        return self.user.username

class Wishlist(TimeStampBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

