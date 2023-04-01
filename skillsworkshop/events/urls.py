from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('events/', views.EventList.as_view(), name="events-list"),
    path('events-public/', views.EventListPublic.as_view(), name="events-public"),
    path('events/<int:pk>/', views.EventDetail.as_view(), name="event-detail"),
]

# format_suffix_patterns helps django format patterns properly?
urlpatterns = format_suffix_patterns(urlpatterns)
