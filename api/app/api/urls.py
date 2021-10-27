from django.urls import path

from . import views

urlpatterns = [
    path("reading", views.reading, name="reading"),
    path("readings", views.readings, name="readings"),
]
