from fasthtml.common import *
from urllib.parse import unquote
import requests

url = "https://my-json-server.typicode.com/samuelsantosro/cliente/clientes/"


     
ar = APIRouter()


def gerar_titulo(tit, subtit):
    pag1 = Div(
        H1(tit),
        H2(subtit),
        P('outro texto para paragráfo')
    ) 
    return Titled("Página Principal", pag1) 
    
    
def gerar_formulario():
    formulario = Form(
        Input(type="text", name="tarefa", placeholder="Digite a tarefa"),
        method="post",
        action="/adicionar_tarefa",
        hx_post= "/adicionar_tarefa",
        hx_target="#lista_tarefas",
        hx_swap="outherHTML"
    )
    return formulario

def gerar_formulario2():
    formulario2 = Form(
        Input(type="text", name="tarefa_api", placeholder="Digite a busca"),
        Button("Enviar"),
        #Input(type="text", name="resposta", placeholder="Aqui aparece a resposta", id="resp"),
        method="post",
        action="/adicionar_api",
        hx_post= "/adicionar_api",
        hx_target="#lista_api",
        hx_swap="outherHTML"
        
    )
    return formulario2

def gerar_lista_tarefas(lista):
    itens_lista = [Li(tarefa, " - ", 
                      A("Excluir", hx_get= f"/deletar/{i}",  hx_target="#lista_tarefas", hx_swap="outherHTML"), " - ", 
                      A("Alterar", hx_get= f"/alterar/{i}{'/teste'}", hx_target="#lista_tarefas", hx_swap="outherHTML")) for i, tarefa in enumerate(lista)]
    lista_local = Ul(*itens_lista, id="lista_tarefas")
    return lista_local


     

def gerar_lista_api(lista2):
    itens_lista2 = [Li(tarefa_api, " - ", 
                      A("Excluir", hx_get= f"/deletar_api/{i}",  hx_target="#lista_api", hx_swap="outherHTML"), " - ", 
                      A("Consultar API", hx_get= f"/consultar_api/{i}", hx_target="#lista_api", hx_swap="afterend")) for i, tarefa_api in enumerate(lista2)]
   
    lista_local2 = Ul(*itens_lista2, id="lista_api")
    #print(url)
    #print(url1)
    return lista_local2

def gerar_consulta(res):
    '''
    pag = Div(P(str(res)))
    return pag
    '''
    consulta = Form(
        Input(type="text", name="resposta_api", placeholder=f"Resultado da busca - {str(res)}", id="resposta_api"),
        hx_target="#resp",
        hx_swap="afterend"
        )
    
        
    
    return consulta

