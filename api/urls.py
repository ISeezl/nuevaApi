from django.urls import path
from .views import *
urlpatterns=[
    path('usuarios/', UsuarioView.as_view(),name="usuarios_list"),
    path('usuarios/<int:idUsuario>', UsuarioView.as_view(),name="usuarios_process")

]