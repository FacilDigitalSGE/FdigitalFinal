
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.urls import reverse





def admin_dashboard(request):
    return render(request, 'comunicacoes/admin/dashboard.html')

def admin_textos(request):
    return render(request, 'comunicacoes/admin/textos.html')

def admin_configuracao(request):
    return render(request, 'comunicacoes/admin/configuracao.html')

from django.template.loader import render_to_string
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.urls import reverse

def admin_textos_status(request):
    status_mapping = {
        'Aguardando Análise': ('fas fa-info-circle', 'br-tag info'),
        'Em análise': ('fas fa-search', 'br-tag warning'),
        'Concluída': ('fas fa-check-circle', 'br-tag success'),
        'Encaminhada': ('fas fa-check-circle', 'br-tag success'),
        'Com Pendência': ('fas fa-exclamation-circle', 'br-tag warning'),
        'Cancelada pelo Usuário': ('fas fa-times-circle', 'br-tag danger'),
        'Cancelada pelo Sistema': ('fas fa-times-circle', 'br-tag danger')
    }

    table_data = [
        [f'<span class="{status_mapping["Aguardando Análise"][1]}"><i class="{status_mapping["Aguardando Análise"][0]}"></i> Aguardando Análise</span>',
         "Prezado(a) requerente, informamos que sua solicitação foi registrada pela Rede Fácil e será respondida em um prazo máximo de 10 (dez) dias úteis.",
         f'<button class="br-button secondary small" type="button" onclick="window.location.href=\'{reverse("comunicacoes:editar_texto_status")}\'"><i class="fas fa-edit"></i>Editar</button>'],
        
        [f'<span class="{status_mapping["Em análise"][1]}"><i class="{status_mapping["Em análise"][0]}"></i> Em análise</span>',
         "Prezado(a) requerente, informamos que sua solicitação foi registrada pela Rede Fácil e será respondida em um prazo máximo de 10 (dez) dias úteis.",
         f'<button class="br-button secondary small" type="button" onclick="window.location.href=\'{reverse("comunicacoes:editar_texto_status")}\'"><i class="fas fa-edit"></i>Editar</button>'],
        
        [f'<span class="{status_mapping["Com Pendência"][1]}"><i class="{status_mapping["Com Pendência"][0]}"></i> Com Pendência</span>',
         "Prezado(a) requerente, o atendimento realizado pelo Fácil Digital apresenta uma pendência que deve ser resolvida em até 15 (quinze) dias consecutivos. Caso não ocorra nenhuma ação dentro deste período, a solicitação será automaticamente cancelada.",
         f'<button class="br-button secondary small" type="button" onclick="window.location.href=\'{reverse("comunicacoes:editar_texto_status")}\'"><i class="fas fa-edit"></i>Editar</button>'],
        
        [f'<span class="{status_mapping["Encaminhada"][1]}"><i class="{status_mapping["Encaminhada"][0]}"></i> Encaminhada</span>',
         "Prezado(a) requerente, o atendimento por meio do Fácil Digital está finalizado com o encaminhamento do seu pedido para análise da área competente. Verifique as seções 'Comunique-se enviado' e 'Documentos anexados pelo Fácil', caso aplicável.",
         f'<button class="br-button secondary small" type="button" onclick="window.location.href=\'{reverse("comunicacoes:editar_texto_status")}\'"><i class="fas fa-edit"></i>Editar</button>'],
        
        [f'<span class="{status_mapping["Cancelada pelo Usuário"][1]}"><i class="{status_mapping["Cancelada pelo Usuário"][0]}"></i> Cancelada pelo Usuário</span>',
         "Prezado(a) requerente, informamos que sua solicitação inicial de serviços foi cancelada por iniciativa própria.",
         f'<button class="br-button secondary small" type="button" onclick="window.location.href=\'{reverse("comunicacoes:editar_texto_status")}\'"><i class="fas fa-edit"></i>Editar</button>'],
        
        [f'<span class="{status_mapping["Cancelada pelo Sistema"][1]}"><i class="{status_mapping["Cancelada pelo Sistema"][0]}"></i> Cancelada pelo Sistema</span>',
         "Prezado(a) requerente, comunicamos que sua solicitação foi encerrada automaticamente por ausência de atividade no prazo de 15 (quinze) dias consecutivos. Se ainda possui interesse na questão, por favor, inicie uma nova solicitação.",
         f'<button class="br-button secondary small" type="button" onclick="window.location.href=\'{reverse("comunicacoes:editar_texto_status")}\'"><i class="fas fa-edit"></i>Editar</button>'],
        
        [f'<span class="{status_mapping["Concluída"][1]}"><i class="{status_mapping["Concluída"][0]}"></i> Concluída</span>',
         "Prezado(a) requerente, o atendimento por meio do Fácil Digital está finalizado. Verifique as seções 'Comunique-se enviado' e 'Documentos anexados pelo Fácil', caso aplicável.",
         f'<button class="br-button secondary small" type="button" onclick="window.location.href=\'{reverse("comunicacoes:editar_texto_status")}\'"><i class="fas fa-edit"></i>Editar</button>']
    ]

    grid_content = render_to_string('components/ggrid.html', {
        'grid_id': 'status_grid',
        'title': 'Status',
        'columns': ['Status', 'Texto Padrão', 'Ações'],
        'table_data': table_data
    })

    return render(request, 'comunicacoes/admin/textos_status.html', {'grid_content': grid_content})
