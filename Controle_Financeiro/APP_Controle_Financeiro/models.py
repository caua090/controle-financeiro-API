from django.db import models
from django.contrib.auth.models import User
class Categoria(models.Model):
    
    nome = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome}'

class Transacao(models.Model):
    TIPOS = (
        ('R', 'Receita'),
        ('D', 'Despesa'),
    )
    
    tipo = models.CharField(max_length=1, choices=TIPOS)
    categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=200)
    data = models.DateField(auto_now_add=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_tipo_display()} - {self.valor} '
    

