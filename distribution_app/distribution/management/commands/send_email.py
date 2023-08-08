from django.core.mail import send_mail
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_mail(*args, **options)

        '''
        subject='Поздравляю с успешной регистрацией на сайте SkyStore!',
                    message='Добро пожаловать',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[self.object.email],
        '''
