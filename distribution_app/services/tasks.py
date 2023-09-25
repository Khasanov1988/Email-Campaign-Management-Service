from distribution.models import Message, Settings, Interval


class Task:
    """
    Class describing tasks for email distribution.
    """

    def __init__(self, pk: int):
        """
        Initializes a Task object with information from Message, Settings, and Interval models.

        Args:
            pk (int): Primary key of the Message object.
        """
        # Fetch relevant data from the database
        message = Message.objects.get(pk=pk)
        settings = Settings.objects.get(message=pk)
        interval = Interval.objects.get(message=pk)

        # Store task attributes
        self.subject = message.subject  # Subject of the email message
        self.text = message.text  # Body text of the email message
        self.time = settings.distribution_time  # Time at which the email should be sent
