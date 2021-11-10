from django.urls import path

from . import views


urlpatterns = [

    path("", views.register_index, name="register_index"),
    path("register/",views.register_new, name="register"),
    path("login/",views.login_new, name="login"),
    path("advisor/",views.advisor_index, name="advisor"),
    path("<int:user_id>/advisor/<int:advisor_id>",views.book_advisor, name="book_advisor"),
    #path("<int:user_id>/advisor/booking",views.booking_index, name="booking index"),
    #path("/add", views.add_name, name="add_name")
]
