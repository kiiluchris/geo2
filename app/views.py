from django.shortcuts import render
from .models import SimplePlace
from django.shortcuts import render, get_object_or_404
from .forms import PlaceForm
import math

# Create your views here.
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