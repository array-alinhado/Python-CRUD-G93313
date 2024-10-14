# SQL
# Linguagem de consulta estruturada.

# SELECT * FROM CLIENTES.

# I/O
# I = input (entrada)
# O = output (saida)

# nome, sabrenome, idade.

# ORM



import os
os.system("clls || clear ")
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")



# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()
 
# Criando tabela.


Base = declarative_base()
class Usuario(Base):
    __tablename__ = "usuarios" 


    # Definindo campos da tabela.
    id = Column ("id", Integer, primary_key= True, autoincrement= True)
    nome = Column("nome", String)
    email = Column ("email", String)
    senha = Column ("senha", String)


    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

#Criando tabela no bancon de dados.
Base.metadata.create_all(bind=MEU_BANCO)
# salvando...
usuario = Usuario("carlos", "carlos69@gamail.com", "696969" )
session.add(usuario)
session.commit()

usuario = Usuario(nome= "beatrix", email= "beatrix69@gamail.com", senha= "69sad6969" )
session.add(usuario)
session.commit()

#listando todos os usuario no banco de dados
print("exibindo dados...")
lista_usuario = session.query(Usuario).all()

for usuario in lista_usuario:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")


# Fechando sessão.
session.close()
