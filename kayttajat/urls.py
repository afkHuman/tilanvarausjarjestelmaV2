from django.urls import path
from . import views

urlpatterns = [
    # Main URL
    path('', views.main, name='main'),
    # Käyttäjät URLs
    path('kayttajat/', views.kayttajat, name='kayttajat'),
    path('kayttajat/details/<slug:slug>', views.details, name='details'),
    # Tilat URLs
    path('tilat/', views.tilat, name='tilat'),
]