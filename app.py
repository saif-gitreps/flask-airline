from flask import Flask
from flask import Flask
from controller.user_controller import *

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login_user():
    return login()

@app.route('/login/admin', methods=['POST'])
def login_admin_user():
    return login_admin()

@app.route('/logout', methods=['POST'])
def logout_user():
    return logout()

@app.route('/signup', methods=['POST'])
def signup_user():
    return signup()


if __name__ == "__main__":
    app.run(debug=True)
