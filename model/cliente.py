from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from typing import Union

from model import Base

class Clientes(Base):
    __tablename__ = 'clientes'

    id_do_cliente = Column("pk_cliente", Integer, primary_key=True)
    nome_do_cliente = Column(String(140), unique=True)
    email_do_cliente = Column(String(255))
    telefone_do_cliente = Column(String(11))
    data_de_cadastro_do_cliente = Column(DateTime, default=datetime.now())

    # definição das informações esperadas no cadastro do cliente
    def __init__(self, 
                 nome_do_cliente:str, 
                 email_do_cliente:str, 
                 telefone_do_cliente:str, 
                 data_de_cadastro_do_cliente:Union[DateTime, None] = None):
        """
        Cadastrar um Cliente
        Arguments:
            nome_do_cliente: O nome completo do cliente.
            email_do_cliente: E-mail de contato do cliente.
            telefone_do_cliente: Telefone de contato do cliente.
            data_de_cadastro_do_cliente: Data de quando o cliente foi cadastrado no banco de dados
        """
        self.nome_do_cliente = nome_do_cliente
        self.email_do_cliente = email_do_cliente
        self.telefone_do_cliente = telefone_do_cliente

        # se a data não for informada, será utilizada a data exata da inserção no banco de dados
        if data_de_cadastro_do_cliente:
            self.data_de_cadastro_do_cliente = data_de_cadastro_do_cliente
