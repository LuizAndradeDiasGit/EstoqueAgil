from base64 import encode
from BancoBD import Banco
from flask import Blueprint, json, render_template, request, jsonify, redirect


class Produtos(object):

    def __init__(self, id_produto=0, descricao="", valor=0):
        self.id_produto = id_produto
        self.descricao = descricao
        self.valor = valor


    def selectALL(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "SELECT id_produto, descricao, valor " \
                   "FROM tb_produtos"
            _sql_data = ()
            c.execute(_sql, _sql_data)
            result = c.fetchall()
            return result
        except Exception as e:
            raise Exception("Ocorreu um erro na busca do produto!", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def selectONE(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "SELECT id_produto, descricao, valor " \
                   "FROM tb_produtos " \
                   "WHERE id_produto = %s"
            _sql_data = (self.id_produto,)
            c.execute(_sql, _sql_data)

            for linha in c:
                self.id_produto = linha[0]
                self.descricao = linha[1]
                self.valor = linha[2]
               

            return "Busca feita com sucesso!"
        except:
            raise Exception("Ocorreu um erro na busca do PRODUTO!", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def insert(self):
        banco = None
        c = None
        try:
            banco = Banco()
           # print(self.imagem)
            c = banco.conexao.cursor()
            _sql = "INSERT INTO tb_produtos(descricao, valor) " \
                "VALUES (%s,%s)"
            _sql_data = (self.descricao, self.valor)
            c.execute(_sql, _sql_data)
            banco.conexao.commit()

            return "Produto cadastrado com sucesso!"
        except Exception as e:
            raise Exception('Erro ao tentar cadastrar produto!', str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def update(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "UPDATE tb_produtos " \
                   "SET descricao=%s,valor=%s" \
                   "WHERE id_produto = %s"
            _sql_data = (self.descricao, self.valor,
                         self.id_produto,)
            c.execute(_sql, _sql_data)
            banco.conexao.commit()

            return "Produto atualizado com sucesso!"
        except Exception as e:
            raise Exception("Erro ao editar produto!", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def delete(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "DELETE FROM tb_produtos " \
                   "WHERE id_produto = %s"
            _sql_data = (self.id_produto)
            c.execute(_sql, _sql_data)
            banco.conexao.commit()

            return "Produto excluído com sucesso!"
        except Exception as e:
            raise Exception("Erro ao tentar excluir produto!", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()