
from django.urls import path
from . import views

urlpatterns = [
    path('listnivel/', views.listNivel),
    path('listred/', views.listRed),
    path('listnodo/', views.listNodo),
    path('listtipo/', views.lisTipoIncidente),
    path('regincidente/<int:pkNivel>/<int:pkRed>/<int:pkNodo>/<int:pkTipo>/', views.registroIncidentes),
    path('listincidente/', views.listIncidente),

]