def admin_textos_email(request):
    email_mapping = {
        'Abertura de Solicitação': ('fas fa-envelope-open', 'br-tag info'),
        'Pendências': ('fas fa-exclamation-circle', 'br-tag warning'),
        'Solicitação Concluída': ('fas fa-check-circle', 'br-tag success'),
        'Cancelamento pelo Usuário': ('fas fa-times-circle', 'br-tag danger')
    }

    edit_urls = {
        'abertura': reverse('comunicacoes:editar_email_abertura'),
        'pendencias': reverse('comunicacoes:editar_email_pendencias'),
        'concluida': reverse('comunicacoes:editar_email_concluida'),
        'cancelamento': reverse('comunicacoes:editar_email_cancelamento')
    }

    table_data = [
        [f'<span class="{email_mapping["Abertura de Solicitação"][1]}"><i class="{email_mapping["Abertura de Solicitação"][0]}"></i> Abertura de Solicitação</span>',
         "Prezado(a) requerente, sua solicitação foi registrada com sucesso no sistema Fácil Digital...",
         f'<button class="br-button secondary small" type="button" onclick="window.location.href=\'{edit_urls["abertura"]}\'"><i class="fas fa-edit"></i>Editar</button>'],
        
        [f'<span class="{email_mapping["Pendências"][1]}"><i class="{email_mapping["Pendências"][0]}"></i> Pendências</span>',
         "Prezado(a) requerente, identificamos pendências em sua solicitação que precisam ser resolvidas...",
         f'<button class="br-button secondary small" type="button" onclick="window.location.href=\'{edit_urls["pendencias"]}\'"><i class="fas fa-edit"></i>Editar</button>'],
        
        [f'<span class="{email_mapping["Solicitação Concluída"][1]}"><i class="{email_mapping["Solicitação Concluída"][0]}"></i> Solicitação Concluída</span>',
         "Prezado(a) requerente, sua solicitação foi concluída com sucesso...",
         f'<button class="br-button secondary small" type="button" onclick="window.location.href=\'{edit_urls["concluida"]}\'"><i class="fas fa-edit"></i>Editar</button>'],
        
        [f'<span class="{email_mapping["Cancelamento pelo Usuário"][1]}"><i class="{email_mapping["Cancelamento pelo Usuário"][0]}"></i> Cancelamento pelo Usuário</span>',
         "Prezado(a) requerente, confirmamos o cancelamento de sua solicitação conforme requisitado...",
         f'<button class="br-button secondary small" type="button" onclick="window.location.href=\'{edit_urls["cancelamento"]}\'"><i class="fas fa-edit"></i>Editar</button>']
    ]

    grid_content = render_to_string('components/ggrid.html', {
        'grid_id': 'email_grid',
        'title': 'E-mails',
        'columns': ['Tipo de E-mail', 'Texto Padrão', 'Ações'],
        'table_data': table_data
    })

    return render(request, 'comunicacoes/admin/textos_email.html', {'grid_content': grid_content})

