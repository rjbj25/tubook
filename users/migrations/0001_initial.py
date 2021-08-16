# Generated by Django 3.2.6 on 2021-08-16 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('neighborhood', models.CharField(max_length=60)),
                ('zip_code', models.IntegerField(max_length=15)),
                ('aditional_reference', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField(max_length=25)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
