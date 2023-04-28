from django.db import models

class mod(models.Model):
    im = models.ImageField(upload_to='media', verbose_name='Фото')

class name(models.Model):
    nam  = models.CharField(max_length=100)
