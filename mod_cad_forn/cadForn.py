from flask import Blueprint, render_template
bp_cadForn = Blueprint('cadForn', __name__, url_prefix="/cadForn", template_folder='templates')

@bp_cadForn.route("/")
def rotaCadForn():
 return render_template('formCadForn.html')