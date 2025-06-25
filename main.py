from fasthtml.common import *
from componentes import *
import requests

url = "http://127.0.0.1:8000/pedidos/"
url2 = "http://127.0.0.1:8000/pedidos/pedido?id="
response = requests.get(url)
item = response.json()

app, routes = fast_app()

lista_api = []

@routes("/listar")
def homepage2():
    form1 = gerar_form()
    elemento_lista_api = gerar_tab_api(item)
    campos = gerar_campos()
    return Titled("Lista de API", form1, elemento_lista_api, campos)


@routes("/buscar_id", methods=["get"])
def consultar(cod: int):
    url3 = f'{url2}{cod}'
    print(url3)
    response = requests.get(url3)
    data = response.json()
    print(data)
    if data != {'msg': 'não encontrado'}:
        return preencher_campos(data)
    else:
        return gerar_campos_naoencontrado()


serve()