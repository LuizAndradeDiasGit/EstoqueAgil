from flask import Blueprint, render_template
bp_home = Blueprint('home', __name__, url_prefix="/", template_folder='templates')

@bp_home.route("/")
def rotaHome():
 return render_template('formHome.html')
