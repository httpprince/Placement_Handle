from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.cdashborad),
    path('addjob/',views.addjob),
    path('joblist/', views.joblist),

    ]