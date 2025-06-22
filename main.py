from fasthtml.common import *
from componentes import *
import requests

url = "https://my-json-server.typicode.com/samuelsantosro/cliente/clientes/"
response = requests.get(url)
data = response.json()
#print(data)

app, routes = fast_app()


lista_tarefas = []
lista_api = []

@routes("/pag2")
def homepage():
    formulario2 = gerar_formulario2()
    elemento_lista_api = gerar_lista_api(lista_api)
    return Titled("Lista de API", formulario2, elemento_lista_api)

@routes("/pag3")
def homepage():
    formulario3 = gerar_formulario2()
    elemento_lista_api = gerar_lista_api(lista_api)
    #formulario4 = gerar_formulario4()
    return Titled("Lista de API", formulario3, elemento_lista_api)


@routes("/")
def homepage():
    formulario = gerar_formulario()
    elemento_lista_tarefas = gerar_lista_tarefas(lista_tarefas)
    return Titled("Lista de Tarefas", formulario, elemento_lista_tarefas)
    


@routes("/adicionar_tarefa", methods=["post"])
def adicionar_tarefa(tarefa: str):
    if tarefa:
        lista_tarefas.append(tarefa)
    return gerar_lista_tarefas(lista_tarefas)

@routes("/adicionar_api", methods=["post", "get"])
def adicionar_api(tarefa_api: str):
    if tarefa_api:
        lista_api.append(tarefa_api)
    return gerar_lista_api(lista_api)


@routes("/deletar/{posicao}")
def deletar(posicao: int):
    if len(lista_tarefas)>posicao:
        lista_tarefas.pop(posicao)
    return gerar_lista_tarefas(lista_tarefas)

@routes("/deletar_api/{posicao}")
def deletar_api(posicao: int):
    if len(lista_api)>posicao:
        lista_api.pop(posicao)
    return gerar_lista_api(lista_api)

@routes("/alterar/{posicao}/{valor}")
def alterar(posicao: int, valor: str):
    if len(lista_tarefas)>posicao:
        lista_tarefas[posicao] = valor
    return gerar_lista_tarefas(lista_tarefas)

@routes("/consultar_api/{posicao}")
def consultar(posicao: int):
    url2 = f'{url}{posicao}'
    #print(url2)
    response = requests.get(url2)
    data = response.json()
    #print(data["nome"])
    return gerar_consulta(data)


serve()


'''
   pag =     Html(
    Head(
    Meta(charset='UTF-8'),
    Meta(http_equiv='X-UA-Compatible', content='IE=edge'),
    Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
    Title('Página Inicial'),
    Link(rel='stylesheet', href='https://github.com/samuelsantosro/HtmlPythonCompleto/blob/main/estilo.css'),
    Script(src='https://github.com/samuelsantosro/HtmlPythonCompleto/blob/main/icone.js')
    ),
    Body(
    Nav(
    Img(src='https://github.com/samuelsantosro/HtmlPythonCompleto/blob/main/img/logo-UNIP.png', cls='logomarca'),
    Label(
    I(cls='fas fa-bars'),
    fr='check',
    cls='checkbtn'
    ),
    Input(type='checkbox', id='check'),
    Ul(
    Li(
    A('Home', href='#')
    ),
    Li(
    A('Arquivos', href='#'),
    Ul(
    Li(
    A('Documentos', href='#')
    ),
    Li(
    A('Outros', href='#')
    )
    )
    ),
    Li(
    A('Cursos', href='#')
    ),
    Li(
    A('Notícias', href='#')
    ),
    Li(
    A('Contato', href='#')
    )
    ),
    cls='menu'
    ),
    Div(
    Aside('Esquerda'),
    Main('Principal'),
    cls='central'
    ),
    Footer('Rodapé')
    ),
    lang='pt-br'
    )
    
    return pag
'''
