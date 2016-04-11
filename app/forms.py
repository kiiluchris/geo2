from django import forms


from .models import SimplePlace, Skills

class PlaceForm(forms.ModelForm):
	class Meta:
		model = SimplePlace
		fields = [
		'city',
		'location',
		'skills'
		]
		widgets = {
			'skills': forms.CheckboxSelectMultiple
		}