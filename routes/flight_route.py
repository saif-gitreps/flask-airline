from flask import Blueprint
from controller.flight_controller import *

flight_bp = Blueprint('flight', __name__, url_prefix='/api/v1/flights')

@flight_bp.route('/search', methods=['GET'])
def search_for_flights():
    return search_flights()

@flight_bp.route("/", methods=['GET'])
def flights_status():
    return get_flight_status()

@flight_bp.route('/', methods=['POST'])
def add_one_flight():
    return add_flight()

@flight_bp.route("/<flightId>", methods=['GET'])
def get_flight(flightId):
    return get_flight_by_id(flightId)

@flight_bp.route("/<flightId>", methods=['DELETE'])
def remove_one_flight(flightId):
    return remove_flight(flightId)