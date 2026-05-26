from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
 path(r"", views.ProfileListView.as_view(), name="show_all_profile"),
 path(r"profile/<int:pk>", views.ProfileDetailView.as_view(), name="show_profile")
]