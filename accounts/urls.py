from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
    path('hiaub/', views.index),
    path('indexTour/', views.indexTour)
]