from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:project_name>/details/", views.details, name="details"),
]

