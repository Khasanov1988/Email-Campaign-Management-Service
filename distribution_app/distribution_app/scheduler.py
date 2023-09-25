import schedule
import time
from distribution.models import Message
from users.models import User
from distribution_app import settings
from django.core.mail import send_mail

# Import task list from settings_cron.py
from settings_cron import CRONJOBS


def send_email_task(pk):
    """
    Function to send emails to all users with a given message.

    Args:
        pk (int): Primary key of the message to be sent.

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


# Define tasks from the CRONJOBS list
for cronjob in CRONJOBS:
    schedule.every().cron(cronjob[0]).do(
        send_email_task,
        pk=int(cronjob[2]),  # Convert the string to an integer
    )

while True:
    schedule.run_pending()
    time.sleep(1)
