from django.urls import path
from .views import serije, serije_detaljno


app_name = 'serije'

urlpatterns = [
    path('serije/', serije, name='serije'),
    path('serije/<slug:slug>/', serije_detaljno, name='serije-detaljno'),

]
