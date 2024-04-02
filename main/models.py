from django.db import models
from simple_history.models import HistoricalRecords

# https://django-simple-history.readthedocs.io/en/latest/index.html


class Ticket(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    tickets = models.ManyToManyField(Ticket, related_name="events")
    history = HistoricalRecords(m2m_fields=[tickets])

    def __str__(self):
        return self.title

    @property
    def all_tickets_in_history(self):
        last_history_event = self.history.latest()
        ticket_ids = last_history_event.tickets.values_list("id", flat=True)
        return Ticket.objects.filter(id__in=ticket_ids)
