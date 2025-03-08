from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('blobe/',views.opachki),
    path('',views.houm_paij,name = "home"),
    path('hajapuri_pa_ajarske',views.shef_uzbek,name = "add_page"),
    path('',views.shpaga_praga,name = "posts"),
    path('post/<int:postid>',views.sho_post,name = "post"),
    path('contact/',views.way_of_nothing,name = "contact"),
    path('login/',views.login,name = "login")
]
