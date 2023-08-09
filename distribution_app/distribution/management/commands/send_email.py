from django.core.mail import send_mail
from django.core.management import BaseCommand
from argparse import ArgumentParser  # Импортируем argparse


from distribution.models import Message
from distribution_app import settings
from users.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):  # Добавляем аргументы
        parser.add_argument('pk', type=int, help='Primary key of the Message object', default=1)

    def handle(self, *args, **options):
        pk = options['pk']  # Получаем переданный аргумент pk
        values_list = User.objects.values_list('email', flat=True)
        send_mail(subject=Message.objects.get(pk=pk).subject,
                  message=Message.objects.get(pk=pk).text,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=list(values_list)
                  )

        '''
        subject='Поздравляю с успешной регистрацией на сайте SkyStore!',
                    message='Добро пожаловать',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[self.object.email],
        '''
