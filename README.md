## Airline System Backend Server 

This backend server is built using Flask, MongoDB, and mongoengine, following the MVC (Model-View-Controller) pattern.

### Installation

1. Clone the repository from GitHub:

```bash
git clone <repository_url>
```

2. Install dependencies using pip:

```bash
pip install -r requirements.txt
```

### Configuration

1. Create a `.env` file in the root directory with the following environment variables:

```plaintext
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=<your_secret_key>
MONGODB_URI=<your_mongodb_uri>
```

### Running the Server

To run the server, execute the following command:

```bash
flask run
```

By default, the server will run on `http://localhost:5000`.

### Endpoints

#### Authentication and User operation (Admin and Customer)

- `/api/v1/login`:
  - POST: to login an existing customer.
- `/api/v1/signup`:
  - POST: create a new account for a customer.
- `/api/v1/logout`:
  - POST: removes session and logs out all types of user.
- `/api/v1/login/admin`:
  - POST: to login an existing admin.
- `/api/v1/login`:
  - POST: create a new account for an admin.


#### Flight Routes Operation

- `/api/v1/flights/search`: 
  - GET: Search for flights by date, to or from.
- `/api/v1/flights/`: 
  - GET: Get all the flights status(Admin operation).
- `/api/v1/flights/`: : 
  - POST: Add a flight (Admin operation).
- `/api/v1/flights/<flightId>`: 
  - GET: Get the status of a particular flight (Admin operation).
- `/api/v1/flights/<flightId>`: 
  - DELETE: Delete a flight (Admin operation).

#### Booking Operations

- `/api/v1/book`:
  - GET: Get all the bookings made by the customer.
- `/api/v1/book/<flightId>`:
  - POST: Book a flight.

### Models

The application uses the following models:

1. **User Model**: Represents users of the system.
2. **Flight Model**: Represents flight information.
3. **Booking Model**: Represents a booking made by a customer.

### Folder Structure

- `app.py`: Main Flask application file.
- `controllers/`: Contains controller logic.
- `models/`: Contains data models.
- `routes/`: Contains all the routes for the endpoints

### Dependencies

- **Flask**: Micro web framework for Python.
- **mongoengine**: Object-Document Mapper (ODM) for working with MongoDB in Python.
- **PyMongo**: Python driver for MongoDB.
