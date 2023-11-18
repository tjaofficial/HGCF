from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(individualTrees_model)
admin.site.register(locationTree_model)
admin.site.register(areaTree_model)
admin.site.register(logCategory_model)
admin.site.register(treeLogs_model)
admin.site.register(tree_qr)