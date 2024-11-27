from django.urls import path
from . import views

app_name = 'comunicacoes'

urlpatterns = [
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/textos/', views.admin_textos, name='admin_textos'),
    path('admin/configuracao', views.admin_configuracao, name='admin_configuracao'),
    path('admin/textos-status/', views.admin_textos_status, name='admin_textos_status'),
    path('admin/textos-status/', views.admin_textos_status, name='admin_textos_status'),
    path('admin/textos-email/', views.admin_textos_email, name='admin_textos_email'),
    path('admin/textos-scripts/', views.admin_textos_scripts, name='admin_textos_scripts'),
    path('admin/textos-scripts/novo/', views.admin_novo_script, name='admin_novo_script'),
    path('admin/textos-email/abertura/editar/', views.editar_email_abertura, name='editar_email_abertura'),
    path('admin/textos-email/pendencias/editar/', views.editar_email_pendencias, name='editar_email_pendencias'),
    path('admin/textos-email/concluida/editar/', views.editar_email_concluida, name='editar_email_concluida'),
    path('admin/textos-email/cancelamento/editar/', views.editar_email_cancelamento, name='editar_email_cancelamento'),


    ]


