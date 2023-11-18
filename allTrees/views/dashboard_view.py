from django.shortcuts import render
from ..models import individualTrees_model
from django.contrib.auth.decorators import login_required

lock = login_required(login_url='Login')

@lock
def dashboard_view(request):
    treeData = individualTrees_model.objects.all()
    
    return render(request, 'dashboard.html', {
        'teeData': treeData
    })