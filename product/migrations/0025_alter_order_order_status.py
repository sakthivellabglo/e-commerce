# Generated by Django 4.1.4 on 2022-12-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(2, 'PENDING'), (1, 'sucess'), (0, 'failed')], default=2),
        ),
    ]