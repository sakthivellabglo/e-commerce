# Generated by Django 4.1.2 on 2022-10-21 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
    ]
