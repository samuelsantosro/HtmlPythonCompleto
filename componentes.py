from fasthtml.common import *
from urllib.parse import unquote
     
ar = APIRouter()

def gerar_form():
        
    formulario = Form(
        Input(type="text", name="cod", placeholder="Digite o código para consultar: ", id="cod"),
        Button("Consultar"),
        method="get",
        action="/buscar_id",
        hx_get= "/buscar_id",
        hx_target="#form2",
        hx_swap="outherHTML"
    )
    return formulario


def gerar_tab_api(lista2):
    cab = Thead(Td("Código"), Td("Nome"), Td("Email"), Td("Fone"), Td("Excluir"), Td("Alterar"))
    itens_lista2 = [Tr(Td(item["id"]), 
                    Td(item["nome"]),
                    Td(item["email"]),
                    Td(item["fone"]),
                    Td(A("Excluir", hx_get= "", hx_target="#lista_api",hx_swap="outherHTML")), 
                    Td(A("Alterar", hx_get= "", hx_target="#form2",hx_swap="outherHTML"))) 
                         for i, item in enumerate (lista2)]
   
    lista_local2 = Table(cab, *itens_lista2, id="lista_api")
    return lista_local2

def gerar_tab_usu(lista2):
    cab = Thead(Td("Código"), Td("Nome"), Td("Email"), Td("Senha"), Td("Ativo"), Td("Administrador"))
    itens_lista2 = [Tr(Td(item["id"]), 
                    Td(item["nome"]),
                    Td(item["email"]),
                    Td(item["senha"]),
                    Td(item["ativo"]),
                    Td(item["admin"]))
                         for i, item in enumerate (lista2)]
   
    lista_local2 = Table(cab, *itens_lista2, id="lista_usu")
    return lista_local2

def gerar_campos():
    form2 = Form(
        Label("Código: ", Input(type="text", name="cod", placeholder="Código: ", id="cod")),
        Label("Nome: ", Input(type="text", name="nome", placeholder="Nome: ", id="nome")),
        Label("Email: ", Input(type="email", name="mail", placeholder="Email: ", id="mail")),
        Label("Fone: ", Input(type="tel", name="fone", placeholder="Fone: ", id="fone")),       
        id='form2'        
    )
    return form2

def gerar_campos_naoencontrado():
    form2 = Form(
        Label("Código: ", Input(type="text", name="cod", placeholder="Não encontrado", id="cod")),
        Label("Nome: ", Input(type="text", name="nome", placeholder="Não encontrado", id="nome")),
        Label("Email: ", Input(type="email", name="mail", placeholder="Não encontrado", id="mail")),
        Label("Fone: ", Input(type="tel", name="fone", placeholder="Não encontrado", id="fone")),       
        id='form2'        
    )
    return form2

def preencher_campos(res):
    form2 = Form(
        Label("Código: ", Input(type="text", name="cod", placeholder="Código: ", id="cod", value=str(res["id"]))),
        Label("Nome: ", Input(type="text", name="nome", placeholder="Nome: ", id="nome", value=str(res["nome"]))),
        Label("Email: ", Input(type="email", name="mail", placeholder="Email: ", id="mail", value=str(res["email"]))),
        Label("Fone: ", Input(type="tel", name="fone", placeholder="Fone: ", id="fone", value=str(res["fone"]))),       
        id='form2'        
    )
    return form2

def gerar_form_cadastro():
    form_cadastro = Form(
        Label("Nome: ", Input(type="text", name="nome", placeholder="Nome: ", id="nome")),
        Label("Email: ", Input(type="email", name="email", placeholder="Email: ", id="email")),
        Label("Senha: ", Input(type="password", name="senha", placeholder="senha: ", id="senha")),        
        Button("Cadastar"),
        Br(),Br(),
        Label("Resposta do Servidor: ", Input(type="text", name="resp", placeholder="Resposta: ", id="resp")),
        method="get",
        action="/enviar_cadastrar_usu",
        hx_get= "/enviar_cadastrar_usu",
        hx_target="#resp",
        hx_swap="outerHTML",
        id='form_cadastro'
    )
    return form_cadastro


def preencher_campo_resposta(res):
    campo_resp =  Input(type="text", name="resp", id="resp", value=str(res),  hx_swap="outerHTML")
    return campo_resp

