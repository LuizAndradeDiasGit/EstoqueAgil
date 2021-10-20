
from BancoBD import Banco
class Usuarios(object):
    def __init__(self, id_usuario=0,  nome = "",   matricula = "",   cpf = "", grupo="SOLIC",   cargo = "",   cep = "",   pais = "",   uf = "",   cidade = "",   bairro = "",   rua = "",   numero = "",   complemento = "",   telefone = "",   data_nasc = "",   sexo = "",   email = "",   senha = ""):

            self.id_usuario = id_usuario
            self.nome = nome
            self.matricula = matricula
            self.cpf = cpf
            self.grupo = grupo
            self.cargo = cargo
            self.cep = cep
            self.pais = pais
            self.uf = uf
            self.cidade = cidade
            self.bairro = bairro
            self.rua = rua
            self.numero = numero
            self.complemento = complemento
            self.telefone = telefone
            self.data_nasc = data_nasc
            self.sexo = sexo
            self.email = email
            self.senha = senha
            
            

    def selectALL(self):
        
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "SELECT ID_USUARIO, NOME, MATRICULA, CPF, GRUPO, CARGO, CEP, PAIS, UF, CIDADE, BAIRRO, RUA, NUMERO, COMPLEMENTO, TELEFONE, DATA_NASC, SEXO, EMAIL, SENHA FROM TB_USUARIOS"
            _sql_data = ()
            c.execute(_sql, _sql_data)
            result = c.fetchall()
            return result
        except Exception as e:
            raise Exception("Ocorreu um erro na busca do Usuário!", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()
 ############################       
    def selectONE(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "SELECT ID_USUARIO, NOME, MATRICULA, CPF, GRUPO, CARGO, CEP, PAIS, UF, CIDADE, BAIRRO, RUA, NUMERO, COMPLEMENTO, TELEFONE, DATA_NASC, SEXO, EMAIL, SENHA"\
                   " FROM TB_USUARIOS" \
            " WHERE ID_USUARIO = %s"
            _sql_data = (self.id_usuario)
            c.execute(_sql, _sql_data)
            for linha in c:
                self.id_usuario = linha[0]
                self.nome = linha[1]
                self.matricula = linha[2]
                self.cpf = linha[3]
                self.grupo = linha[4]
                self.cargo = linha[5]
                self.cep = linha[6]
                self.pais = linha[7]
                self.uf = linha[8]
                self.cidade = linha[9]
                self.bairro = linha[10]
                self.rua = linha[11]
                self.numero = linha[12]
                self.complemento = linha[13]
                self.telefone = linha[14]
                self.data_nasc = linha[15]
                self.sexo = linha[16]
                self.email = linha[17]
                self.senha = linha[18]
            return "Busca feita com sucesso!"
        except Exception as e:
            raise Exception("Ocorreu um erro na busca do usuario!", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

############################
    def insert(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "INSERT INTO TB_USUARIOS (NOME, MATRICULA, CPF, GRUPO, CARGO, CEP, PAIS, UF, CIDADE, BAIRRO, RUA, NUMERO, COMPLEMENTO, TELEFONE, DATA_NASC, SEXO, EMAIL, SENHA) " \
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            _sql_data = (self.nome, self.matricula, self.cpf, self.grupo , 
            self.cargo, self.cep, self.pais, self.uf, self.cidade, self.bairro, self.rua , 
            self.numero, self.complemento, self.telefone, self.data_nasc, self.sexo , 
            self.email, self.senha )

            c.execute(_sql, _sql_data)
            banco.conexao.commit()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            raise Exception('Erro ao tentar cadastrar Usuário!', str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

############################ nm
    def update(self):
        banco = None
        c = None
        try:
            banco = Banco()    
            c = banco.conexao.cursor()
            _sql = "UPDATE TB_USUARIOS " \
            "SET NOME = %s,MATRICULA = %s,CPF = %s,GRUPO = %s,CARGO = %s,"\
	        "CEP = %s,PAIS = %s,UF = %s,CIDADE = %s,BAIRRO = %s,RUA = %s,NUMERO = %s,"\
	        "COMPLEMENTO = %s,TELEFONE = %s,DATA_NASC = %s,SEXO = %s,EMAIL = %s,SENHA = %s"\
            " WHERE ID_USUARIO = %s"

            _sql_data = (self.nome, self.matricula, self.cpf, self.grupo , 
            self.cargo, self.cep, self.pais, self.uf, self.cidade, self.bairro, self.rua , 
            self.numero, self.complemento, self.telefone, self.data_nasc, self.sexo , 
            self.email, self.senha, self.id_usuario )

            c.execute(_sql, _sql_data)
            banco.conexao.commit()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            raise Exception("Erro ao editar usuário!", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

###########################
    def delete(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "DELETE FROM TB_USUARIOS WHERE ID_USUARIO = %s"
            _sql_data = (self.id_usuario)
            c.execute(_sql, _sql_data)
            banco.conexao.commit()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            raise Exception("Erro ao tentar excluir", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()
#########################
    def selectLogin(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "select id_usuario,nome,matricula,grupo from tb_usuarios where matricula = %s and senha = %s"
            _sql_data = (self.matricula, self.senha,)
            c.execute(_sql, _sql_data)
            for linha in c:
                self.id_usuario = linha[0]
                self.nome = linha[1]
                self.matricula = linha[2]
                self.grupo = linha[3]
            return "Busca feita com sucesso!"
        except Exception as e:
            raise Exception('Erro na busca!', str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()   




