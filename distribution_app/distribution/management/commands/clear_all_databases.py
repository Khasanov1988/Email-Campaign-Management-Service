from django.core.management import BaseCommand
from distribution.models import Message, Logs, Settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        # List of database models to clear
        database_models = [Message, Logs, Settings]

        for model in database_models:
            # Clear the database records for each model
            self.stdout.write(f'Clearing {model.__name__} database...')
            model.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Database {model.__name__} cleared successfully.'))
