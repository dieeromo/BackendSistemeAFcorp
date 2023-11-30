
from django.urls import path
from . import views

urlpatterns = [
    path('listnivel/', views.listNivel),
    path('listred/', views.listRed),
    path('listnodo/', views.listNodo),
    path('listtipo/', views.lisTipoIncidente),
    path('regincidente/<int:pkNivel>/<int:pkRed>/<int:pkNodo>/<int:pkTipo>/', views.registroIncidentes),
    path('listincidente/', views.listIncidente),
    ## BITACORA EQUIPOS
    path('reg_equipo_red/<int:pkNodo_inicial>/<int:pkNodo_actual>/', views.registroEquipos),
    path('list_equipo_red/', views.listEquiposRed),

    path('reg_mantenimiento_equipo/<int:pkEquipo>/', views.registroMantenimientoEquipos),
    path('reg_movimiento_equipo/<int:pkEquipo>/<int:pkNodoSalida>/<int:pkNodoLlegada>/', views.registroMovimiento_Equipos),



]