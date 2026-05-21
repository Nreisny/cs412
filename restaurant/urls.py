from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path(r'', views.main, name="main"), # Main Page
    path(r'order/', views.order, name="order"), # Order Page
    path(r'submit/', views.submit, name="submit"), # Submit page
]