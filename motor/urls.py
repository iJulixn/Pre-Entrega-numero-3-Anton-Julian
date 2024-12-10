from django.urls import path
from . import views
from .views import motorv8,motorv6,motori4,inicio,crear_motor_v8,crear_motor_v6,crear_motor_I4,listado_motoresi4,listado_motoresv6,listado_motoresv8,listado_motores

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path("motor_v8/",motorv8, name= "motor_v8"),
    path("motor_v6/",motorv6, name= "motor_v6"),
    path("motor_i4/",motori4, name="motor_i4"),

    path('crear_motorv8/',crear_motor_v8, name='crear_motorv8'),
    path('crear_motorv6/',crear_motor_v6, name='crear_motorv6'),
    path('crear_motori4/',crear_motor_I4, name='crear_motori4'),
    path('motores/listadov8/', views.listado_motoresv8, name='listado_motoresv8'),
    path('motores/listadov6/', views.listado_motoresv6, name='listado_motoresv6'),
    path('motores/listadoi4/', views.listado_motoresi4, name='listado_motoresi4'),
    path('motores/listado/', views.listado_motores, name='listado_motores'),
    
    
    



]