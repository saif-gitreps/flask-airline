from datetime import datetime
from mongoengine import *
from dotenv import load_dotenv
import os

load_dotenv()

connect(host=os.getenv("MONGO_URI"), db="Airline")

class Booking(Document):
    customerId = ReferenceField("User", required=True)
    flightId = ReferenceField("Flight", required=True)
    seatNumber = IntField(required=True)
    createdAt = DateTimeField(default=datetime.now)

    def to_json(self):
        return {
            "id": str(self.id),
            "customerId": str(self.customerId.id),  
            "flightId": str(self.flightId.id),    
            "seatNumber": self.seatNumber,
            "createdAt": self.createdAt
        }
