from django.urls import path
from . import views

urlpatterns = [
    path("dashboard", views.dashboard_view, name="dashboard"),
    path("addTree/<str:locationID2>/<str:areaID2>", views.addTree_view, name="addTree"),
    path("addLocation", views.addLocation_view, name="addLocation"),
    path("addArea/<str:locationID2>", views.addArea_view, name="addArea"),
    path("treeData/<str:locationID2>/<str:areaID2>/<str:treeID2>", views.treeData2_view, name="treeData"),
    path("treeLog/<str:locationID2>/<str:areaID2>/<str:treeID2>/<str:selector>", views.treeLog_view, name="treeLog"),
    path("addLog/<str:locationID2>/<str:areaID2>/<str:treeID2>", views.addLog2_view, name="addLog"),
]
