from django.views.generic import TemplateView
from django.utils.safestring import mark_safe

class PesquisaAvancadaView(TemplateView):
    template_name = 'pesquisa/pesquisa_avancada.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Configuração das colunas
        columns = [
            "Protocolo",
            "Assunto",
            "Solicitante",
            "CPF/CNPJ",
            "Data Entrada",
            "Ações"
        ]

        # Dados das linhas
        table_data = [
            [
                '<div class="text-center"><a href="#" class="br-button secondary small"><i class="fas fa-search"></i>2024001234</a></div>',
                '<div class="text-center">Licença de Funcionamento</div>',
                '<div class="text-center">João Silva</div>',
                '<div class="text-center">123.456.789-00</div>',
                '<div class="text-center">15/01/2024</div>',
                '<div class="text-center"><button class="br-button secondary circle small" type="button" title="Visualizar"><i class="fas fa-eye"></i></button> <button class="br-button primary circle small" type="button" title="Editar"><i class="fas fa-edit"></i></button></div>'
            ],
            [
                '<div class="text-center"><a href="#" class="br-button secondary small"><i class="fas fa-search"></i>2024001235</a></div>',
                '<div class="text-center">Certidão Negativa</div>',
                '<div class="text-center">Maria Santos</div>', 
                '<div class="text-center">987.654.321-00</div>',
                '<div class="text-center">16/01/2024</div>',
                '<div class="text-center"><button class="br-button secondary circle small" type="button" title="Visualizar"><i class="fas fa-eye"></i></button> <button class="br-button primary circle small" type="button" title="Editar"><i class="fas fa-edit"></i></button></div>'
            ],
            [
                '<div class="text-center"><a href="#" class="br-button secondary small"><i class="fas fa-search"></i>2024001236</a></div>',
                '<div class="text-center">Alvará Sanitário</div>',
                '<div class="text-center">Empresa XYZ Ltda</div>',
                '<div class="text-center">12.345.678/0001-90</div>', 
                '<div class="text-center">17/01/2024</div>',
                '<div class="text-center"><button class="br-button secondary circle small" type="button" title="Visualizar"><i class="fas fa-eye"></i></button> <button class="br-button primary circle small" type="button" title="Editar"><i class="fas fa-edit"></i></button></div>'
            ]
        ]

        context['grid_id'] = 'pesquisa'
        context['title'] = 'Resultados da Pesquisa'
        context['columns'] = columns
        context['table_data'] = table_data

        return context
    
from django.shortcuts import render

def pesquisa_simplificada(request):
    # Configuração das colunas
    columns = [
        "Protocolo",
        "Assunto",
        "Solicitante", 
        "CPF/CNPJ",
        "Data Entrada",
        "Ações"
    ]

    # Dados das linhas
    table_data = [
        [
            '<div class="text-center"><a href="#" class="br-button secondary small"><i class="fas fa-search"></i>2024001234</a></div>',
            '<div class="text-center">Licença de Funcionamento</div>',
            '<div class="text-center">João Silva</div>',
            '<div class="text-center">123.456.789-00</div>',
            '<div class="text-center">15/01/2024</div>',
            '<div class="text-center"><button class="br-button secondary circle small" type="button" title="Visualizar"><i class="fas fa-eye"></i></button></div>'
        ],
        [
            '<div class="text-center"><a href="#" class="br-button secondary small"><i class="fas fa-search"></i>2024001235</a></div>',
            '<div class="text-center">Certidão Negativa</div>',
            '<div class="text-center">Maria Santos</div>', 
            '<div class="text-center">987.654.321-00</div>',
            '<div class="text-center">16/01/2024</div>',
            '<div class="text-center"><button class="br-button secondary circle small" type="button" title="Visualizar"><i class="fas fa-eye"></i></button></div>'
        ],
        [
            '<div class="text-center"><a href="#" class="br-button secondary small"><i class="fas fa-search"></i>2024001236</a></div>',
            '<div class="text-center">Alvará Sanitário</div>',
            '<div class="text-center">Empresa XYZ Ltda</div>',
            '<div class="text-center">12.345.678/0001-90</div>', 
            '<div class="text-center">17/01/2024</div>',
            '<div class="text-center"><button class="br-button secondary circle small" type="button" title="Visualizar"><i class="fas fa-eye"></i></button></div>'
        ]
    ]

    context = {
        'title': 'Pesquisa Simplificada',
        'grid_id': 'pesquisa',
        'columns': columns,
        'table_data': table_data
    }
    
    return render(request, 'pesquisa/pesquisa_simplificada.html', context)
