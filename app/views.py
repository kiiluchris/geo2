from django.shortcuts import render
from .models import SimplePlace
from django.shortcuts import render, get_object_or_404
from .forms import PlaceForm
import math

# Calendar imports

import calendar
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape as esc

# Create your views here.
def home(request):
	form = PlaceForm(data = request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		form.save_m2m()

	places = SimplePlace.objects.all()
	# my_workouts = Workouts.objects.order_by('my_date').filter(
 #    	my_date__year=year, my_date__month=month
 #  	)
	# cal = WorkoutCalendar(my_workouts).formatmonth(year, month)
	context = {
		'queryset': places,
		'form':form,
		# 'calendar': mark_safe(cal),
	}
	return render(request, "home.html", context)

def page(request, id = None):
	place = get_object_or_404(SimplePlace, id = id)
	# current_lat =  place.location.split(",")[0]
	# current_lng =  place.location.split(",")[1]
	# print "Current_Lng: ", float(current_lng), "Current_Lat: ", float(current_lat)

	# # query = "SELECT *, ( 3959 * acos( cos( radians(" . $lat . ") ) * cos( radians( lat ) ) * cos( radians( lng ) - radians(" . $lng . ") ) + sin( radians(" . $lat . ") ) * sin( radians( lat ) ) ) ) AS distance FROM your_table HAVING distance < 5";
	# # near = SimplePlace.objects.raw(query):
	# near = SimplePlace.objects.values('location')

	context = {
		"place":place,
		# 'near':near,
	}
	return render(request, "page2.html", context)




# Django calendar

# class WorkoutCalendar(HTMLCalendar):

#     def __init__(self, workouts):
#         super(WorkoutCalendar, self).__init__()
#         self.workouts = self.group_by_day(workouts)

#     def formatday(self, day, weekday):
#         if day != 0:
#             cssclass = self.cssclasses[weekday]
#             if date.today() == date(self.year, self.month, day):
#                 cssclass += ' today'
#             if day in self.workouts:
#                 cssclass += ' filled'
#                 body = ['<ul>']
#                 for workout in self.workouts[day]:
#                     body.append('<li>')
#                     body.append('<a href="%s">' % workout.get_absolute_url())
#                     body.append(esc(workout.title))
#                     body.append('</a></li>')
#                 body.append('</ul>')
#                 return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
#             return self.day_cell(cssclass, day)
#         return self.day_cell('noday', '&nbsp;')

#     def formatmonth(self, year, month):
#         self.year, self.month = year, month
#         return super(WorkoutCalendar, self).formatmonth(year, month)

#     def group_by_day(self, workouts):
#         field = lambda workout: workout.performed_at.day
#         return dict(
#             [(day, list(items)) for day, items in groupby(workouts, field)]
#         )

#     def day_cell(self, cssclass, body):
#         return '<td class="%s">%s</td>' % (cssclass, body)