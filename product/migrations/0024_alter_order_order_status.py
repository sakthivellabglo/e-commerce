# Generated by Django 4.1.2 on 2022-11-02 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[('PENDING', 'PENDING'), ('SUCCESS', 'sucess'), ('FAILED', 'failed')], default=2),
        ),
    ]
