from django.urls import path

from .views import *

urlpatterns = [
    path('', calculator, name='calculator'),
    path('viewcalc/', view_calculator, name='view_calculator'),
]