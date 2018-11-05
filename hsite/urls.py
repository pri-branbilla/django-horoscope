from django.urls import path
from . import views

urlpatterns = [
    path('',  views.MainPage, name="Home"),
    path('Contato/', views.Contato, name="Contato"),
    path('TodosSignos/', views.MostrarTodos, name="TodosSignos"),
    path('TodosSignos/<str:signo>/', views.MostrarTodosSelect, name="TodosSignos"),
    path('DescobrirSigno/', views.DescobrirSigno, name="DescobrirSigno"),
]
