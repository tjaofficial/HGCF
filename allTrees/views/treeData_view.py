from django.shortcuts import render
from ..models import individualTrees_model, areaTree_model, locationTree_model

def treeData_view(request, locationID2, areaID2, treeID2):
    treeData = individualTrees_model.objects.get(locationID__locationID=locationID2, areaID__areaID=areaID2, treeID=treeID2)
    print(treeData)
    return render(request, 'treeData.html',{
        'locationID2': locationID2, 'areaID2': areaID2, 'treeID2': treeID2, 'treeData': treeData
    })