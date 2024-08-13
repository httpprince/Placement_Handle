from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.sdashboard),
    path('job/',views.joblist),
    ]