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
        iList = {}
        for x in range(1,16):
            if 'iName'+ str(x) in dataCopy:
                iList[str(x)] = {
                    'name': dataCopy['iName'+ str(x)],
                    'qty': dataCopy['iQty'+ str(x)],
                    'notes': dataCopy['inotes'+ str(x)]
                }
        dataCopy['ingredients'] = iList
        dataCopy['equipment'] = iList
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