from django.shortcuts import render, redirect
from ..forms import locationTree_form
from ..models import locationTree_model

def addLocation_view(request):
    addForm = locationTree_form
    locationsData = locationTree_model.objects.all()
    
    if request.method == 'POST':
        formData = locationTree_form(request.POST)
        if formData.is_valid():
            formData.save()
            return redirect('addLocation')
        
    return render(request, 'addLocation.html', {
        'addForm': addForm, 'locationsData': locationsData
    })