""" BANCOS DE DADOS 
    - SQL (LINGUAGEM DE CONSULTA ESTRUTURADA)
    - EXEMPLO:
        - SELECT * FROM CLIENTES;
        - IRÁ CONSULTAR  O BD NA TABELA CLIENTES.

        - SGBD: 
            - GERENCIAR PERMISSSÕES DE ACESSO 
            - ADMINISTRADOR DE BANCO DE DADOS (DBA)
            - CRIAR CONSULTAS PERSONALIZADAS
            - SELECT * FROM CLIENTES;
    - ORM: MAPEAMNETO OBEJETO RELACIONAL 
        - USAR A LINGUAGEM DE PROGRAMAÇÃO PARA MANIPULAR O BANCO DE DADOS 
"""

import os 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de Dados 
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com o banco de dados 
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando Tabela
Base = declarative_base()
class Cliente(Base):
    __tablename__ = " Clientes"

    # Definindo campos de tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classse 
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de Dados.
Base.metadata.create_all(bind=MEU_BANCO)
    
