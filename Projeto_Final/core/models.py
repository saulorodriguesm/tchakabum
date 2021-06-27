from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100, blank=True, null= True)
    complemento = models.CharField(max_length=100, blank=True, null= True)
    bairro = models.CharField(max_length=50, blank=True, null= True)
    cidade = models.CharField(max_length=100, blank=True, null= True)
    cep = models.CharField(max_length=10, blank=True, null= True)
    email = models.CharField(max_length= 50)
    telefone = models.CharField(max_length=20, blank=True, null= True)
    foto = models.ImageField(upload_to= 'fotos_clientes', blank=True, null= True)


    def __str__(self):
        return f'{self.nome} ({self.id})'


class Meta:
    verbose_name_plural = 'Clientes'


class Produto(models.Model):
    fabricante = models.CharField(max_length=100, blank=True, null= True)
    modelo = models.CharField(max_length=50)
    preco = models.CharField(max_length=50)
    cor = models.CharField(max_length=50, blank=True, null= True)
    tipo = models.CharField(max_length=50)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_produtos', blank=True, null= True)
    observacao = models.TextField(blank=True,null=True)


    def __str__(self):
            return f'{self.modelo} ({self.tipo})'


class Meta:
    verbose_name_plural = 'Produtos'

class Venda(models.Model):
    valor_total = models.CharField(max_length=20)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    observacao = models.TextField(blank=True,null=True)
    def __str__(self):
            return f'{self.valor_total} ({self.id_cliente})'


class Meta:
    verbose_name_plural = 'Vendas'


class Veiculo(models.Model):
    Nada = models.CharField


