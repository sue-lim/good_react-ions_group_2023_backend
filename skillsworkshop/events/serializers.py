from rest_framework import serializers

from .models import Event
# UHWC from users.serializers import ("whatever sue has called it")


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'event_title', 'description', 'datetime', 'location',
                  'max_participants', 'image', 'is_open', 'organiser', 'attendees']
        read_only_fields = ['id', 'attendees']

    attendees = serializers.SerializerMethodField()

    def get_attendees(self, object):  # format of attendees as below. to inform front end team
        name = {
            'first_name': 'object.attendees.first_name',
            'last_name': 'object.attendees.last_name'
        }
        return (name)
