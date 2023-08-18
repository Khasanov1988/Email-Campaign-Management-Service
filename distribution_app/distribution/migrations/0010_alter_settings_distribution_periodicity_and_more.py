# Generated by Django 4.2.4 on 2023-08-17 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distribution', '0009_alter_settings_distribution_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='distribution_periodicity',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='distribution.interval', verbose_name='периодичность рассылки'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='settings',
            name='distribution_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distribution.status', verbose_name='статус рассылки'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distribution.message', verbose_name='сообщение'),
        ),
    ]