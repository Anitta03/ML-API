# Generated by Django 3.2.23 on 2023-12-13 09:35

import cnn.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tomato',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=cnn.models.upload_to),
        ),
    ]
