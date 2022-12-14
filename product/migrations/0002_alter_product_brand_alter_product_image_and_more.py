# Generated by Django 4.1.2 on 2022-10-20 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(default='apple', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=55),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.BooleanField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='apple', max_length=40),
            preserve_default=False,
        ),
    ]
