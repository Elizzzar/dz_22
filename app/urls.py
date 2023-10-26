from django.urls import path
from .views import dz_22
urlpatterns = [
    path('', dz_22, name='dz_22'),
]
