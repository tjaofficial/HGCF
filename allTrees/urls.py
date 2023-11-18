from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.homePage_view, name="home"),
    path("dashboard", views.dashboard_view, name="dashboard"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="Logout"),
=======
    path("dashboard", views.dashboard_view, name="dashboard"),
>>>>>>> 7aa6b663ee8dc078e4be5be585a0156e634083f2
    path("addTree/<str:locationID2>/<str:areaID2>", views.addTree_view, name="addTree"),
    path("addLocation", views.addLocation_view, name="addLocation"),
    path("addArea/<str:locationID2>", views.addArea_view, name="addArea"),
    path("treeData/<str:locationID2>/<str:areaID2>/<str:treeID2>", views.treeData2_view, name="treeData"),
    path("treeLog/<str:locationID2>/<str:areaID2>/<str:treeID2>/<str:selector>", views.treeLog_view, name="treeLog"),
    path("addLog/<str:locationID2>/<str:areaID2>/<str:treeID2>", views.addLog2_view, name="addLog"),
]
