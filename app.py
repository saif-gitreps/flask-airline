from flask import Flask, session
from flask_cors import CORS
from controller.user_controller import *
from controller.flight_controller import *
from controller.booking_controller import *
from routes.user_route import user_bp
from routes.flight_route import flight_bp
from routes.booking_route import booking_bp

app = Flask(__name__)
app.secret_key = "airline"
CORS(app)

app.register_blueprint(user_bp)
app.register_blueprint(flight_bp)
app.register_blueprint(booking_bp)

if __name__ == "__main__":
    app.run(debug=True)
