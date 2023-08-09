from datetime import date, datetime, timedelta, time

from django.db import models
from django.utils import timezone

from distribution_app import settings


# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=150, verbose_name='статус')

    def __str__(self):
        # Строковое отображение объекта
        return f'Статус рассылки: {self.status}'

    class Meta:
        verbose_name = 'статус рассылки'  # Настройка для наименования одного объекта
        verbose_name_plural = 'статусы рассылки'  # Настройка для наименования набора объектов


class Interval(models.Model):
    time_interval = models.CharField(max_length=150, verbose_name='периодичность')

    def __str__(self):
        # Строковое отображение объекта
        return f'Периодичность рассылки: {self.time_interval}'

    class Meta:
        verbose_name = 'периодичность рассылки'  # Настройка для наименования одного объекта
        verbose_name_plural = 'периодичности рассылки'  # Настройка для наименования набора объектов


class Settings(models.Model):
    distribution_start_time = models.DateTimeField(default=timezone.now, null=True, blank=True,
                                                   verbose_name='время начала рассылки')
    distribution_stop_time = models.DateTimeField(default=timezone.now, null=True, blank=True,
                                                  verbose_name='время окончания рассылки')
    distribution_time = models.TimeField(default=time(hour=10, minute=0), verbose_name='время рассылки')
    distribution_periodicity = models.ForeignKey('distribution.Interval',
                                                 on_delete=models.CASCADE, verbose_name='периодичность рассылки')
    distribution_status = models.ForeignKey('distribution.Status',
                                            on_delete=models.CASCADE, verbose_name='статус рассылки')
    message = models.ForeignKey('distribution.Message', on_delete=models.CASCADE, verbose_name='сообщение')


    def __str__(self):
        # Строковое отображение объекта
        return f'Рассылка в {self.distribution_time}, {self.distribution_periodicity}'

    class Meta:
        verbose_name = 'настройка рассылки'  # Настройка для наименования одного объекта
        verbose_name_plural = 'настройки рассылки'  # Настройка для наименования набора объектов


class Logs(models.Model):
    last_attempt_time = models.DateTimeField(default=None, null=True, blank=True,
                                             verbose_name='дата и время последней попытки')
    last_attempt_status = models.CharField(max_length=150, default=None, null=True, blank=True,
                                           verbose_name='статус попытки')
    last_attempt_response = models.CharField(max_length=150, default=None, null=True, blank=True,
                                             verbose_name='ответ почтового сервера')
    message = models.ForeignKey('distribution.Message', on_delete=models.CASCADE)

    def __str__(self):
        # Строковое отображение объекта
        return f'Лог рассылки на дату: {self.last_attempt_time} в статусе {self.last_attempt_status}'

    class Meta:
        verbose_name = 'лог рассылки'  # Настройка для наименования одного объекта
        verbose_name_plural = 'лог рассылки'  # Настройка для наименования набора объектов


class Message(models.Model):
    subject = models.CharField(max_length=150, verbose_name='тема рассылки')
    text = models.TextField(verbose_name='тело письма')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='владелец')

    def __str__(self):
        # Строковое отображение объекта
        return f'Сообщение с номером {self.pk} на тему: {self.subject}'

    class Meta:
        verbose_name = 'сообщение'  # Настройка для наименования одного объекта
        verbose_name_plural = 'сообщения'  # Настройка для наименования набора объектов
        permissions = [
            (
                'set_published',
                'Can publish',
            )
        ]
