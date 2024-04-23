from flask import Blueprint, render_template
from database.cliente import CLIENTES #leitura: da pasta 'database' importe o arquivo 'cliente' e a variavel 'clientes'

cliente_route = Blueprint('cliente', __name__)

"""
Rota de Clientes
    - /clientes/ (GET) - Listar os clientes
    - /clientes/ (POST) - inserir o cliente no servidor
    - /clientes/new (GET) - renderizar o formulario para criar um cliente
    - /clientes/<id> (GET) - obter os dados de um cliente
    - /clientes/<id>/edit (GET) - renderizar um formulario para editar um cliente
    - /clientes/<id>/update (PUT) - atualizar os dados do cliente
    - /clientes/<id>/delete (DELETE) - deleta o registro do usuario
"""


@cliente_route.route('/')
def lista_clientes():
    """ listar os clientes """
    return render_template('lista_clientes.html', clientes=CLIENTES)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ inserir os dados do cliente no banco de dados """ # como é apenas para inserir não necessita de template.
    pass


@cliente_route.route('/new') # methods=['GET'] não precisa mencionar, pois por padrão as rotas são GET.
def form_cliente():
    """ formulário para cadastrar um cliente """
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ exibir detalhes do cliente """
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ formulario para editar um cliente """
    return render_template('form_edit_cliente.html') # for_edit_cliente e form_cliente é a mesma coisa, porém um possui id e o outro não. Um é POST pois irá inserir e o outro é PUT pois irá atualizar.

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ atualizar informações do cliente """
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """ deletar informações do cliente """
    pass