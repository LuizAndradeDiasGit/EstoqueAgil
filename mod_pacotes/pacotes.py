from flask import Blueprint, render_template
bp_pacotes = Blueprint('pacotes', __name__, url_prefix="/pacotes", template_folder='templates')

@bp_pacotes.route("/")
def rotaPacotes():
 return render_template('formPacotes.html')