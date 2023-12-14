from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    re_path(r'servicios/', views.servicios, name='servicios'),
    re_path(r'contactos/', views.contactos, name='contactos'),
    re_path(r'recetas/', views.recetas, name='recetas'),
    re_path(r'parrilleros/', views.parrilleros, name='parrilleros'),
    re_path(r'disponibilidad/', views.disponibilidad, name='disponibilidad'),
    re_path(r'reserva/', views.reserva, name='reserva'),
    path('pagina1/', views.pagina1, name='pagina1'),
    path('pagina2/', views.pagina2, name='pagina2'),
    path('formulario/', views.formulario, name='formulario'),
    re_path(r'logout', views.logout, name="logout"),
    re_path(r'page2', views.views2, name="views2"),
    re_path(r'nosotros/', views.nosotros, name='nosotros'),
    re_path(r'change-password/', views.api_change_password,
        name='change-password')


]
