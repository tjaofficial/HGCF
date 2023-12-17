from django.shortcuts import render, redirect
from ..models import recipeModel
from ..forms import recipeForm
from django.contrib.auth.decorators import login_required

lock = login_required(login_url='Login')

@lock
def recipeForm_view(request):
    noFooter = True
    smallHeader = True
    sideBar = True
    form = recipeForm
    modelData = recipeModel.objects.all()
    if request.method == "POST":
        dataCopy = request.POST.copy()
        print(dataCopy)
        iList = {}
        for x in range(1,16):
            if 'iName'+ str(x) in dataCopy:
                iList[str(x)] = {
                    'name': dataCopy['iName'+ str(x)],
                    'qty': dataCopy['iQty'+ str(x)],
                    'notes': dataCopy['iNotes'+ str(x)]
                }
        dataCopy['ingredients'] = iList
        eList = {}
        for x in range(1,16):
            if 'eName'+ str(x) in dataCopy:
                eList[str(x)] = {
                    'name': dataCopy['eName'+ str(x)],
                    'qty': dataCopy['eQty'+ str(x)],
                    'notes': dataCopy['eNotes'+ str(x)]
                }
        dataCopy['equipment'] = eList
        data = recipeForm(dataCopy)
        if data.is_valid():
            print('saved')
            data.save()
        else:
            print(data.errors)
                
        
    
    return render(request, "recipes/recipeForm.html", {
        'smallHeader': smallHeader,
        'noFooter': noFooter,
        'sideBar': sideBar,
        'form': form,
        'modelData': modelData
    })
    
def recipeForm_view(request):
    noFooter = True
    smallHeader = True
    sideBar = True
    
    return render(request, "recipes/recipeForm.html", {
        'smallHeader': smallHeader,
        'noFooter': noFooter,
        'sideBar': sideBar,
})