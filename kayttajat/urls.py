from django.urls import path
from . import views

urlpatterns = [
    path('kayttajat/', views.kayttajat, name='kayttajat'),
    path('kayttajat/details/<int:id>', views.details, name='details'),
]