from django.urls import path
from .views import filmovi, filmovi_detaljno


app_name = 'filmovi'

urlpatterns = [
    path('filmovi/', filmovi, name='filmovi'),
    path('filmovi/<slug:slug>/', filmovi_detaljno, name='filmovi-detaljno'),

]