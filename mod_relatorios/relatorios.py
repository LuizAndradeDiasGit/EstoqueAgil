from flask import Blueprint, render_template
bp_relatorios = Blueprint('relatorios', __name__, url_prefix="/relatorios", template_folder='templates')

@bp_relatorios.route("/")
def rotaRelatorios():
 return render_template('formRelatorios.html')