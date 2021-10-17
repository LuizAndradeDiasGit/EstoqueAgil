from flask import Blueprint, render_template, request, redirect, url_for,session
bp_login = Blueprint('login', __name__, url_prefix="/", template_folder='templates')

@bp_login.route("/", methods = ['GET','POST'])
def login():
 return render_template('formLogin.html')

@bp_login.route("/login", methods=['POST'])
def validaLogin():
  _name = request.form['usuario']
  _pass = request.form['senha']

  if _name == "abc" and _pass == "abc":
      #limpa a sessão
      session.clear()
      #registra 'usuario' na sessão, armazenando o login do usuario
      session['usuario'] = _name

      # abre a aplicação na tela home
      return redirect(url_for('home.rotaHome'))
  else:
 #retorna para a tela de login
    return redirect(url_for('login.login', falhaLogin=1)) 
     #login não está funcionando'''

 