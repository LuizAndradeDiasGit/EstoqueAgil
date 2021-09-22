from flask import Blueprint, render_template
bp_envios = Blueprint('envios', __name__, url_prefix="/envios", template_folder='templates')

@bp_envios.route("/")
def rotaEnvios():
 return render_template('formEnvios.html')