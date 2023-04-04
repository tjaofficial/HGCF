from django.shortcuts import render, redirect
from ..forms import areaTree_form
from ..models import areaTree_model

def addArea_view(request, locationID2):
    addForm = areaTree_form
    areasData = areaTree_model.objects.all()
    
    if request.method == 'POST':
        formData = areaTree_form(request.POST)
        if formData.is_valid():
            formData.save()
            return redirect('addArea', locationID2)
    return render(request, 'addArea.html', {
        'addForm': addForm, 'areasData': areasData, 'locationID': locationID2
    })