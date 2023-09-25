from datetime import date, datetime, timedelta, time
from django.db import models
from django.utils import timezone
from distribution_app import settings


class Status(models.Model):
    status = models.CharField(max_length=150, verbose_name='Status')

    def __str__(self):
        return f'Distribution Status: {self.status}'

    class Meta:
        verbose_name = 'Distribution Status'
        verbose_name_plural = 'Distribution Statuses'


class Interval(models.Model):
    time_interval = models.CharField(max_length=150, verbose_name='Interval')

    def __str__(self):
        return f'Distribution Interval: {self.time_interval}'

    class Meta:
        verbose_name = 'Distribution Interval'
        verbose_name_plural = 'Distribution Intervals'


class Settings(models.Model):
    distribution_start_time = models.DateTimeField(default=timezone.now, null=True, blank=True,
                                                   verbose_name='Distribution Start Time')
    distribution_stop_time = models.DateTimeField(default=timezone.now, null=True, blank=True,
                                                  verbose_name='Distribution Stop Time')
    distribution_time = models.TimeField(default=time(hour=10, minute=0), verbose_name='Distribution Time')
    distribution_periodicity = models.ForeignKey('distribution.Interval',
                                                 on_delete=models.CASCADE, verbose_name='Distribution Periodicity')
    distribution_status = models.ForeignKey('distribution.Status',
                                            on_delete=models.CASCADE, verbose_name='Distribution Status')
    message = models.ForeignKey('distribution.Message', on_delete=models.CASCADE, verbose_name='Message')

    def __str__(self):
        return f'Distribution at {self.distribution_time}, {self.distribution_periodicity}'

    class Meta:
        verbose_name = 'Distribution Setting'
        verbose_name_plural = 'Distribution Settings'


class Logs(models.Model):
    last_attempt_time = models.DateTimeField(default=None, null=True, blank=True,
                                             verbose_name='Last Attempt Time')
    last_attempt_status = models.CharField(max_length=150, default=None, null=True, blank=True,
                                           verbose_name='Last Attempt Status')
    last_attempt_response = models.CharField(max_length=150, default=None, null=True, blank=True,
                                             verbose_name='Last Attempt Response')
    message = models.ForeignKey('distribution.Message', on_delete=models.CASCADE)

    def __str__(self):
        return f'Distribution Log on {self.last_attempt_time} with Status {self.last_attempt_status}'

    class Meta:
        verbose_name = 'Distribution Log'
        verbose_name_plural = 'Distribution Logs'


class Message(models.Model):
    subject = models.CharField(max_length=150, verbose_name='Message Subject')
    text = models.TextField(verbose_name='Message Body')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Message Owner')

    def __str__(self):
        return f'Message #{self.pk} with Subject: {self.subject}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        permissions = [
            (
                'set_published',
                'Can Publish',
            )
        ]
