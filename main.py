from fasthtml.common import *
from componentes import *
import requests


url_lista_ped = "http://127.0.0.1:8000/pedidos/listar"
url_pedido = "http://127.0.0.1:8000/pedidos/pedido?id="
url_cadastro = "http://127.0.0.1:8000/autenticacao/criar_conta"
url_lista_usu = "http://127.0.0.1:8000/autenticacao/listar_usu"

app, routes = fast_app()

#lista_api = []


@routes("/")
def homepage():
    menu = cabecalho()
    return Titled("Pagina Inicial", menu)

@routes("/listar_ped")
def homepage2():
    menu = cabecalho()
    response = requests.get(url_lista_ped)
    item = response.json()
    form1 = gerar_form()
    elemento_lista_api = gerar_tab_api(item)
    campos = gerar_campos()
    return Titled("Lista de API", menu, form1, elemento_lista_api, campos)

@routes("/listar_usu")
def homepage2():
    menu = cabecalho()
    response = requests.get(url_lista_usu)
    item = response.json()
    elemento_lista_usu = gerar_tab_usu(item)
    return Titled("Lista de Usuáios", menu, elemento_lista_usu)

@routes("/buscar_id", methods=["get"])
def consultar(cod: int):
    url3 = f'{url_pedido}{cod}'
    print(url3)
    response = requests.get(url3)
    data = response.json()
    print(data)
    if data != {'msg': 'não encontrado'}:
        return preencher_campos(data)
    else:
        return gerar_campos_naoencontrado()

@routes("/cadastrar_usu")
def homepage3():
    menu = cabecalho()
    form2 = gerar_form_cadastro()
    #resposta = preencher_campo_resposta('resposta')
    return Titled("Cadastrar Usuário", menu, form2)

@routes("/enviar_cadastrar_usu", methods=["get","post"])
def cadastrar_usu(nome: str, email: str, senha: str):
    url_nova = f'{url_cadastro}?email={email}&senha={senha}&nome={nome}'
    response = requests.post(url_nova)
    res = response.json()
    return preencher_campo_resposta(res)

    
serve()