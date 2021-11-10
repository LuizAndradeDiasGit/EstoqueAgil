from flask import Blueprint, render_template, request, redirect, url_for,session
bp_login = Blueprint('login', __name__, url_prefix="/", template_folder='templates')
from mod_cad_usu.cadUsuBD import Usuarios
from funcoes import Funcoes, LOG

@bp_login.route("/", methods = ['GET','POST'])
def login():
 return render_template('formLogin.html')

@bp_login.route("/login", methods=['POST'])
def validaLogin():
  _msg = ""
  try:
# cria o objeto e armazena o usuario e senha digitado
    usuario = Usuarios()
    usuario.matricula = request.form['usuario']
    usuario.senha = Funcoes.cifraSenha(request.form['senha'])
# realiza a busca pelo usuario e armazena o resultado no objeto
    _msg = usuario.selectLogin()
# verifica se usuario foi encontrado
    if usuario.id_usuario > 0:
# limpa a sessão
      session.clear()
# registra usuario na sessão, armazenando o login do usuário
      session['usuario'] = usuario.nome
      session['matricula'] = usuario.matricula
      session['grupo'] = usuario.grupo

      Funcoes.criaLOG(LOG.info, LOG.login.value, request.path, session['matricula'], '')


# abre a aplicação na tela home
      return redirect(url_for('home.rotaHome'))
    else:
# retorna para a tela de login
      return redirect(url_for('login.login', falhaLogin=1))
  except Exception as e:
    _msg, _msg_exception = e.args 
    return redirect(url_for('login.login', mensagem=_msg, mensagem_exception=_msg_exception))
 