from fasthtml.common import *
from componentes import *
import requests

url = "http://my-json-server.typicode.com/samuelsantosro/cliente/clientes/"
url3 = "http://127.0.0.1:8000/pedidos/"
#response = requests.get(url)
#data = response.json()
#print(data)

app, routes = fast_app()


lista_tarefas = []
lista_api = []

@routes("/pag2")
def homepage2():
    formulario2 = gerar_formulario2()
    elemento_lista_api = gerar_lista_api(lista_api)
    return Titled("Lista de API", formulario2, elemento_lista_api)

@routes("/pag3")
def homepage3():
    formulario3 = gerar_formulario2()
    elemento_lista_api = gerar_lista_api(lista_api)
    #formulario4 = gerar_formulario4()
    return Titled("Lista de API", formulario3, elemento_lista_api)

@routes("/pag4")
def homepage4():
    formulario4 = gerar_formulario5()
    elemento_lista_api2 = gerar_lista_api_simples(lista_api)
    #formulario4 = gerar_formulario4()
    return Titled("Lista de API", formulario4, elemento_lista_api2)

@routes("/pag5")
def homepage5():
    formulario6 = gerar_formulario6()
    elemento_lista_api3 = gerar_lista_api_simples_id(lista_api)
    #formulario4 = gerar_formulario4()
    return Titled("Lista de API", formulario6, elemento_lista_api3)


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

@routes("/adicionar_api_simples", methods=["post", "get"])
def adicionar_api_simples(tarefa_api: str):
    if tarefa_api:
        lista_api.append(tarefa_api)
    return gerar_lista_api_simples(lista_api)

@routes("/adicionar_api_simples_id", methods=["post", "get"])
def adicionar_api_simples(tarefa_api: str):
    if tarefa_api:
        lista_api.append(tarefa_api)
    return gerar_lista_api_simples_id(lista_api)


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

@routes("/retorna_api")
def consultar_simples():
    url2 = f'{url3}'
    #print(url2)
    response = requests.get(url2)
    data = response.json()
    #print(data["nome"])
    return gerar_consulta_simples(data)

@routes("/retorna_api/pedido?id={posicao}")
def consultar_simples_id(posicao: int):
    print(url3)
    url2 = f'{url3}/pedido?id={posicao}'
    print(url2)
    response = requests.get(url2)
    data = response.json()
    #print(data["nome"])
    return gerar_consulta_simples(data)

serve()