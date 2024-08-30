import React, { useEffect, useState } from 'react';
import axios from 'axios';

const SeatMap = () => {
  const [seatMap, setSeatMap] = useState([]);
  const [numSeats, setNumSeats] = useState(1);
  const [message, setMessage] = useState(null);

  useEffect(() => {
    fetchSeats();
  }, []);

  const fetchSeats = async () => {
    try {
      const response = await axios.get('http://localhost:5000/seats');
      setSeatMap(response.data);
    } catch (error) {
      console.error('Error fetching seat map:', error);
    }
  };

  const handleReserve = async () => {
    try {
      const response = await axios.post('http://localhost:5000/reserve', { num_seats: numSeats });
      setMessage(`Your seats are booked: ${response.data.join(', ')}`);
      fetchSeats();
    } catch (error) {
      setMessage('Error booking seats: ' + error.response.data.error);
    }
  };

  return (
    <div>
      <div>
        Seats:
        {seatMap.map((row, rIndex) => (
          <div key={rIndex} style={{ display: 'flex' }}>
            Row {rIndex + 1}:
            {row.map((seat, sIndex) => (
              <div
                key={sIndex}
                style={{
                  width: '30px',
                  height: '30px',
                  margin: '5px',
                  backgroundColor: seat ? 'red' : 'green',
                  textAlign: 'center',
                  lineHeight: '30px'
                }}
              >
                {seat ? 'X' : 'O'}
              </div>
            ))}
          </div>
        ))}
      </div>
      <input type="number" value={numSeats} onChange={(e) => setNumSeats(parseInt(e.target.value))} min="1" max="7" />
      <button onClick={handleReserve}>Reserve Seats</button>
      {message && <p>{message}</p>}
    </div>
  );
};

export default SeatMap;