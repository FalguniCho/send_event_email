from django.urls import path
from .views import send_event_emails, home,EventList

urlpatterns = [
    path('', home, name='home'),
    path('send_event_emails/', send_event_emails, name='send_event_emails'),
    path('api/events/', EventList.as_view(), name='event-list'),
]