def admin_textos_scripts(request):
    table_data = [
        [
            "Aprovação de Desdobro de Caneta", 
            "18/03/2024",
            "Rogério Nogueira",
            "Prezado contribuinte, para solicitar a segunda via do IPTU...",
            '<span class="br-tag">IPTU</span> <span class="br-tag">Segunda Via</span> <span class="br-tag">Tributos</span>',
            f'<button class="br-button secondary small" type="button" onclick="window.location.href=\'{reverse("comunicacoes:editar_script")}\'"><i class="fas fa-edit"></i>Editar</button>'        ],
        [
            "Como deixar o Rogério sem graça", 
            "17/03/2024",
            "Heleni Bueno",
            "Para emissão da Certidão Negativa de Débitos Municipais...",
            '<span class="br-tag">CND</span> <span class="br-tag">Certidões</span>',
            f'<button class="br-button secondary small" type="button" onclick="window.location.href=\'{reverse("comunicacoes:editar_script")}\'"><i class="fas fa-edit"></i>Editar</button>'
        ]
    ]

    grid_content = render_to_string('components/ggrid.html', {
        'grid_id': 'scripts_grid',
        'title': 'Scripts de Atendimento',
        'columns': ['Nome/Descrição', 'Atualização', 'Usuário', 'Texto', 'Serviços Relacionados', 'Ações'],
        'table_data': table_data
    })

    return render(request, 'comunicacoes/admin/textos_scripts.html', {'grid_content': grid_content})

def admin_novo_script(request):
    return render(request, 'comunicacoes/admin/novo_script.html')


def editar_email_abertura(request):
    variaveis_sistema = {
        'nome': '{{nome_requerente}}',
        'data': '{{data_solicitacao}}',
        'numero_chamado': '{{numero_chamado}}',
        'assunto': '{{assunto_solicitacao}}'
    }
    
    texto_atual = {
        'status': 'rascunho',  # rascunho, revisao, publicado
        'conteudo': 'Prezado(a) requerente, sua solicitação foi registrada com sucesso no sistema Fácil Digital...'
    }
    
    return render(request, 'comunicacoes/admin/editar_email_abertura.html', {
        'variaveis': variaveis_sistema,
        'texto': texto_atual
    })

def editar_email_pendencias(request):
    variaveis_sistema = {
        'nome': '{{nome_requerente}}',
        'data': '{{data_solicitacao}}',
        'numero_chamado': '{{numero_chamado}}',
        'assunto': '{{assunto_solicitacao}}'
    }
    
    texto_atual = {
        'status': 'rascunho',
        'conteudo': 'Prezado(a) requerente, identificamos pendências em sua solicitação que precisam ser resolvidas...'
    }
    
    return render(request, 'comunicacoes/admin/editar_email_pendencias.html', {
        'variaveis': variaveis_sistema,
        'texto': texto_atual
    })

def editar_email_concluida(request):
    variaveis_sistema = {
        'nome': '{{nome_requerente}}',
        'data': '{{data_solicitacao}}',
        'numero_chamado': '{{numero_chamado}}',
        'assunto': '{{assunto_solicitacao}}'
    }
    
    texto_atual = {
        'status': 'rascunho',
        'conteudo': 'Prezado(a) requerente, sua solicitação foi concluída com sucesso...'
    }
    
    return render(request, 'comunicacoes/admin/editar_email_concluida.html', {
        'variaveis': variaveis_sistema,
        'texto': texto_atual
    })

def editar_email_cancelamento(request):
    variaveis_sistema = {
        'nome': '{{nome_requerente}}',
        'data': '{{data_solicitacao}}',
        'numero_chamado': '{{numero_chamado}}',
        'assunto': '{{assunto_solicitacao}}'
    }
    
    texto_atual = {
        'status': 'rascunho',
        'conteudo': 'Prezado(a) requerente, confirmamos o cancelamento de sua solicitação conforme requisitado...'
    }
    
    return render(request, 'comunicacoes/admin/editar_email_cancelamento.html', {
        'variaveis': variaveis_sistema,
        'texto': texto_atual
    })

def editar_texto_status(request):
    variaveis_sistema = {
        'nome': '{{nome_requerente}}',
        'data': '{{data_solicitacao}}',
        'numero_chamado': '{{numero_chamado}}',
        'assunto': '{{assunto_solicitacao}}'
    }
    
    texto_atual = {
        'status': 'rascunho',
        'conteudo': 'Prezado(a) requerente, informamos que sua solicitação foi registrada pela Rede Fácil...'
    }
    
    return render(request, 'comunicacoes/admin/editar_texto_status.html', {
        'variaveis': variaveis_sistema,
        'texto': texto_atual
    })

def editar_script(request):
    variaveis_sistema = {
        'nome': '{{nome_requerente}}',
        'data': '{{data_solicitacao}}',
        'numero_chamado': '{{numero_chamado}}',
        'assunto': '{{assunto_solicitacao}}'
    }
    
    texto_atual = {
        'status': 'rascunho',  # rascunho, revisao, publicado
        'conteudo': 'Prezado contribuinte, para solicitar a segunda via do IPTU...'
    }
    
    return render(request, 'comunicacoes/admin/editar_script.html', {
        'variaveis': variaveis_sistema,
        'texto': texto_atual
    })
