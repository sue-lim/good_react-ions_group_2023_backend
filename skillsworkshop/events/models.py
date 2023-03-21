from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.model):
    event_title = models.CharField(max_length=200)
    description = models.Textfield()
    datetime = models.DateTimeField()
    location = models.CharField(max_length=200)
    max_participants = models.CharField(max_length=200)  # should be integer
    image = models.URLField()
    is_open = models.BooleanField()
    organiser = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='organiser'
    )
    attendees = models.OneToManyField(
        User,
        related_name='attendee',
        on_delete=models.CASCADE,
    )


@property
def max_capacity(self):
    # how to add max participants
    return self.max_participants.aggregate(sum=models.sum('max_participant'))['sum']
