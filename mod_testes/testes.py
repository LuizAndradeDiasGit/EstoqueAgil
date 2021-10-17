from flask import Blueprint, render_template
bp_testes = Blueprint('testes', __name__, url_prefix="/testes", template_folder='templates')

@bp_testes.route("/")
def rotaTestes():
 return render_template('testeTabela.html')