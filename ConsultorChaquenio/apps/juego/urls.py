from django.urls import path, include
from django.contrib.auth import views as auth
from . import views

app_name = "juego"

urlpatterns = [

    path('inicio/', views.Home, name='inicio'),

    path('pregunta/', views.Juego, name="pregunta"),

    path('respuesta/', views.Respuesta_Seleccionada),

    path('detalles/', views.Detalles, name="detalles"),

    path('ranking/', views.Tabla, name="ranking"),
]