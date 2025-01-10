from django.forms import ModelForm
from.models import *

class Study_form(ModelForm):

    class Meta:
        model= Study
        fields= '__all__'