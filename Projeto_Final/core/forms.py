from django.forms import ModelForm
from core.models import Cliente,Produto, Venda


class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class FormProduto(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


class FormVenda(ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'
