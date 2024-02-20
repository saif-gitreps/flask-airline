from flask import Flask, session
from controller.user_controller import *
from controller.flight_controller import *
from controller.booking_controller import *

app = Flask(__name__)
app.secret_key = "airline"

#to do, remove all the single quotes with double quotes

@app.route('/api/v1/login', methods=['POST'])
def login_user():
    return login()

@app.route('/api/v1/signup', methods=['POST'])
def signup_user():
    return signup()

@app.route('/api/v1/logout', methods=['POST'])
def logout_user():
    return logout()

#routes related to booking flight (user related routes).
@app.route('/api/v1/book', methods=['GET'])
def view_bookings():
    return get_bookings()

@app.route('/api/v1/book/<flightId>', methods=['POST'])
def book_one_flight(flightId):
    return book_flight(flightId)

@app.route('/api/v1/flights/search', methods=['GET'])
def search_for_flights():
    return search_flights()

#routes related to flights and admin(admin related routes)
@app.route('/api/v1/login/admin', methods=['POST'])
def login_admin_user():
    return login_admin()

@app.route('/api/v1/signup/admin', methods=['POST'])
def signup_admin():
    return signup_new_admin()

@app.route("/api/v1/flights/status", methods=['POST'])
def flights_status():
    return get_flight_status()

@app.route('/api/v1/flights', methods=['POST'])
def add_one_flight():
    return add_flight()

@app.route("/api/v1/flights/<flightId>", methods=['DELETE'])
def remove_one_flight(flightId):
    return remove_flight(flightId)



if __name__ == "__main__":
    app.run(debug=True)
