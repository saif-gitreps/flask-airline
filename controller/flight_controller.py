from models.booking_model import Booking
from models.flight_model import Flight
from flask import jsonify, request, session

def search_flights():
    try:
        if not session.get('isAuthenticated'):
            return jsonify({'error': 'User not authenticated'}), 401
            
        data = request.json
        _from = data['from']
        destination = data['destination']
        flightDate = data['flightDate']

        flights = Flight.objects(_from=_from, destination=destination, flightDate=flightDate, isBooked=False)
        
        return jsonify(flights), 200    
        
    except Exception as error:
        return jsonify({'error': str(error)}), 500
   
def get_booked_flights():
    try:
        if not session.get("isAdmin") and not session.get("isAuthenticated"):
            return jsonify({'error': 'User not authenticated'}), 401
         
        data = request.json
        flightNumber = data['flightNumber']
        flightDate = data['flightDate']
        
        flights = Flight.objects(flightNumber = flightNumber, flightDate = flightDate,isBooked = True)
        
        return jsonify(flights), 200
    
    except Exception as error:
        return jsonify({'error': str(error)}), 500
    
def add_flight():
    try:
        if not session.get("isAdmin") and not session.get("isAuthenticated"):
            return jsonify({'error': 'User not authenticated'}), 401
        
        data = request.json
        admindId = request.session['_id']
        flightNumber = data['flightNumber']
        flightDate = data['flightDate']
        _from = data['_from']
        destination = data['destination']
        seatNumber = data['seatNumber']
        
        flight = Flight(admindId, flightNumber, flightDate, _from, destination, seatNumber)
        flight.save()
        
        return jsonify({'message': 'Flight added successfully'}), 200
    
    except Exception as error:
        return jsonify({'error': str(error)}), 500
    
def remove_flight(flightId):
    try:
        if not session.get("isAdmin") and not session.get("isAuthenticated"):
            return jsonify({'error': 'User not authenticated'}), 401
        
        flight = Flight.objects(id=flightId).first()
        
        if not flight:
            return jsonify({'error': 'Flight not found'}), 404
        
        flight.delete()
        
        return jsonify({'message': 'Flight removed successfully'}), 200
    
    except Exception as error:
        return jsonify({'error': str(error)}), 500