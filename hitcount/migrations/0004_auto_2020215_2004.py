# Generated by Django 2.0.3 on 2019-06-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hitcount', '0003_auto_20190608_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hitcount',
            name='object_pk',
            field=models.PositiveIntegerField(verbose_name='object ID'),
        ),
    ]
