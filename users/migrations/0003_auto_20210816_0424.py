# Generated by Django 3.2.6 on 2021-08-16 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210816_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
