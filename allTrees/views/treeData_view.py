from django.shortcuts import render
from ..models import individualTrees_model, areaTree_model, locationTree_model, treeLogs_model

def treeData2_view(request, locationID2, areaID2, treeID2):
    treeData = individualTrees_model.objects.get(locationID__locationID=locationID2, areaID__areaID=areaID2, treeID=treeID2)
    treeLogs = treeLogs_model.objects.all().filter(treeID__locationID__locationID=locationID2, treeID__areaID__areaID=areaID2, treeID__treeID=treeID2).order_by('-date')
    print(treeLogs)
    return render(request, 'treeData.html',{
        'treeLogs': treeLogs, 'locationID': locationID2, 'areaID': areaID2, 'treeID': treeID2, 'treeData': treeData
    })
    
def treeLog_view(request, locationID2, areaID2, treeID2, selector):
    if selector == 'all':
        treeLogData = treeLogs_model.objects.all().filter(treeID__locationID__locationID=locationID2, treeID__areaID__areaID=areaID2, treeID__treeID=treeID2).order_by('-date')
        variables = {
            'locationID': locationID2, 
            'areaID': areaID2, 
            'treeID': treeID2, 
            'selector': selector,
            'treeLogData': treeLogData,
        }
    else:
        treeLog = treeLogs_model.objects.get(id=int(selector))
        variables = {
            'locationID': locationID2, 
            'areaID': areaID2, 
            'treeID': treeID2, 
            'treeLog': treeLog,
            'selector': selector,
        }
    print(selector)
    return render(request, 'treeLog.html', variables)