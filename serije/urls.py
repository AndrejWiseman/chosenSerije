from django.urls import path
from .views import serije


app_name = 'serije'

urlpatterns = [
    path('serije/', serije, name='serije' )
]
