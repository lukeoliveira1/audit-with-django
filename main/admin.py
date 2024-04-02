from django.contrib import admin

from main.models import Event, Ticket

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Event)