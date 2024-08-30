from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


NUM_ROWS = 12
SEATS_PER_ROW = 7
NUM_SEATS = NUM_ROWS * SEATS_PER_ROW - 4  # The given condition according to the problem statement

seat_map = []
for r in range(NUM_ROWS):
    row_size = SEATS_PER_ROW if r < NUM_ROWS - 1 else 3
    seat_map.append([False] * row_size)  

@app.route('/seats', methods=['GET'])
def get_seats():
    return jsonify(seat_map)

@app.route('/reserve', methods=['POST'])
def reserve_seats():
    data = request.get_json()
    num_seats = data.get('num_seats')

    if num_seats < 1 or num_seats > SEATS_PER_ROW:
        return jsonify({"error": "You can only book between 1 and 7 seats"}), 400

    # Searching for seats which are available
    for row in range(NUM_ROWS):
        if sum(seat_map[row]) + num_seats <= len(seat_map[row]):
            seats = []
            for col in range(len(seat_map[row])):
                if not seat_map[row][col]:
                    seat_map[row][col] = True
                    seats.append(f"{row+1}{chr(65+col)}")
                    if len(seats) == num_seats:
                        return jsonify(seats)

    # If no single row can fill the request, try to book nearby seats as per the problem statement
    seats = []
    for row in range(NUM_ROWS):
        for col in range(len(seat_map[row])):
            if not seat_map[row][col]:
                seat_map[row][col] = True
                seats.append(f"{row+1}{chr(65+col)}")
                if len(seats) == num_seats:
                    return jsonify(seats)

    return jsonify({"error": "Not enough seats available"}), 400

if __name__ == "__main__":
    app.run(debug=True)