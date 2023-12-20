from django.shortcuts import render
from ..models import individualTrees_model, locationTree_model, areaTree_model
from django.contrib.auth.decorators import login_required

lock = login_required(login_url='Login')

@lock
def dashboard_view(request):
    treeData = individualTrees_model.objects.all()
    locationData = locationTree_model.objects.filter(locationID=1)
    areaData = areaTree_model.objects.all()[3]
    noFooter = True
    smallHeader = True
    sideBar = True
    
    
    
    return render(request, 'dashboard.html', {
        'teeData': treeData, 
        'noFooter': noFooter, 
        'smallHeader': smallHeader,
        'sideBar': sideBar,
        'locationData': locationData,
        'areaData': areaData,
    })