# Generated by Django 4.1.2 on 2022-10-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_remove_order_items_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
