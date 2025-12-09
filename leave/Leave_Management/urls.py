from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('apply/', views.apply_leave, name='apply_leave'),
    path('cancel/<int:pk>/', views.cancel_leave, name='cancel_leave'),
    path('approve/<int:pk>/', views.approve_leave, name='approve_leave'),
    path('register/', views.register, name='register'),
]
