from django.contrib import admin

# Register your models here.
from .models import Topic, Event

admin.site.register(Topic)
admin.site.register(Event)