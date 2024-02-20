from flask import Blueprint
from controller.user_controller import *

user_bp = Blueprint('user', __name__, url_prefix='/api/v1')

@user_bp.route('/login', methods=['POST'])
def login_user():
    return login()

@user_bp.route('/signup', methods=['POST'])
def signup_user():
    return signup()

@user_bp.route('/logout', methods=['POST'])
def logout_user():
    return logout()

@user_bp.route('/login/admin', methods=['POST'])
def login_admin_user():
    return login_admin()

@user_bp.route('/signup/admin', methods=['POST'])
def signup_admin():
    return signup_new_admin()