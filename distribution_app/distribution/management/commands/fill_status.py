from django.core.management import BaseCommand
from distribution.models import Status

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Prepare a list of new data
        new_data = [
            {'status': 'completed'},
            {'status': 'created'},
            {'status': 'started'},
        ]

        # Clear the previous database records
        self.stdout.write('Clearing "Status" database...')
        Status.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('"Status" database cleared successfully.'))

        # Fill the database with new data
        self.stdout.write('Filling "Status" database...')
        statuses_for_adding = []
        for status_item in new_data:
            statuses_for_adding.append(Status(**status_item))
        Status.objects.bulk_create(statuses_for_adding)
        self.stdout.write(self.style.SUCCESS('"Status" database filled successfully.'))
