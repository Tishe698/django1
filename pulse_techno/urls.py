from django.urls import path

from pulse_techno.views import *

urlpatterns = [
    path('', index, name='home'),
    path('send-to-telegram/', send_to_telegram, name='send_to_telegram'),
    path('uspeh', uspeh, name='uspeh'),
    path('landing', landing, name='landing'),
    path('korparativ', korparativ, name='korparativ'),
    path('online_shop', online_shop, name='online_shop'),

]
