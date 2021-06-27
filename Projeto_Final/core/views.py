from django.shortcuts import render, redirect
from core.forms import FormCliente, FormProduto,FormVenda
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from core.models import Cliente, Produto, Venda
from django.contrib import messages


def home(request):
    return render(request, 'core/index.html')


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


@login_required()
def cadastro_cliente(request):
    form = FormCliente(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    else:
        contexto = {'form': form}
        return render(request, 'core/cadastro_cliente.html', contexto)


@login_required()
def cadastro_produto(request):
    form = FormProduto(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    else:
        contexto = {'form': form}
        return render(request, 'core/cadastro_produto.html', contexto)


def listagem_produtos(request):
    if request.user.is_staff:
        if request.POST and request.POST['produto_input']:
            dados = Produto.objects.filter(nome=request.POST['produto_input'])
        else:
            dados = Produto.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/listagem_produtos.html', contexto)
    else:
        return render(request, 'core/nao_autorizado.html')


@login_required()
def listagem_clientes(request):
    if request.user.is_staff:
        if request.POST and request.POST['cliente_input']:
            dados = Cliente.objects.filter(nome=request.POST['cliente_input'])
        else:
            dados = Cliente.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/listagem_clientes.html', contexto)
    else:
        return render(request, 'core/nao_autorizado.html')


def listagem_vendas(request):
    if request.user.is_staff:
        if request.POST and request.POST['venda_input']:
            dados = Venda.objects.filter(nome=request.POST['venda_input'])
        else:
            dados = Venda.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/listagem_vendas.html', contexto)
    else:
        return render(request, 'core/nao_autorizado.html')


@login_required()
def cadastro_venda(request):
    form = FormVenda(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    else:
        contexto = {'form': form}
        return render(request, 'core/cadastro_venda.html', contexto)


@login_required()
def atualiza_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente atualizado com sucesso !! ")
            return redirect('url_listagem_clientes')
        else:
            contexto = {'form': form, 'texto_titulo': 'Atualização de Cliente',
                        'texto_botao': 'Atualizar', 'url_voltar': 'listagem_clientes', 'texto_title': 'AtuCli'}
            return render(request, 'core/cadastro_cliente.html', contexto)
    else:
        return render(request, 'core/nao_autorizado.html')


@login_required()
def exclui_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        if request.POST:
            obj.delete()
            messages.success(request, "Cliente excluido com sucesso !! ")
            return redirect('url_listagem_clientes')
        else:
            contexto = {'dados': obj.nome, 'id': obj.id, 'url': 'listagem_clientes'}
            return render(request, 'core/confirma_exclusao.html', contexto)
    else:
        return render(request, 'core/nao_autorizado.html')


def atualiza_produto(request, id):
    if request.user.is_staff:
        obj = Produto.objects.get(id=id)
        form = FormProduto(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado com sucesso !! ")
            return redirect('url_atualiza_produto')
        else:
            contexto = {'form': form, 'texto_titulo': 'Atualização de Cliente',
                        'texto_botao': 'Atualizar', 'url_voltar': 'listagem_clientes', 'texto_title': 'AtuCli'}
            return render(request, 'core/cadastro_produto.html', contexto)
    else:
        return render(request, 'core/nao_autorizado.html')


@login_required()
def exclui_produto(request, id):
    if request.user.is_staff:
        obj = Produto.objects.get(id=id)
        if request.POST:
            obj.delete()
            messages.success(request, "Produto excluido com sucesso !! ")
            return redirect('url_listagem_produtos')
        else:
            contexto = {'dados': obj.fabricante, 'modelo': obj.modelo, 'url': 'listagem_produtos'}
            return render(request, 'core/confirma_exclusao.html', contexto)
    else:
        return render(request, 'core/nao_autorizado.html')
