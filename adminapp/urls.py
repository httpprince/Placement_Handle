from django.urls import path

from .views import *

urlpatterns = [
    path('',adashboard),
    path('addplacementcell/',addplacementcell),
    path('viewplacementcells/',viewplacementcells),
    ]