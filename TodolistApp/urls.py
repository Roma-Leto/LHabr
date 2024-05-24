from django.urls import path

from TodolistApp.views import index

urlpatterns = [
    path("", index, name="index"),

]
