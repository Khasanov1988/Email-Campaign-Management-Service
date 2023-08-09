CRONJOBS = [
    ('*/5 * * * *', 'distribution_app.cron.other_scheduled_job', 'pk=1'),
    ('0   4 * * *', 'django.core.management.call_command', 'send_email', 'pk=1'),
]
