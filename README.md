# Train Seat Reservation System

This project consists of a backend Flask API and a React frontend for managing seat reservations in a train coach. The system allows users to book seats with a preference for reserving seats in a single row when possible, and to book nearby seats if a single row cannot accommodate the entire request.

## Backend (Flask)

### Overview

The backend is a Flask application that provides two endpoints:

- **GET `/seats`**: Retrieves the current seat map of the coach.
- **POST `/reserve`**: Reserves a specified number of seats.

### Setup

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Install Flask and Flask-CORS:
   ```bash
   pip install Flask Flask-CORS
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

## Frontend (React)

### Overview

The frontend is a React application that displays the seat map and allows users to reserve seats. It interacts with the Flask API to fetch the current seat map and to send seat reservation requests.

### Components

- **SeatMap**: Displays the seat map and provides an interface for reserving seats.

### Setup

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install axios
   ```

3. Run the React application:
   ```bash
   npm start
   ```

## Usage

1. Start the Flask backend and the React frontend.
2. Access the React application in your browser (typically at `http://localhost:3000`).
3. The seat map will be displayed, and you can enter the number of seats to reserve and click "Reserve Seats."

