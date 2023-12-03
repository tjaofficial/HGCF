from django.shortcuts import render
from ..models import individualTrees_model, areaTree_model
from ..forms import individualTrees_form
from ..utils import alphabetKey
import json
from django.contrib.auth.decorators import login_required

lock = login_required(login_url='Login')

@lock
def addTree_view(request, locationID2, areaID2):
    print(locationID2)
    print(areaID2)
    addForm = individualTrees_form
    areaData = areaTree_model.objects.get(areaID=areaID2)
    treeData = individualTrees_model.objects.filter(locationID__locationID=locationID2, areaID__areaID=areaID2)
    print(treeData)
    treeList = []
    if treeData.exists():
        print("------------")
        for tree in treeData:
            if tree.locationID.locationID == locationID2 and tree.areaID.areaID == areaID2:
                treeList.append(tree.treeID)

    treeList = json.dumps(treeList)
    gridWidth = areaData.widthByTree
    
    def letterNumber(number):
        charNumber = 64 + number
        print(chr(charNumber))

    letterNumber(gridWidth)
    rowList = []
    for x in range(65, (65+gridWidth)):
        rowList.append(chr(x))
    print(rowList)

    gridlength = areaData.lengthByTree
    columnRange = range(1, int(gridlength) + 1)
    print(gridlength)
    print(treeList)

    if request.method == "POST":
        print('post')
    return render(request, 'addTree.html', {
        'columnRange': columnRange, 
        'rowList': rowList, 
        'addForm': addForm, 
        'treeData': treeData, 
        'locationID': locationID2, 
        'areaID': areaID2, 
        'gridWidth': gridWidth, 
        'gridlength': gridlength, 
        'treeList': treeList, 
        'gridRange': range(1,((gridlength*gridWidth)+1))
    })