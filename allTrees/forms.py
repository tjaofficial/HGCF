from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
            'password1': forms.TextInput(attrs={'type': 'password', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }
        
class recipeForm(ModelForm):
    class Meta:
        model = recipeModel
        fields = ("__all__")
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'recipe name'}),
            'ingredients': forms.TextInput(),
            'equipment': forms.TextInput(),
            'serving_size': forms.NumberInput(attrs={'placeholder':'serving #'}),
            'time': forms.TextInput(attrs={'placeholder':'HH:MM'}),
            'meal_type': forms.Select(),
            'directions': forms.Textarea(),
            'special_notes': forms.TextInput(),
            'healthy_choice': forms.Select(),
            'description': forms.TextInput(),
            'cuisine': forms.TextInput(),
            'freezer_friendly': forms.TextInput(),
        }