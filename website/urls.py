from django.contrib import admin
from django.urls import path
from . import views
app_name ='website'

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('properties/', views.properties, name='properties'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('blog/', views.blog, name='blog'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('terms/', views.terms, name='terms'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('register/', views.register, name='register'),
    path('property_details/', views.property_details,name='property_details'),
    path('dashboard/' ,views.dashboard ,name='dashboard'),
    path('apartment', views.apartment,name='apartment'),
    path('payment1/', views.paymentPage,name='payment1'),
    path('payment-history/', views.payment_history, name='payment_history'),
    
]
