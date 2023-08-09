# Generated by Django 4.2.4 on 2023-08-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribution', '0007_remove_settings_distribution_time_finish_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='distribution_start_time',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='время начала рассылки'),
        ),
        migrations.AddField(
            model_name='settings',
            name='distribution_stop_time',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='время окончания рассылки'),
        ),
    ]
