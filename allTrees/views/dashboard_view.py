from django.shortcuts import render
from ..models import individualTrees_model

def dashboard_view(request):
    treeData = individualTrees_model.objects.all()
    
    return render(request, 'dashboard.html', {
        'teeData': treeData
    })