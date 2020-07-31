from django.urls import path

from . import views

urlpatterns = [
    # ex: /product bunların hepsi polls değil/
    path('', views.index, name='index'),
    ]