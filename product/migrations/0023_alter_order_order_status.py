# Generated by Django 4.1.2 on 2022-11-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[('PENDING', 'pending'), ('SUCCESS', 'sucess'), ('FAILED', 'failed')], default=2),
        ),
    ]
