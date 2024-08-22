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
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('property_details/', views.property_details,name='property_details'),
]
