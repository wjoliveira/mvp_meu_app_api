from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importação dos elementos definidos no modelo
from model.base import Base
from model.cliente import Clientes

db_path = "database/"
# verifica se o diretório não existe
if not os.path.exists(db_path):
    # caso o diretório não exista, cria o mesmo
    os.makedirs(db_path)

# url de acesso ao banco de dados
db_url = "sqlite:///%s/db.sqlite3" % db_path

# criação da engine de conexão com o banco de dados
engine = create_engine(db_url, echo=False)

# Instância um criador de sessão com o banco de dados
Session = sessionmaker(bind=engine)

# criação do banco de dados, caso ele não exista
if not database_exists(engine.url):
    create_database(engine.url)

# criação das tabelas no banco de dados, caso não existam
Base.metadata.create_all(engine)