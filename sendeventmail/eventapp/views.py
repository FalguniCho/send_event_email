from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Event, Employee, EmailTemplate
import datetime

@csrf_exempt
def send_event_emails(request):
    current_date = datetime.date.today()
    events = Event.objects.filter(date=current_date)

    for event in events:
        employees = Employee.objects.all()
        email_template = EmailTemplate.objects.get(event_type=event.event_type)

        for employee in employees:
            email_content = email_template.template.format(
                employee_name=employee.name,
                event_type=event.event_type,
                event_date=event.date
            )

            try:
                send_mail(
                    f"Event Reminder: {event.event_type}",
                    email_content,
                    "your_email@example.com",
                    [employee.email],
                    fail_silently=False,
                )
                # Log successful email sending here
            except Exception as e:
                # Log error here and optionally retry
                pass

    return JsonResponse({"message": "Event emails sent successfully."})

def home(request):
    return render(request, 'eventapp/home.html')

from rest_framework import generics
from .models import Event
from .serializers import EventSerializer

class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
