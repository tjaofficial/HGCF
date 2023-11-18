from django.shortcuts import render, redirect
from ..forms import areaTree_form
from ..models import areaTree_model, locationTree_model
from ..utils import selectNextID
from django.contrib.auth.decorators import login_required

lock = login_required(login_url='Login')

@lock
def addArea_view(request, locationID2):
    addForm = areaTree_form
    areasData = areaTree_model.objects.filter(locationID=locationID2)
    location = locationTree_model.objects.get(locationID=locationID2)
    newID = selectNextID(areasData.order_by('-areaID'), 'area')
    print(newID)
    if request.method == 'POST':
        print(request.POST)
        formData = areaTree_form(request.POST)
        print(formData.errors)
        if formData.is_valid():
            print('Hello')
            formData.save()
            return redirect('addArea', locationID2)
    return render(request, 'addArea.html', {
        'newID': newID, 'location': location, 'addForm': addForm, 'areasData': areasData, 'locationID': locationID2
    })