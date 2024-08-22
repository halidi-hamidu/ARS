from django.contrib import admin
from django.urls import path, include
from .views import ApartmentPage
from . import views


app_name = 'account'

urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('dashboard/', views.dashboardPage, name='dashboard'),
    path('Apartment/', ApartmentPage.as_view(), name='apartment')
    
]
