from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.pdashboard),
    path('addcompany/',views.addcompany),
    path('viewcompany/',views.viewcompany),
    path('addstudent/',views.addstudent),
    path('viewstudent/', views.viewstudent),


]