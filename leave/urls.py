from django.urls import path 
from . import views

urlpatterns = [
    path('staff-dashboard/', views.staffDashboard, name='staffDashboard'),
    path('new-leave/', views.new_leave, name='new_leave'),
    path('staff-dashboard/<int:leave_id>/', views.view_leave, name='view_leave'),

    path('approved-leaves/', views.approved_leaves, name='approved_leaves'),
    path('pending-leaves/', views.pending_leaves, name='pending_leaves'),
]