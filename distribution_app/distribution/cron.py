from django.core.mail import send_mail
from distribution.models import Message
from distribution_app import settings
from users.models import User


def my_scheduled_job(pk):
    """
    A scheduled job to send an email with a specific message to all users.

    Args:
        pk (int): The primary key of the message to be sent.

    Note:
        - Retrieves a list of email addresses of all users.
        - Retrieves the message by its primary key (pk).
        - Sends the message to all addresses in the list.
    """
    values_list = User.objects.values_list('email', flat=True)
    message = Message.objects.get(pk=pk)
    send_mail(
        subject=message.subject,
        message=message.text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=list(values_list)
    )
