from django.core.management import BaseCommand
from distribution.models import Message, Logs, Settings, Status
from services.crontask.crontask_job import crontab_job


class Command(BaseCommand):

    def add_arguments(self, parser):
        # Add command-line argument 'pk' to specify the primary key of the Message object
        parser.add_argument('pk', type=int, help='Primary key of the Message object', default=1)

    def handle(self, context_data={}, *args, **options):
        # Get the primary key 'pk' from the command-line arguments
        pk = options['pk']
        message = Message.objects.get(pk=pk)

        # Get or create a settings object for the message
        setting, created = Settings.objects.get_or_create(message=message)
        setting.distribution_status = Status.objects.get(status='started')
        setting.save()

        # Set the 'settings_list' key in the context_data
        context_data['settings_list'] = [setting]

        # Call the 'crontab_job' function with the context_data
        crontab_job(context_data)
