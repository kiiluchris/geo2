from django.db import models

from django.contrib.auth.models import User

from django.conf import settings

from django.core.urlresolvers import reverse

# Without using spatial db
from django.db import models as pmodels
from location_field.models.plain import PlainLocationField

# Create your models here.
class Skills(pmodels.Model):
    skill = pmodels.CharField(max_length=255)
    def __unicode__(self):
        return self.skill

class SimplePlace(pmodels.Model):
    user =  pmodels.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    city = pmodels.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    skills = pmodels.ManyToManyField(Skills)

    def __unicode__(self):
    	return self.city

    def get_absolute_url(self):
		return reverse("page", kwargs={"id": self.id})

class Skill(pmodels.Model):
    skill = pmodels.ManyToManyField(SimplePlace)


        