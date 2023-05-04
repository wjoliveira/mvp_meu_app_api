from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Clientes

class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser cadastrado deve ser representado
    """
    nome_do_cliente: str = "Wellington de Jesus Oliveira"
    email_do_cliente: str = "wellington.dejesusoliveira@email.com.br"
    telefone_do_cliente: str = "219XXXXXXXX"


class ListagemClientesSchema(BaseModel):
    """ Define como uma listagem de clientes será retornada.
    """
    clientes:List[ClienteSchema]


def exibe_clientes(clientes: List[Clientes]):
    """ Retorna uma representação dos clientes seguindo o schema definido em ClienteViewSchema
    """
    result = []
    for cliente in clientes:
        result.append({
            "id_do_cliente": cliente.id_do_cliente,
            "nome_do_cliente": cliente.nome_do_cliente,
            "email_do_cliente": cliente.email_do_cliente,
            "telefone_do_cliente": cliente.telefone_do_cliente
        })

    return {"clientes": result}


class ClienteViewSchema(BaseModel):
    """ Define como um cliente será retornado
    """
    id_do_cliente: int = 1
    nome_do_cliente: str = "Wellington de Jesus Oliveira"
    email_do_cliente: str = "wellington.dejesusoliveira@email.com.br"
    telefone_do_cliente: str = "219XXXXXXXX"


class ClienteDeleteSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de exclusão
    """
    id_do_cliente: int = 1


def exibe_cliente(cliente: Clientes):
    """ Retorna uma representação do cliente seguindo o schema definido em ClienteViewSchema
    """
    return {
        "id_do_cliente": cliente.id_do_cliente,
        "nome_do_cliente": cliente.nome_do_cliente,
        "email_do_cliente": cliente.email_do_cliente,
        "telefone_do_cliente": cliente.telefone_do_cliente
    }