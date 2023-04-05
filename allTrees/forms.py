from django import forms
from django.forms import ModelForm
from .models import *

class individualTrees_form(ModelForm):
    class Meta:
        model = individualTrees_model
        fields = ("__all__")
        widgets = {
            'treeID': forms.TextInput(),
            'rootStock': forms.TextInput(),
            'zionType': forms.TextInput(),
            'datePlanted': forms.DateInput(attrs={'type':'date'}),
        }
        
class locationTree_form(ModelForm):
    class Meta:
        model = locationTree_model
        fields = ("__all__")
        widgets = {
            'locationID':forms.TextInput(attrs={}),
            'name':forms.TextInput(),
            'address':forms.TextInput(),
            'city':forms.TextInput(),
            'state':forms.TextInput(),
            'dateEst':forms.DateInput(attrs={'type':'date'}),
        }
        
class areaTree_form(ModelForm):
    class Meta:
        model = areaTree_model
        fields = ("__all__")
        widgets = {
            'areaID': forms.TextInput(),
            'name': forms.TextInput(),
            'dateEst': forms.DateInput(attrs={'type':'date'}),
            'widthByTree': forms.NumberInput(),
            'lengthByTree': forms.NumberInput(),
        }
        
class logCategory_form(ModelForm):
    class Meta:
        model = logCategory_model
        fields = ("__all__")
        widgets = {
            'name': forms.TextInput(),
            'description': forms.TextInput(),
        }
        
        
class treeLogs_form(ModelForm):
    class Meta:
        model = treeLogs_model
        fields = ("__all__")
        widgets = {
            'treeID': forms.TextInput(),
            'date': forms.DateInput(attrs={'type':'date'}),
            'time': forms.TimeInput(attrs={'type':'time'}),
            'note': forms.TextInput(),
            'category': forms.Select(),
        }