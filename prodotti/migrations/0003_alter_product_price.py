# Generated by Django 4.1.1 on 2022-09-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodotti', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
