from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Clientes
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="MVP Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definição de tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cliente_tag = Tag(name="Clientes", description="Adição, visualização e remoção de clientes à base")


@app.get('/', tags=[home_tag])
def home():
    """ Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect("/openapi")


@app.post("/cliente_cadastrar", tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_cliente(form: ClienteSchema):
    """ Adiciona um novo Cliente à base de dados
        Retorna uma representação dos clientes 
    """
    cliente = Clientes(
        nome_do_cliente=form.nome_do_cliente,
        email_do_cliente=form.email_do_cliente,
        telefone_do_cliente=form.telefone_do_cliente)
    logger.debug(f"Adicionando cliente de nome: '{cliente.nome_do_cliente}'")
    try:
        # Conexão com o banco de dados
        session = Session()
        # adicionando cliente
        session.add(cliente)
        # efetivação do comando de adição de novo cliente na tabela
        session.commit()
        logger.debug(f"Adicionado cliente de nome: '{cliente.nome_do_cliente}'")
        return exibe_cliente(cliente), 200
    
    except Exception as e:
        # em caso de um erro fora do previsto
        error_msg = "Não foi possível gravar novo item."
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome_do_cliente}', {error_msg}")
        return {"message": error_msg}, 400
    

@app.get("/clientes_listar", tags=[cliente_tag],
         responses={"200": ListagemClientesSchema, "404": ErrorSchema})
def get_clientes():
    """ Faz a busca por todos os Clientes cadastrados
        Retorna uma representação da listagem de clientes
    """
    logger.debug(f"Coletando clientes")
    # Conexão com o banco de dados
    session = Session()
    # Realizando a busca
    clientes = session.query(Clientes).all()

    if not clientes:
        # Se não existirem clientes cadastrados
        return {"clientes": []}, 200
    else:
        logger.debug(f"%d clientes localizados" % len(clientes))
        # Retorna a representação de clientes
        print(clientes)
        return exibe_clientes(clientes), 200
    

@app.delete("/cliente_deletar", tags=[cliente_tag],
            responses={"200": ClienteDeleteSchema, "404": ErrorSchema})
def delete_cliente(query: ClienteDeleteSchema):
    """ Deleta um Cliente a partir do id do cliente informado
        Retorna uma mensagem de confirmação da remoção
    """
    #cliente_nome = unquote(unquote(query.nome_do_cliente))
    cliente_id = query.id_do_cliente
    print(cliente_id)
    logger.debug(f"Deletando dados sobre o cliente #{cliente_id}")
    # Conexão com o banco de dados
    session = Session()
    # Fazendo a busca
    contar = session.query(Clientes).filter(Clientes.id_do_cliente == cliente_id).delete()
    session.commit()

    if contar:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado cliente #{cliente_id}")
        return {"message": "Cliente removido", "nome": cliente_id}
    else:
        # se o produto não foi encontrado
        error_msg = "Cliente não encontrado na base "
        logger.warning(f"Erro ao deletar cliente #'{cliente_id}', {error_msg}")
        return {"mesage": error_msg}, 404
