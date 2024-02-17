from django.urls import path
from . import views

urlpatterns = [
    path('ml/', views.ml, name='ml'),
    path('', views.mlapp, name='mlapp'),
    
]