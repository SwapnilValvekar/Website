from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('<int:couse_id>/', views.raj, name="Swapnil"),
    path('', views.courses, name="homepage"),
    path('hello/', views.hello),
    path('index/', views.index),
]
