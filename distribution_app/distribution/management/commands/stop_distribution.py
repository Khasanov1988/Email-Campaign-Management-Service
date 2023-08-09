from django.core.management import BaseCommand

from distribution.models import Message, Logs, Settings, Status
from services.crontask.crontask_job import crontab_job


class Command(BaseCommand):

    def add_arguments(self, parser):  # Добавляем аргументы
        parser.add_argument('pk', type=int, help='Primary key of the Message object', default=1)

    def handle(self, context_data={}, *args, **options):
        pk = options['pk']  # Получаем переданный аргумент pk
        message = Message.objects.get(pk=pk)
        setting = Settings.objects.get(message=message)
        setting.distribution_status = Status.objects.get(status='completed')
        setting.save()
        context_data['settings_list'] = [Settings.objects.get(message=message)]
        crontab_job(context_data)
