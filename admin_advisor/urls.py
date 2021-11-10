from django.urls import path

from . import views


urlpatterns = [

    path("", views.add_name, name="add_name"),
    #path("/add", views.add_name, name="add_name")

]