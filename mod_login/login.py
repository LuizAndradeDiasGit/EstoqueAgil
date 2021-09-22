from flask import Blueprint, render_template
bp_login = Blueprint('login', __name__, url_prefix="/login", template_folder='templates')

@bp_login.route("/")
def rotaLogin():
 return render_template('formLogin.html')