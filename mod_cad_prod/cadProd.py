from flask import Blueprint, render_template
bp_cad_prod = Blueprint('cadProd', __name__, url_prefix="/cadProd", template_folder='templates')

@bp_cad_prod.route("/")
def rotaCadProd():
 return render_template('formcadProd.html')