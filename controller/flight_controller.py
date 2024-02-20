from models.booking_model import Booking
from models.flight_model import Flight
from flask import jsonify, request, session
from datetime import datetime

def search_flights():
    try:
        if not session.get("isAuthenticated"):
            return jsonify({"error": "User not authenticated"}), 401
            
        data = request.json
        _from = data.get("_from")
        destination = data.get("destination")
        flightDate =  data.get("flightDate")
        
        query = {
            "isBooked": False
        }
        
        if _from:
            query["_from"] = _from
        if destination:
            query["destination"] = destination
        if flightDate:
            flightDate = datetime.strptime(flightDate, "%Y-%m-%dT%H:%M")
            query["flightDate"] = flightDate
        
        if _from and destination:
            flights = Flight.objects(_from=_from, destination=destination, isBooked=False)
        elif _from and flightDate:
            flights = Flight.objects(_from=_from, flightDate=flightDate, isBooked=False)
        elif destination and flightDate:
            flights = Flight.objects(destination=destination, flightDate=flightDate, isBooked=False)
        else:
            flights = Flight.objects(**query)
            
        all_flights = [flight.to_json() for flight in flights]
                    
        return jsonify(
            {"message" : "Available flights retrieved successfully ",
             "Data":all_flights}
        ), 200    
        
    except Exception as error:
        return jsonify({"error": str(error)}), 500
   
def get_flight_status():
    try:
        if not session.get("isAdmin") and not session.get("isAuthenticated"):
            return jsonify({"error": "User not authenticated"}), 401
         
        data = request.json
        flightNumber = data.get("flightNumber")
        flightDate = data.get("flightDate")
        
        query = {}
        if flightNumber:
            query["flightNumber"] = flightNumber
        if flightDate:
            query["flightDate"] = flightDate
            
        if flightNumber and flightDate:
            flights = Flight.objects(flightNumber=flightNumber, flightDate=flightDate)
        else:
            flights = Flight.objects(**query)
        
        all_flights = [flight.to_json() for flight in flights]
        
        return jsonify(
            {"message": "Flight retrieved successfully", 
             "Flights": all_flights}
        ), 200
    
    except Exception as error:
        return jsonify({"error": str(error)}), 500
    
def add_flight():
    try:
        if not session.get("isAdmin") and not session.get("isAuthenticated") :
            return jsonify({"error": "User not authorized"}), 401
        
        data = request.json
        
        flightDate = data.get("flightDate" )
        date_format = "%Y-%m-%dT%H:%M"
        
        if Flight.objects(seatNumber=data.get("seatNumber") ,flightNumber=data.get("flightNumber")):
            return jsonify({"error": "Flight with this seat number already exists"}), 400
        
        flight = Flight(
            adminId=session.get("_id"),
            flightNumber=data.get("flightNumber"),
            flightDate=datetime.strptime(flightDate, date_format),
            _from=data.get("_from"),
            destination=data.get("destination"),
            seatNumber=data.get("seatNumber"),
            isBooked=False
        )
        flight.save()
        
        return jsonify({"message": "Flight added successfully"}), 200
    
    except Exception as error:
        return jsonify({"error": str(error)}), 500

def get_flight_by_id(flightId):
    try:
        if not session.get("isAdmin") and not session.get("isAuthenticated"):
            return jsonify({"error": "User not authenticated"}), 401
        
        flight = Flight.objects(id=flightId).first()
        
        if not flight:
            return jsonify({"error": "Flight not found"}), 404
        
        return jsonify(
            {"message": "flight retrieved successfully", 
             "Data" :flight.to_json()}
        ), 200
    
    except Exception as error:
        return jsonify({"error": str(error)}), 500
    
def remove_flight(flightId):
    try:
        if not session.get("isAdmin") and not session.get("isAuthenticated"):
            return jsonify({"error": "User not authprized"}), 401
        
        flight = Flight.objects(id=flightId).first()
        
        if not flight:
            return jsonify({"error": "Flight not found"}), 404
        
        flight.delete()
        
        return jsonify({"message": "Flight removed successfully"}), 200
    
    except Exception as error:
        return jsonify({"error": str(error)}), 500