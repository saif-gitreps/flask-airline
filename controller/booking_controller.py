from models.booking_model import Booking
from models.flight_model import Flight
from flask import jsonify, request, session

def book_flight(flightId):
    try:
        if not session.get('isAuthenticated'):
            return jsonify({'error': 'User not authenticated'}), 401
              
        flight = Flight.objects(id=flightId).first()
        
        customerId = request.session['_id']
        
        if not flight or flight.isBooked == True:
            return jsonify({'error': 'Flight not found or is booked already'}), 404
        
        bookedFlight = Booking(customerId = customerId, flightId = flightId, seatNumber = flight.seatNumber)
        
        flight = Flight.objects(id=flightId).update(isBooked=True)
        bookedFlight.save()
        
        return jsonify({'message': 'Flight booked successfully'}), 200
        
    except Exception as error:
        return jsonify({'error': str(error)}), 500
        
    
def get_bookings():
    try:
        if not session.get('isAuthenticated'):
            return jsonify({'error': 'User not authenticated'}), 401
        
        customerId = session['_id']
        
        bookings = Booking.objects(customerId=customerId)
        
        return jsonify(bookings), 200
    
    except Exception as error:
        return jsonify({'error': str(error)}), 500