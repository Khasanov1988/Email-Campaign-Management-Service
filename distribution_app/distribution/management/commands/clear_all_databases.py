from django.core.management import BaseCommand

from distribution.models import Message, Logs, Settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_base_list = [Message, Logs, Settings]
        for data_base in data_base_list:
            self.stdout.write(f'Clearing {data_base.__name__} database...')
            data_base.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Database {data_base.__name__} cleared successfully.'))
