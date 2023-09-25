from django.core.management import BaseCommand

from distribution.models import Interval

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Prepare a list of new data
        new_data = [
            {'time_interval': '1 day'},
            {'time_interval': '1 week'},
            {'time_interval': '1 month'},
        ]

        # Clear the previous database records
        self.stdout.write('Clearing "Interval" database...')
        Interval.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Database cleared successfully.'))

        # Fill the database with new data
        self.stdout.write('Filling "Interval" database...')
        intervals_for_adding = []
        for interval_data in new_data:
            intervals_for_adding.append(Interval(**interval_data))
        Interval.objects.bulk_create(intervals_for_adding)
        self.stdout.write(self.style.SUCCESS('Database filled successfully.'))
