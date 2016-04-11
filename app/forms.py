from django import forms


from .models import SimplePlace, Skills

class PlaceForm(forms.ModelForm):
	queryset = Skills.objects.values('skill')
	CHOICES = []
	count = 0
	for choice in queryset:		
		CHOICES.append((count, choice['skill']))
		count += 1
	print CHOICES
	skills = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required= True, choices = CHOICES)
	class Meta:
		model = SimplePlace
		fields = [
		'city',
		'location',
		]