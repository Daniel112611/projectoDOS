# Generated by Django 3.2.8 on 2021-11-15 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0011_auto_20211109_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket_detail',
            name='devolution_approved',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ticket_detail',
            name='devolution_request',
            field=models.DateField(),
        ),
    ]
