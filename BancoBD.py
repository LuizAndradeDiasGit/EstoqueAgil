import pymssql  # SQLServer


class Banco():
 def __init__(self): 


    host = "127.0.0.1"
    user = "sa"
    password = "luizandrade"
    database = "ESTOQUE"

    self.conexao = pymssql.connect( host=host, user=user, password=password, database=database)
