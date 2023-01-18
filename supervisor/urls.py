from django.urls import path 
from . import views

urlpatterns = [
    path('supervisor-dashboard/', views.supervisorDashboard, name='supervisorDashboard'),
]