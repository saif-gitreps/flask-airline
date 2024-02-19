from datetime import datetime
from mongoengine import *
from dotenv import load_dotenv
import os

load_dotenv()

connect(host=os.getenv("MONGO_URI"))

class Booking(Document):
    customerId = StringField(ReferenceField("User"), required=True)
    flightId = StringField(ReferenceField("Flight"), required=True)
    seatNumber = IntField(required=True)
    createdAt = DateTimeField(default=datetime.now)

    def to_json(self):
        return {
            "id": str(self.id),
            "customerId": self.customerId,
            "flightId": self.flightId,
            "seatNumber": self.seatNumber,
            "createdAt": self.createdAt
        }
    