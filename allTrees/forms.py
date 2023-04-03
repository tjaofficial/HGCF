from django import forms
from django.forms import ModelForm
from .models import *

class individualTrees_form(forms.ModelForm):
    class Meta:
        model = individualTrees_model
        fields = "__all__"
        widget = {
            'treeID': forms.CharField(),
            'rootStock': forms.CharField(),
            'zionType': forms.CharField(),
            'datePlanted': forms.CharField(),
        }