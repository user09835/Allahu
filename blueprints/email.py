from flask import Blueprint, render_template

email_blueprint = Blueprint('email', __name__, template_folder='../templates')

@gen_blueprint.route('/email')
def email():
    return render_template('email.html')
