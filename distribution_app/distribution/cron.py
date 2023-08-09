from django.core.mail import send_mail

from distribution.models import Message
from distribution_app import settings
from users.models import User


def my_scheduled_job(pk):
    values_list = User.objects.values_list('email', flat=True)
    send_mail(subject=Message.objects.get(pk=pk).subject,
              message=Message.objects.get(pk=pk).text,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=list(values_list)
              )
