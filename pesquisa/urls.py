from django.urls import path
from . import views

app_name = 'pesquisa'

urlpatterns = [
    path('avancada/', views.PesquisaAvancadaView.as_view(), name='pesquisa_avancada'),
    path('simplificada/', views.pesquisa_simplificada, name='pesquisa_simplificada'),

]
