# Generated by Django 3.2.8 on 2021-10-27 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20211027_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price_product',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 27, 0, 21, 6, 518647)),
        ),
    ]
