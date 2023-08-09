from datetime import datetime

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(null=True, blank=True, max_length=150, verbose_name='slug')
    text = models.TextField(verbose_name='описание')
    preview = models.ImageField(null=True, blank=True, verbose_name='превью')
    made_date = models.DateField(default=datetime.now, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        # Строковое отображение объекта
        return f'Пост номер {self.pk}. {self.title}'

    class Meta:
        verbose_name = 'пост'  # Настройка для наименования одного объекта
        verbose_name_plural = 'посты'  # Настройка для наименования набора объектов
