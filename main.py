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
    __tablename__ = "clientes"

    # Definindo campos de tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe 
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de Dados.
Base.metadata.create_all(bind=MEU_BANCO)

# CRUD.
# Create -insert - Salvar.
os.system("cls || clear") 

print("Solicitando dados para o usuário.")
inserir_nome = input("Digite o seu Nome: ")
inserir_email = input("Digite o seu Email: ")
inserir_senha = input("Digite o seu Senha: ")

cliente = Cliente(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(cliente)
session.commit()

# Read - select - Consulta
print("\nExibindo Dados de todos os Clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# U - Update - Atualizar 
print("\nAtualizando dados do Usuário.")
email_cliente = input("Digite o Email que será atualizado: ")

cliente = session.query(Cliente).filter_by(email=email_cliente).first()

if cliente:
    cliente.nome = input("Digite o novo Nome: ")
    cliente.email = input("Digite o novo e-mail: ")
    cliente.senha = input("Digite a nova Senha: ")

    session.commit()
    print("Dados atualizados com sucesso.")
else: 
    print("Cliente não encontrado.")

# Read - select - Consulta
print("\nExibindo Dados de todos os Clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# D - Delete - DELETE - Excluir 
print("\nExcluindo dados do Usuário.")
email_cliente = input("Digite o Email do Cliente que será Excluido: ")

cliente = session.query(Cliente).filter_by(email=email_cliente).first()

if cliente:
    session.delete(cliente)
    session.commit()
    print(f"Cliente {cliente.nome} excluído com sucesso!")
else: 
    print("Cliente não encontrado.")

# Read - select - Consulta
print("\nExibindo Dados de todos os Clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# Read - select - Consulta

