from flask import Flask, render_template, session, request
import os

from mod_home.home import bp_home
from mod_cad_forn.cadForn import bp_cadForn
from mod_produto.produto import bp_produto
from mod_cad_transp.cadTransp import bp_cad_transp
from mod_cad_usu.cadUsu import bp_cad_usu
from mod_envios.envios import bp_envios
from mod_login.login import bp_login
from mod_relatorios.relatorios import bp_relatorios
from mod_pacotes.pacotes import bp_pacotes 
from mod_testes.testes import bp_testes

app = Flask(__name__)

app.secret_key = os.urandom(12).hex()

app.register_blueprint(bp_home)
app.register_blueprint(bp_cadForn)
app.register_blueprint(bp_produto)
app.register_blueprint(bp_cad_transp)
app.register_blueprint(bp_cad_usu)
app.register_blueprint(bp_envios)
app.register_blueprint(bp_login)
app.register_blueprint(bp_relatorios)
app.register_blueprint(bp_pacotes)
app.register_blueprint(bp_testes)


if __name__ == "__main__":
    app.run(debug = True, port = 5000)
