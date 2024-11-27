from django.db import models
from ckeditor.fields import RichTextField

class TextoPadrao(models.Model):
    identificador = models.CharField(max_length=100, unique=True)
    titulo = models.CharField(max_length=200)
    conteudo = RichTextField()
    categoria = models.CharField(max_length=50, choices=[
        ('PENDENCIA', 'Mensagem de Pendência'),
        ('EMAIL', 'Template de Email'),
        ('RESPOSTA', 'Resposta Padrão')
    ])
    ativo = models.BooleanField(default=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
