# Ваше_приложение/models.py
from django.db import models


class Image(models.Model):
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/', default='',
                               blank=True)  # Добавляем значение по умолчанию и разрешаем пустое значение (blank=True)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.description and self.image1.name
