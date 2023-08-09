from datetime import datetime
from django.core.management import BaseCommand
from django.utils import timezone

from distribution.models import Message, Logs
from distribution_app import settings
from distribution_app.settings_local import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from users.models import User

import smtplib
from email.mime.text import MIMEText


class Command(BaseCommand):

    def add_arguments(self, parser):  # Добавляем аргументы
        parser.add_argument('pk', type=int, help='Primary key of the Message object', default=1)

    def handle(self, *args, **options):
        pk = options['pk']  # Получаем переданный аргумент pk
        message = Message.objects.get(pk=pk)
        email_list = User.objects.values_list('email', flat=True)

        msg = MIMEText(message.text)
        msg['Subject'] = message.subject
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = ', '.join(email_list)

        try:
            with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
                server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
                response = server.sendmail(settings.EMAIL_HOST_USER, email_list, msg.as_string())
                status = 'positive'
        except Exception as error:
            status = 'negative'
            response = error

        new_log = Logs(
            last_attempt_time=timezone.now(),
            last_attempt_status=status,
            last_attempt_response=str(response),
            message=message,
        )
        new_log.save()
