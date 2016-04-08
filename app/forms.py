from django import forms

from .models import SimplePlace

class PlaceForm(forms.ModelForm):
	class Meta:
		model = SimplePlace
		fields = [
		'city',
		'skills',
		'location',
		]