from rest_framework import serializers, response
from .models import Event
from users.serializers import CustomUserSerializer


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        # ['id', 'event_title', 'description', 'datetime', 'location',
        #           'max_participants', 'image', 'is_open', 'organizer', 'attendees']
        read_only_fields = ['id', 'attendees']

    attendees = CustomUserSerializer(many=True, read_only=True)

    def get_attendees(self, object):  # format of attendees as below. to inform front end team
        name = {
            'first_name': 'object.attendees.first_name',
            'last_name': 'object.attendees.last_name'
        }
        return (name)

    ######### BELOW COMMENTED OUT AS WE DON'T NEED THIS. IT WILL CLASH WITH BUILT IN MODEL SERIALIZER #########
    

    # def create(self, validated_data):
    #     event = Event.objects.create(
    #         title=validated_data['title'],
    #         description=validated_data['description'],
    #         max_participant=validated_data['max_participants'],
    #         image=validated_data['image'],
    #         is_open=validated_data['is_open'],
    #         datetime=validated_data['datetime'],
    #         organizer=validated_data['organizer'],
    #         sponsor=validated_data['sponsor']
    #     )
    #     event.save()
    #     return event
    
    
    # def update(self, instance, validated_data):
    #     instance.event_title = validated_data.get(
    #         'title', instance.event_title)
    #     instance.description = validated_data.get(
    #         'description', instance.description)
    #     instance.max_participants = validated_data.get(
    #         'max_participants', instance.max_participants)
    #     instance.image = validated_data.get('image', instance.image)
    #     instance.is_open = validated_data.get('is_open', instance.is_open)
    #     instance.datetime = validated_data.get('datetime', instance.datetime)
    #     instance.organizer = validated_data.get(
    #         'organizer', instance.organizer)
    #     instance.sponsor = validated_data.get(
    #         'sponsor', instance.sponsor)
    #     instance.save()
    #     return response(instance, status=200)
