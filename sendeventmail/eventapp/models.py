from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Event(models.Model):
    event_type = models.CharField(max_length=50)
    date = models.DateField()

class EmailTemplate(models.Model):
    event_type = models.CharField(max_length=50)
    template = models.TextField()

