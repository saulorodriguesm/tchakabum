"""Projeto_Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import home, cadastro_produto, listagem_produtos, cadastro_cliente, listagem_clientes,\
    listagem_vendas, cadastro_venda, Registrar, atualiza_cliente, exclui_cliente, atualiza_produto,exclui_produto
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registrar/', Registrar.as_view(), name='url_registrar'),
    path('', home, name='url_principal'),
    path('cadastro_cliente/', cadastro_cliente, name='url_cadastro_cliente'),
    path('cadastro_produto/', cadastro_produto, name='url_cadastro_produto' ),
    path('listagem_clientes/', listagem_clientes, name='url_listagem_clientes' ),
    path('listagem_produtos/', listagem_produtos, name='url_listagem_produtos' ),
    path('listagem_vendas/', listagem_vendas, name='url_listagem_vendas' ),
    path('cadastro_venda/', cadastro_venda, name='url_cadastro_venda' ),
    path('atualiza_cliente/<int:id>/', atualiza_cliente, name='url_atualiza_cliente'),
    path('exclui_cliente/<int:id>/', exclui_cliente, name='url_exclui_cliente'),
    path('atualiza_produto/<int:id>/', atualiza_produto, name='url_atualiza_produto'),
    path('exclui_produto/<int:id>/', exclui_produto, name='url_exclui_produto'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)