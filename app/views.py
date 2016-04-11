# Rendering views
from django.shortcuts import render
from .models import SimplePlace
from django.shortcuts import render, get_object_or_404
from .forms import PlaceForm

# Math class
import math

# Swingtime imports
from datetime import datetime, timedelta
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render

from swingtime import models as swingtime

#-------------------------------------------------------------------------------
def event_type(request, abbr):
    event_type = get_object_or_404(swingtime.EventType, abbr=abbr)
    now = datetime.now()
    occurrences = swingtime.Occurrence.objects.filter(
        event__event_type=event_type,
        start_time__gte=now,
        start_time__lte=now+timedelta(days=+30)
    )
    print occurrences
    return render(request, 'upcoming_by_event_type.html', {
        'occurrences': occurrences,
        'event_type': event_type
    })


def home(request):
	form = PlaceForm(data = request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		form.save_m2m()

	places = SimplePlace.objects.all()
	context = {
		'queryset': places,
		'form':form,
		# 'calendar': calendar(2016, 'March'),
	}
	return render(request, "home.html", context)

def page(request, id = None):
	current_place = get_object_or_404(SimplePlace, id = id)
	current_lat =  current_place.location.split(",")[0]
	current_lng =  current_place.location.split(",")[1]

	other_places = SimplePlace.objects.values('location', 'city')
	nearby_places = []

	for place in other_places:
		lat = place['location'].split(",")[0]
		lng = place['location'].split(",")[1]
		# Calculate places within a certain distance
		distance = calc_dist(float(current_lat), float(current_lng), float(lat), float(lng))

		if distance < 50.0 and current_place.city != place['city']:
			nearby_places.append(place)

	# Remove duplicates
	nearby_places = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in nearby_places)]

	context = {
		"current_place":current_place,
		'other_places':nearby_places,
	}
	return render(request, "page2.html", context)

# def km2mile(x):
# 	'''a function to convert km to mile'''
# 	return int(x * 0.621371)

def calc_dist(lat1, lon1, lat2, lon2):
	'''a function to calculate the distance in miles between two 
	points on the earth, given their latitudes and longitudes in degrees'''


	# covert degrees to radians
	lat1 = math.radians(lat1)
	lon1 = math.radians(lon1)
	lat2 = math.radians(lat2)
	lon2 = math.radians(lon2) 

	# get the differences
	delta_lat = lat2 - lat1 
	delta_lon = lon2 - lon1 

	# Haversine formula, 
	# from http://www.movable-type.co.uk/scripts/latlong.html
	a = ((math.sin(delta_lat/2))**2) + math.cos(lat1)*math.cos(lat2)*((math.sin(delta_lon/2))**2) 
	c = 2 * math.atan2(a**0.5, (1-a)**0.5)
	# earth's radius in km
	earth_radius = 6371
	# return distance in miles
	return earth_radius * c
	# return km2mile(earth_radius * c)
