# Generated by Django 4.1.1 on 2022-09-25 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodotti', '0006_product_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='capacity',
            field=models.TextField(max_length=100),
        ),
    ]