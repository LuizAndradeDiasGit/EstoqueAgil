from flask import Blueprint, render_template
bp_cad_usu = Blueprint('cadUsu', __name__, url_prefix="/cadUsu", template_folder='templates')

@bp_cad_usu.route("/")
def rotaCadUsu():
 return render_template('formCadUsu.html')