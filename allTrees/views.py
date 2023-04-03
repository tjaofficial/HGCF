from django.shortcuts import render
from .models import individualTrees_model
from .forms import individualTrees_form

# Create your views here.
def dashboard_view(request):
    treeData = individualTrees_model.objects.all()
    
    return render(request, 'dashboard.html', {
        'teeData': treeData
    })
    
def addTree_view(request):
    
    return render(request, 'addTree.html', {
    })

def addLocation_view(request):
    
    return render(request, 'addLocation.html', {
    })

def addArea_view(request):
    
    return render(request, 'addArea.html', {
    })