from django.db import models

class mod(models.Model):
    im = models.ImageField(upload_to='media', verbose_name='Фото')

