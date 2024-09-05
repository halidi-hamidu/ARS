from django.contrib import admin
from django.urls import path
from .views import ApartmentPage
from . import views
from django.conf import settings
from .views import custom_logout_view
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.conf.urls.static import static
from .views import delete_apartment

app_name = 'account'
urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('dashboard/', views.dashboardPage, name='dashboard'),
    path('apartment/', ApartmentPage.as_view(), name='apartment'), 
    path('logout/', custom_logout_view, name='logout'),
    path('apartment/<str:id>/delete/', delete_apartment, name='delete_apartment'),
#path('delete_apartment/<int:id>/', views.delete_apartment, name='delete_apartment'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
