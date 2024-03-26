from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('participantes', views.list_participantes, name='participantes'),
    
]