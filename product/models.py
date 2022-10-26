from django.db import models
from django.contrib.auth.models import User

Order_choices = [
    ('pending', 'pending'),
    ('sucess', 'sucess'),
    ('failed', 'failed'),
]

class Product(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    brand = models.CharField(max_length=40)
    stock = models.BooleanField()

    def __str__(self):
        return " {} {} {} {} {} ".format(self.title, self.image, self.price, self.brand, self.stock)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True)
    date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return " {} {} {} {} {} ".format(self.user, self.product, self.quantity, self.price, self.date)


class Order(models.Model):
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
