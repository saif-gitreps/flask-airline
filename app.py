from flask import Flask, session
from flask import Flask
from flask_session import Session
from controller.user_controller import *
from controller.flight_controller import *
from controller.booking_controller import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_strong_secret_key"  # Replace with a strong, unique secret key
Session(app)

@app.route('/login', methods=['POST'])
def login_user():
    return login()

@app.route('/login/admin', methods=['POST'])
def login_admin_user():
    return login_admin()

@app.route('/signup', methods=['POST'])
def signup_user():
    return signup()

@app.route('/logout', methods=['POST'])
def logout_user():
    return logout()

# adding book flight based on url parameter
@app.route('/book/<flightId>', methods=['POST'])
def book_one_flight(flightId):
    return book_flight(flightId)

@app.route('/book', methods=['GET'])
def view_bookings():
    return get_bookings()

@app.route('/search-flights', methods=['POST'])
def search_for_flights():
    return search_flights()

@app.route("/flights/booked-flights", methods=['GET'])
def booked_flights():
    return get_booked_flights()

@app.route('/flight', methods=['POST'])
def add_one_flight():
    return add_flight()

@app.route("/flight/<flightId>", methods=['DELETE'])
def remove_one_flight(flightId):
    return remove_flight(flightId)



if __name__ == "__main__":
    app.run(debug=True)
