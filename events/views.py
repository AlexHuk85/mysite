from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar
from .models import Event
# Create your views here.

def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 2000 or year >2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "My club Event Calender - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    announcements = [
        {
            'date': '7-5-2021',
            'announcement': "Club Registrations Open"
        },
        {
            'date': '7-1-2021',
            'announcement': "Joe Smith Elected New Club President"
        }
    ]
    #return HttpResponse('<h1>%s</h1><p>%s</p>' % (title, cal))
    return render(request, 'events/calender.html', {'title': title, 'cal': cal, 'announcements': announcements})

def all_events(request):
    event_list = Event.objects.all()
    return render(request,
        'events/event_list.html',
        {'event_list':event_list})