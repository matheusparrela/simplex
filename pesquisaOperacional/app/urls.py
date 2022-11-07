from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('createSimplex/', views.createSimplex, name='createSimplex'),
    #path('salvar/', views.salvar, name='salvar')
]

