# do módulo Flask inporte a classe Flask, url_for serve para montar url's internas do servidor web de acordo com o nome da função da rota que você quer.
# render_template: busca na pasta docs um arquivo .html, quanto mandar vairáveis do backend para o frontend.
# JINJA: permite programar no html, jinja é um módulo que vem junto ao flask junto com a instalação

from flask import Flask
from routes.home import home_route
from routes.cliente import cliente_route

# inicialização (tem que estar no topo)
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')

#execução (tem que estar aqui no final)
app.run(debug=True) # quando modificar arquivo e salvar ele vai recarregar o servidor web.