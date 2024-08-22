from django.contrib import admin
from django.urls import path, include
from .views import ApartmentPage
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'account'

urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('dashboard/', views.dashboardPage, name='dashboard'),
    path('Apartment/', ApartmentPage.as_view(), name='apartment')
    
]

urlpatterns = [
    # ... your url patterns ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)