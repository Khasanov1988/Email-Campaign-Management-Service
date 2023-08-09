from datetime import date, datetime, timedelta

from django.db import models


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
    distribution_time_start = models.DateField(default=datetime.now, verbose_name='дата начала рассылки')
    distribution_time_finish = models.DateField(default=(datetime.now() + timedelta(days=7)), verbose_name='дата окончания рассылки',)
    distribution_periodicity = models.ForeignKey('distribution.Interval', on_delete=models.SET_NULL, null=True,
                                                 blank=True,
                                                 verbose_name='периодичность рассылки')
    distribution_status = models.ForeignKey('distribution.Status', on_delete=models.SET_NULL, null=True, blank=True,
                                            verbose_name='статус рассылки')
    message = models.ForeignKey('distribution.Message', on_delete=models.CASCADE)

    def __str__(self):
        # Строковое отображение объекта
        return f'Рассылка c {self.distribution_time_start} по {self.distribution_time_finish}'

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

    def __str__(self):
        # Строковое отображение объекта
        return f'Сообщение с номером {self.pk} на тему: {self.subject}'

    class Meta:
        verbose_name = 'сообщение'  # Настройка для наименования одного объекта
        verbose_name_plural = 'сообщения'  # Настройка для наименования набора объектов


