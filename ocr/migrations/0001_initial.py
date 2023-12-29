# Generated by Django 3.2.23 on 2023-12-29 10:07

from django.db import migrations, models
import ocr.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=ocr.models.upload_to)),
            ],
        ),
    ]
