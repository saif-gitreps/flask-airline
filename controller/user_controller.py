from models.user_model import User
from flask import jsonify, request, session

def login():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')
        
        user = User.objects(email=email).first()
        
        if not user or not user.verify_password(password) or user.isAdmin or request.method != 'POST':
            return jsonify({'error': 'Bad request or invalid email or password'}), 400
        
        session["_id"] = str(user.id)
        session["isAuthenticated"] = True    
        
        return jsonify({'message': 'User logged in successfully'}), 200

    except Exception as error: 
        error = str(error)
        return jsonify({'error': error }), 500

def login_admin():
    try:
        json = request.json
        email = json.get('email')
        password = json.get('password')
        
        if email and password and request.method == 'POST':
            user = User.objects(email=email).first()
            if user and user.verify_password(password) and user.isAdmin:
                
                session["_id"] = str(user.id)
                session["isAuthenticated"] = True
                session["isAdmin"] = True
                
                return jsonify({'message': 'Admin logged in successfully'}), 
            else:
                return jsonify({'error': 'invalid email or password'}), 400
        else:
            return jsonify({'error': 'Bad request'}), 400
    except Exception as error:
        return jsonify({'error': error }), 500

def logout():
    session.clear()
    return jsonify({'message': 'User logged out successfully'}), 200

def signup():
    try:
        json = request.json
        name = json.get('fullname')
        email = json.get('email')
        password = json.get('password')
        
        if not (name and email and password) and not request.method == 'POST':
            return jsonify({'error': 'Bad request, missing fullname, email, or password'}), 400
        
        if User.objects(email=email):
            return jsonify({'error': 'User with this email already exists'}), 400

        user = User(name=name, email=email)
        user.set_password(password)
        user.save()

        return jsonify({'message': 'User added successfully'}), 201

    except Exception as error:
        return jsonify({'error': str(error)}), 500
        
    