# Ваше_приложение/models.py
from django.db import models


class Image(models.Model):
    image1 = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.description and self.image1.name

class Image2(models.Model):
    image1 = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.description and self.image1.name

class Image3(models.Model):
    image1 = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.description and self.image1.name
