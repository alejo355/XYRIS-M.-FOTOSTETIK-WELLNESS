from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('login/', views.login, name='login'),
    path('inicio', views.inicio, name='inicio'),
]