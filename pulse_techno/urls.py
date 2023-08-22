from django.urls import path

from pulse_techno.views import *

urlpatterns = [
    path('', index, name='home'),

]
