from django.db import models

# Create your models here.

def upload_to(instance, filename):
    return 'image/{filename}'.format(filename = filename)


class bill(models.Model):
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)
