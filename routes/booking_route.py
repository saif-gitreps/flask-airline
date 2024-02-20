from flask import Blueprint
from controller.booking_controller import *

booking_bp = Blueprint('booking', __name__, url_prefix='/api/v1/book')

@booking_bp.route('/', methods=['GET'])
def view_bookings():
    return get_bookings()

@booking_bp.route('/<flightId>', methods=['POST'])
def book_one_flight(flightId):
    return book_flight(flightId)