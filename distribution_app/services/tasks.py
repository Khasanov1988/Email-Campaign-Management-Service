from distribution.models import Message, Settings, Interval


class Task:
    """
    Class describing tasks
    """
    def __init__(self, pk: int):
        # Describing attributes
        message = Message.objects.get(pk=pk)
        settings = Settings.objects.get(message=pk)
        interval = Interval.objects.get(message=pk)
        self.subject = message.subject
        self.text = message.text
        self.time = settings.distribution_time
