# Generated by Django 3.2.9 on 2022-03-07 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_product_islisted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='isListed',
            field=models.BooleanField(default=True),
        ),
    ]
