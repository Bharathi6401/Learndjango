# from django.forms import ModelForm
# from django import forms
# from .models import *
#
# class Students_Form(forms.ModelForm):
#
#     class Meta:
#         model = models
#         fields = '__all__'
#
#
#

# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import *


# create a ModelForm
class Students_Form(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Students
        fields = "__all__"
