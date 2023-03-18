from django.db import models

# Create your models here.

# User = get_user_model() - to unhash when merged with user (TUWM)

class Event(models.model):
    event_title = models.CharField(max_length=200)
    description = models.Textfield()
    datetime = #find on google
    location = models.CharField(max_length=200)
    max_participants = models.CharField(max_length=200) #should be integer
    image = models.URLField()
    is_open = models.BooleanField()
    # organiser = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name='organiser'
    # ) UHWC
    # attendees = models.ManyToManyField(
    #     User,
    #     related_name='attendee'
    # )
