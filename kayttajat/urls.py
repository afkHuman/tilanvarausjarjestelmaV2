from django.urls import path
from . import views

urlpatterns = [
    # Main URL
    path('', views.main, name='main'),
    # Käyttäjät URLs
    path('kayttajat/', views.kayttajat, name='kayttajat'),
    path('kayttajat/users_details/<slug:slug>', views.users_details, name='users_details'),
    # Tilat URLs
    path('tilat/', views.tilat, name='tilat'),
    path('tilat/spaces_details/<slug:slug>', views.spaces_details, name='spaces_details'),
]