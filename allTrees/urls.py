from django.urls import path
from . import views

urlpatterns = [
    path("dashboard", views.dashboard_view, name="dashboard"),
    path("addTree", views.addTree_view, name="addTree"),
    path("addLocation", views.addLocation_view, name="addLocation"),
    path("addArea", views.addArea_view, name="addArea"),
]
