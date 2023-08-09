from django.core.management import BaseCommand

from distribution.models import Status


class Command(BaseCommand):
    def handle(self, *args, **options):
        # List preparation
        new_data = [
            {'status': 'completed'},
            {'status': 'created'},
            {'status': 'started'},
        ]
        # Cleaning up the previous database
        self.stdout.write('Clearing "Status" database...')
        Status.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('"Status" database cleared successfully.'))

        # Filling the database with new data
        self.stdout.write('Filling "Status" database...')
        categories_for_adding = []
        for category_item in new_data:
            categories_for_adding.append(Status(**category_item))
        Status.objects.bulk_create(categories_for_adding)
        self.stdout.write(self.style.SUCCESS('"Status" database filled successfully.'))