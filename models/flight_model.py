from datetime import datetime
from mongoengine import *
from dotenv import load_dotenv
import os

load_dotenv()

connect(host=os.getenv("MONGO_URI"), db="Airline")

class Flight(Document):
    adminId = ReferenceField("User") 
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
            "adminId": str(self.adminId.id),  
            "flightNumber": self.flightNumber,
            "flightDate": self.flightDate,
            "_from": self._from,
            "destination": self.destination,
            "seatNumber": self.seatNumber,
            "isBooked": self.isBooked,
            "createdAt": self.createdAt
        }
