from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^', views.home),
    url(r'^novo', views.novo),
    url(r'^hab_vencidas', views.hab_vencidas),
    url(r'^imprimir/', views.GeneratePdf.as_view()),
    url(r'^editar', views.editar_cliente),
    url(r'^salvar', views.salvar),
    url(r'^visualizar', views.visualizar),
    ]
