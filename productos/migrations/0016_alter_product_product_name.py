# Generated by Django 3.2.8 on 2021-11-21 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0015_alter_product_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50),
        ),
    ]
