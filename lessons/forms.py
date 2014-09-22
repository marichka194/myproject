from django.forms import ModelForm
from lessons.models import Person

__author__ = 'Admin'

class PersonEditingForm(ModelForm):
    class Meta:
        model = Person