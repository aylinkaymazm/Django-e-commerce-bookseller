from django.urls import path

from . import views

urlpatterns = [
    # ex: /home bunların hepsi polls değil/
    path('', views.index, name='index'),
    ]