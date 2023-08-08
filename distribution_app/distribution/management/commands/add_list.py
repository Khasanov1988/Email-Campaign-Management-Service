from django.core.management import BaseCommand

from distribution.models import Interval


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Подготовка списка
        new_data = [
            {'time_interval': '1 day'},
            {'time_interval': '1 week'},
            {'time_interval': '1 month'},
        ]
        # Очистка предыдущей базы данных
        self.stdout.write('Clearing "Interval" database...')
        Interval.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Database cleared successfully.'))

        # Заполнение базы данных новыми данными
        self.stdout.write('Filling "Interval" database...')
        categories_for_adding = []
        for category_item in new_data:
            categories_for_adding.append(Interval(**category_item))
        Interval.objects.bulk_create(categories_for_adding)
        self.stdout.write(self.style.SUCCESS('Database filled successfully.'))