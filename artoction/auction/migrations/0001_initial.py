# Generated by Django 3.2.9 on 2022-02-19 08:48

import auction.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('base_price', models.FloatField(default=None)),
                ('current_price', models.FloatField()),
                ('current_bidder', models.CharField(blank=True, max_length=20, null=True)),
                ('listedBy', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('last_bid_date', models.DateField(auto_now=True)),
                ('image1', models.ImageField(upload_to=auction.models.uploadImageHandler)),
                ('image2', models.ImageField(upload_to=auction.models.uploadImageHandler)),
                ('image3', models.ImageField(upload_to=auction.models.uploadImageHandler)),
                ('image4', models.ImageField(upload_to=auction.models.uploadImageHandler)),
                ('image5', models.ImageField(upload_to=auction.models.uploadImageHandler)),
                ('isUpcoming', models.BooleanField(default=True)),
                ('isOngoing', models.BooleanField(default=False)),
                ('isSold', models.BooleanField(default=False)),
            ],
        ),
    ]
