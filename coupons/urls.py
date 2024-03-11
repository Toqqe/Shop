from django.urls import path

from . import views

urlpatterns = [
    path('apply/', views.apply),
    path('remove/', views.remove)
]
