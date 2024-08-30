from django.contrib import admin
from django.urls import path
from .views import ApartmentPage
from . import views
from django.conf import settings
from .views import custom_logout_view
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.conf.urls.static import static

app_name = 'account'
urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('dashboard/', views.dashboardPage, name='dashboard'),
    path('apartment/', ApartmentPage.as_view(), name='apartment'), 
    path('logout/', custom_logout_view, name='logout'),
    # Ensure the URL name and pattern are correct
    # path('apartment/<int:pk>/edit/', views.apartment_edit, name='edit_apartment'),
    # path('apartment/<int:pk>/delete/', views.apartment_delete, name='delete_apartment'),
    # Other URLs...
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
