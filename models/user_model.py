from datetime import datetime
from mongoengine import *
from bcrypt import hashpw, gensalt, checkpw
from dotenv import load_dotenv
import os

load_dotenv()

connect(host=os.getenv("MONGO_URI"))


class User(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    isAdmin = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.now)
    
    def set_password(self, password):
        self.password = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

    def verify_password(self, password):
        return checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
    def to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "isAdmin": self.isAdmin
        }