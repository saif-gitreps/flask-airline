from datetime import datetime
from mongoengine import *
from dotenv import load_dotenv
import os

load_dotenv()

connect(host=os.getenv("MONGO_URI"))

class Flight(Document):
    adminId = StringField(ReferenceField("User"))
    flightNumber = StringField(required=True)
    flightDate = DateTimeField(required=True)
    _from = StringField(required=True)
    destination = StringField(required=True)
    seatNumber = IntField(required=True)
    isBooked = BooleanField(default=False)
    createdAt = DateTimeField(default=datetime.now)
    
    def to_json(self):
        return {
            "id": str(self.id),
            "flightNumber": self.flightNumber,
            "departure": self.departure,
            "destination": self.destination,
            "departureTime": self.departureTime,
            "arrivalTime": self.arrivalTime,
            "seatNumber": self.seatNumber,
            "isBooked": self.isBooked,
            "createdAt": self.createdAt
        }