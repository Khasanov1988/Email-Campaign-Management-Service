# Generated by Django 4.2.4 on 2023-08-06 15:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_interval', models.DateTimeField(default=datetime.timedelta(days=1), verbose_name='периодичность')),
            ],
            options={
                'verbose_name': 'периодичность рассылки',
                'verbose_name_plural': 'периодичности рассылки',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_attempt_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='дата и время последней попытки')),
                ('last_attempt_status', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='статус попытки')),
                ('last_attempt_response', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='ответ почтового сервера')),
            ],
            options={
                'verbose_name': 'лог рассылки',
                'verbose_name_plural': 'лог рассылки',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=150, verbose_name='статус')),
            ],
            options={
                'verbose_name': 'статус рассылки',
                'verbose_name_plural': 'статусы рассылки',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distribution_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='время рассылки')),
                ('distribution_periodicity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='distribution.interval', verbose_name='периодичность рассылки')),
                ('distribution_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='distribution.status', verbose_name='статус рассылки')),
            ],
            options={
                'verbose_name': 'настройка рассылки',
                'verbose_name_plural': 'настройки рассылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150, verbose_name='тема рассылки')),
                ('text', models.TextField(verbose_name='тело письма')),
                ('logs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='distribution.logs', verbose_name='логи рассылки')),
                ('settings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='distribution.settings', verbose_name='настройки рассылки')),
            ],
        ),
    ]
