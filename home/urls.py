from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='Home'),
    path("about",views.about, name='About'),
    path("contact",views.contact, name='Contact'),
    path("service",views.service, name='Services'),
    path("login",views.loginUser, name='login'),
    path("logout",views.logoutUser, name='logout'),
    path("store",views.store, name='store'),
]
