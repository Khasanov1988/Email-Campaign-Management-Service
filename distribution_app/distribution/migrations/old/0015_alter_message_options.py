# Generated by Django 4.2.4 on 2023-08-17 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distribution', '0014_remove_settings_owner_message_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'permissions': [('set_published', 'Can publish')], 'verbose_name': 'сообщение', 'verbose_name_plural': 'сообщения'},
        ),
    ]
