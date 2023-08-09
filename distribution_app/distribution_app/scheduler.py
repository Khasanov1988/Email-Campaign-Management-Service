import schedule
import time
from distribution.models import Message
from users.models import User
from distribution_app import settings
from django.core.mail import send_mail

# Импортируем список задач из settings_cron.py
from settings_cron import CRONJOBS


def send_email_task(pk):
    values_list = User.objects.values_list('email', flat=True)
    message = Message.objects.get(pk=pk)
    send_mail(
        subject=message.subject,
        message=message.text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=list(values_list)
    )


# Определяем задачи из списка
for cronjob in CRONJOBS:
    schedule.every().cron(cronjob[0]).do(
        send_email_task,
        pk=int(cronjob[2]),  # Преобразовываем строку в целое число
    )

while True:
    schedule.run_pending()
    time.sleep(1)
