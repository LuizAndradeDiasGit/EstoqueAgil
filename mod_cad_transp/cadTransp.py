from flask import Blueprint, render_template
bp_cad_transp = Blueprint('cadTransp', __name__, url_prefix="/cadTransp", template_folder='templates')

@bp_cad_transp.route("/")
def rotaCadTransp():
 return render_template('formcadTransp.html')