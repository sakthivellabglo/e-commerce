# Generated by Django 4.1.2 on 2022-10-30 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_remove_wishlist_product_wishlist_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tax',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_product_cost',
        ),
    ]
