from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    # path('<str:stateName>/', views.stateView, name='stateView'),
]
