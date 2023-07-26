from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('doctors', views.doctors, name='doctors'),
    path('departments/', views.departments, name='departments'),
    path('contact/', views.contact, name='contact'),
]
