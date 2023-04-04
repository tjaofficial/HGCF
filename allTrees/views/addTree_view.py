from django.shortcuts import render
from ..models import individualTrees_model, areaTree_model
from ..forms import individualTrees_form

def addTree_view(request, locationID2, areaID2):
    addForm = individualTrees_form
    areaData = areaTree_model.objects.get(areaID=areaID2)
    treeData = individualTrees_model.objects.all()
    treeList = []
    for tree in treeData:
        if tree.locationID.locationID == locationID2 and tree.areaID.areaID == areaID2:
            treeList.append(tree)
    gridWidth = areaData.widthByTree
    gridlength = areaData.lengthByTree
    print(treeList)
    return render(request, 'addTree.html', {
        'addForm': addForm, 'treeData': treeData, 'locationID': locationID2, 'areaID': areaID2, 'gridWidth': gridWidth, 'gridlength': gridlength, 'treeList': treeList 
    })