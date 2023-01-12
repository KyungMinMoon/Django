# hello / urls.py

from django.urls import path
from . import views

urlpatterns = [
    # FULL URL
    # hello/world => views.py / hello_world
    path('world/', views.hello_world),
    # hello/lunch 
    path('lunch/', views.lunch),

    path('lotto/', views.lotto),
]