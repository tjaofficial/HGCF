from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage_view, name="home"),
    path("dashboard", views.dashboard_view, name="dashboard"),
    path("announcements", views.announcements_view, name="announcements"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="Logout"),
    path("addTree/<str:locationID2>/<str:areaID2>", views.addTree_view, name="addTree"),
    path("addLocation", views.addLocation_view, name="addLocation"),
    path("addArea/<str:locationID2>", views.addArea_view, name="addArea"),
    path("treeData/<str:locationID2>/<str:areaID2>/<str:treeID2>", views.treeData2_view, name="treeData"),
    path("treeLog/<str:locationID2>/<str:areaID2>/<str:treeID2>/<str:selector>", views.treeLog_view, name="treeLog"),
    path("addLog/<str:locationID2>/<str:areaID2>/<str:treeID2>", views.addLog2_view, name="addLog"),
    
    #Joyces Kitchen URLs
    path("recipeForm", views.recipeForm_view, name="recipeForm"),
    path("recipes/<str:recipe>", views.recipeInfo_view, name="recipeInfo"),
    
    #Environmental URLs
    path("weatherDash", views.weather_dashboard_view, name="weatherDash"),
    
    #Stores
    path("addProduct", views.addProduct_view, name="addProduct"),
    path("store", views.store_view, name="store"),
]

