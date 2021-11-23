from hashlib import sha3_256
import logging
from enum import Enum
class LOG(Enum):
    info = 'info'
    warning = 'warning'
    error = 'error'
    debug = 'debug'
    login = 'LOGIN'
    falhalogin = 'FALHA LOGIN'
    logoff = 'LOGOFF'
    excecao = 'EXCEÇÃO'
    sqlInsert = 'Insert'
    sqlUpdate = 'Update'
    sqlDelete = 'Delete'
class Funcoes(object):
    # criptografia de mão única utilizando sha3_256
    # para cifrar as senhas dos usuários no banco de dados
    @staticmethod
    def cifraSenha(senha):
        return sha3_256(senha.encode('utf-8')).hexdigest()

    @staticmethod
    def criaLOG(tipo, status, rota, usuario, mensagem):
      logging.basicConfig(filename='registrolog.log',format='%(levelname)s|%(name)s|%(asctime)s|%(message)s',datefmt='%d/%m/%Y %H:%M:%S', encoding='utf-8',
        level=logging.INFO)
      _msg = f'{status}|{rota}|{usuario}|{mensagem}'
      if tipo == LOG.info:
        logging.info(_msg)
      elif tipo == LOG.warning:
        logging.warning(_msg)
      elif tipo == LOG.error:
        logging.error(_msg)
      elif tipo == LOG.debug:
        logging.debug(_msg)

