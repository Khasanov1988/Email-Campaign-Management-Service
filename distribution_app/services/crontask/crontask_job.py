import os
from datetime import datetime

from django.utils import timezone

from distribution.models import Settings
from distribution_app.settings import BASE_DIR, CRON_DIR


def cron_schedule(setting: Settings) -> str:
    if setting.distribution_periodicity.time_interval == '1 week':
        second_part = ' * * 1'
    elif setting.distribution_periodicity.time_interval == '1 month':
        second_part = ' 1 * *'
    else:
        second_part = ' * * *'

    time = str(setting.distribution_time)
    first_part = f'{time[3:5]} {time[0:2]}'
    return first_part + second_part


def cron_definite_time_schedule(distribution_time) -> str:
    target_date = timezone.localtime(distribution_time)

    current_timezone = timezone.get_current_timezone()

    # Получение значений минут, часов, дней и т.д. из даты и времени
    minute = target_date.minute
    hour = target_date.hour
    day = target_date.day
    month = target_date.month
    dow = target_date.weekday() + 1  # Нумерация дней недели в cron начинается с 1 (понедельник)

    # Создание выражения cron
    cron_expression = f"{minute} {hour} {day} {month} {dow}"

    return cron_expression


def make_command(command_name: str, *args: int | list) -> str:
    path_to_project = os.path.join(BASE_DIR, '')[:-1]
    path_to_venv_activation = r'..\venv\Scripts\activate'
    final_command = f'cd {path_to_project} & call {path_to_venv_activation} & python manage.py {command_name}'
    if args:
        for arg in args:
            if isinstance(arg, list):
                arg = ' '.join(arg)
            final_command += f' {arg}'
    return final_command


def is_command_exist(command) -> bool:
    with open(CRON_DIR, 'r', encoding='utf-8') as file:
        content = file.readlines()
        for line in content:
            if line.strip() == command.strip():
                return True
        return False


def command_write(command) -> None:
    with open(CRON_DIR, 'a', encoding='utf-8') as file:
        file.write('\n' + command)


def command_delete(command) -> None:
    with open(CRON_DIR, 'r', encoding='utf-8') as file:
        content = file.readlines()

    with open(CRON_DIR, 'w', encoding='utf-8') as file:
        for line in content:
            if line.strip() != command.strip() and line.strip() != '':
                file.write(line)


def crontab_job(context_data: dict) -> None:
    for setting in context_data['settings_list']:
        pk = setting.message.pk

        if setting.distribution_start_time is not None:
            command = cron_definite_time_schedule(setting.distribution_start_time) + " " + make_command(
                'start_distribution', pk)
            # Проверяем есть ли рассылки, которые нужно запланировать начать
            if setting.distribution_start_time > timezone.now():
                if not is_command_exist(command):
                    command_write(command)
            else:
                if is_command_exist(command):
                    command_delete(command)

        if setting.distribution_stop_time is not None:
            command = cron_definite_time_schedule(setting.distribution_stop_time) + " " + make_command(
                'stop_distribution', pk)
            # Проверяем есть ли рассылки, которые нужно запланировать закончить
            if setting.distribution_stop_time > timezone.now():
                if not is_command_exist(command):
                    command_write(command)
            else:
                if is_command_exist(command):
                    command_delete(command)

        # Проверяем есть ли незапущенные рассылки
        command = cron_schedule(setting) + " " + make_command('send_email', pk)
        current_status: str = setting.distribution_status.status
        if current_status == 'started':
            if not is_command_exist(command):
                command_write(command)
        if current_status == 'completed':
            if is_command_exist(command):
                command_delete(command)
